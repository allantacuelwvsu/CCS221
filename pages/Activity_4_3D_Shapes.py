import numpy as np
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf
import streamlit as st

def _plt_basic_object_(points):
    """Plots a basic object, assuming its convex and not too complex"""
    fig = plt.figure()
    tri = Delaunay(points).convex_hull

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection = '3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],
                        triangles=tri,
                        shade = True, cmap = cm.seismic, lw = 0.5)
    ax.set_xlim3d(-6.5, 6.5)
    ax.set_ylim3d(-6.5, 6.5)
    ax.set_zlim3d(-6.5, 6.5)
    plt.show()
    st.pyplot(fig)

def _cube_(bottom_lower, side_length = 3):

    """Create cube starting from the given bottom-lower point (lowest x, y, z values)"""
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
        bottom_lower + [side_length, 0, side_length],
        bottom_lower
    ])

    return points

def _prism_(bottom_lower, side_length = 3):

    """Create cube starting from the given bottom-lower point (lowest x, y, z values)"""
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],                       #dalom
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [0, 0, 0],
        bottom_lower + [0, 0, 0],
        bottom_lower
    ])

    return points
    
def _rectangle_(bottom_lower, side_length = 3):

    """Create cube starting from the given bottom-lower point (lowest x, y, z values)"""
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, 4, 0],
        bottom_lower + [side_length, 4, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, 4, side_length],
        bottom_lower + [side_length, 4, side_length],
        bottom_lower + [side_length, 0, side_length],
        bottom_lower
    ])

    return points

def _pyramid_(bottom_lower, side_length = 3):

    """Create cube starting from the given bottom-lower point (lowest x, y, z values)"""
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [-3, -3, -3],
        bottom_lower + [3, -3, -3],
        bottom_lower + [3, 3, -3],
        bottom_lower + [-3, 3, -3],
        bottom_lower + [0, 0, 5],               #base
        bottom_lower
    ])

    return points

def _diamond_(bottom_lower, side_length = 3):

    """Create cube starting from the given bottom-lower point (lowest x, y, z values)"""
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [-1, -1, -1],
        bottom_lower + [1, -1, -1],
        bottom_lower + [1, 1, -1],
        bottom_lower + [-1, 1, -1],
        bottom_lower + [0, 0, -5],               #[?, ?, height]
        bottom_lower
    ])

    return points

def rotate_obj(points, angle):
    
    angle = float(angle)
    rotation_matrix = tf.stack([[tf.cos(angle), tf.sin(angle), 0],
                                [-tf.sin(angle), tf.cos(angle), 0],
                                [0, 0, 1]
                                ])

    return tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))

def shear_obj_y(points, yold, ynew, zold, znew):
    
    sh_y = tf.multiply(yold, ynew)
    sh_z = tf.multiply(zold, znew)
   
    shear_points = tf.stack([[sh_y, 0, 0],
                            [sh_z, 1, 0],
                            [0, 0, 1]
                            ])
   
   
    shear_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(shear_points, tf.float32))
    return shear_object

def shear_obj_x(points, xold, xnew, zold, znew):
    
    sh_x = tf.multiply(xold, xnew)
    sh_z = tf.multiply(zold, znew)
   
    shear_points = tf.stack([[1, sh_x, 0],
                            [0, 1, 0],
                            [0, sh_z, 1]
                            ])
   
   
    shear_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(shear_points, tf.float32))
    return shear_object

def main():
    bottom_lower = (0, 0, 0)
    
    Transformation = st.selectbox('Transformation Type:', ['cube', 'prism', 'rectangle', 'pyramid', 'diamond'])
    
    if (Transformation == "cube"):
        init_shape_ = _cube_(bottom_lower, side_length = 5)
        Transform = st.selectbox('Transformation Type:', ('rotate', 'shear'))
        
        if Transform == "rotate":
            st.write('Rotation Control')
            angle = st.slider('Rotation Size : ', 0, 1500, 1)
            with tf.compat.v1.Session() as session:
                object = session.run(rotate_obj(init_shape_, angle))
            
        if Transform == "shear":
            TTransform = st.selectbox('Shear', ('Shear X', 'Shear Y'))
            
            if TTransform == 'Shear Y':
                st.sidebar.write('Shear Y Controls')
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                yold = st.slider('Y Old:', 0.0, 5.0, 0.001)
                ynew = st.slider('Y New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_y(init_shape_, yold, ynew, zold, znew))
                    
            elif TTransform == 'Shear X':
                st.sidebar.write('Shear X Controls')
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                xold = st.slider('X Old:', 0.0, 5.0, 0.001)
                xnew = st.slider('X New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_x(init_shape_, xold, xnew, zold, znew))
        st.pyplot(fig)
            
    elif (Transformation == "prism"):
        init_shape_ = _prism_(bottom_lower, side_length = 5)
        Transform = st.selectbox('Transformation Type:', ('rotate', 'shear'))
        
        if Transform == "rotate":
            st.write('Rotation Control')
            angle = st.slider('Rotation Size : ', 0, 1500, 1)
            with tf.compat.v1.Session() as session:
                object = session.run(rotate_obj(init_shape_, angle))
            
        if Transform == "shear":
            TTransform = st.selectbox('Shear', ('Shear X', 'Shear Y'))
            
            if TTransform == 'Shear Y':
                st.sidebar.write('Shear Y Controls')
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                yold = st.slider('Y Old:', 0.0, 5.0, 0.001)
                ynew = st.slider('Y New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_y(init_shape_, yold, ynew, zold, znew))
                    
            elif TTransform == 'Shear X':
                st.sidebar.write('Shear X Controls')
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                xold = st.slider('X Old:', 0.0, 5.0, 0.001)
                xnew = st.slider('X New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_x(init_shape_, xold, xnew, zold, znew))
    elif (Transformation == "rectangle"):
        init_shape_ = _rectangle_(bottom_lower, side_length = 5)
        Transform = st.selectbox('Transformation Type:', ('rotate', 'shear'))
        
        if Transform == "rotate":
            st.write('Rotation Control')
            angle = st.slider('Rotation Size : ', 0, 1500, 1)
            with tf.compat.v1.Session() as session:
                object = session.run(rotate_obj(init_shape_, angle))
            
        if Transform == "shear":
            TTransform = st.selectbox('Shear', ('Shear X', 'Shear Y'))
            
            if TTransform == 'Shear Y':
                st.sidebar.write('Shear Y Controls')
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                yold = st.slider('Y Old:', 0.0, 5.0, 0.001)
                ynew = st.slider('Y New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_y(init_shape_, yold, ynew, zold, znew))
                    
            elif TTransform == 'Shear X':
                st.sidebar.write('Shear X Controls')
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                xold = st.slider('X Old:', 0.0, 5.0, 0.001)
                xnew = st.slider('X New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_x(init_shape_, xold, xnew, zold, znew))
        st.pyplot(fig)
    elif (Transformation == "pyramid"):
        init_shape_ = _pyramid_(bottom_lower, side_length = 5)
        Transform = st.selectbox('Transformation Type:', ('rotate', 'shear'))
        
        if Transform == "rotate":
            st.write('Rotation Control')
            angle = st.slider('Rotation Size : ', 0, 1500, 1)
            with tf.compat.v1.Session() as session:
                object = session.run(rotate_obj(init_shape_, angle))
            
        if Transform == "shear":
            TTransform = st.selectbox('Shear', ('Shear X', 'Shear Y'))
            
            if TTransform == 'Shear Y':
                st.sidebar.write('Shear Y Controls')
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                yold = st.slider('Y Old:', 0.0, 5.0, 0.001)
                ynew = st.slider('Y New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_y(init_shape_, yold, ynew, zold, znew))
                    
            elif TTransform == 'Shear X':
                st.sidebar.write('Shear X Controls')
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                xold = st.slider('X Old:', 0.0, 5.0, 0.001)
                xnew = st.slider('X New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_x(init_shape_, xold, xnew, zold, znew))
        st.pyplot(fig)
    elif (Transformation == "diamond"):
        init_shape_ = _diamond_(bottom_lower, side_length = 5)
        Transform = st.selectbox('Transformation Type:', ('rotate', 'shear'))
        
        if Transform == "rotate":
            st.write('Rotation Control')
            angle = st.slider('Rotation Size : ', 0, 1500, 1)
            with tf.compat.v1.Session() as session:
                object = session.run(rotate_obj(init_shape_, angle))
            
        if Transform == "shear":
            TTransform = st.selectbox('Shear', ('Shear X', 'Shear Y'))
            
            if TTransform == 'Shear Y':
                st.sidebar.write('Shear Y Controls')
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                yold = st.slider('Y Old:', 0.0, 5.0, 0.001)
                ynew = st.slider('Y New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_y(init_shape_, yold, ynew, zold, znew))
                    
            elif TTransform == 'Shear X':
                st.sidebar.write('Shear X Controls')
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                xold = st.slider('X Old:', 0.0, 5.0, 0.001)
                xnew = st.slider('X New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_x(init_shape_, xold, xnew, zold, znew))
        st.pyplot(fig)
        
    _plt_basic_object_(object)
    
if __name__ == '__main__':
    main()
