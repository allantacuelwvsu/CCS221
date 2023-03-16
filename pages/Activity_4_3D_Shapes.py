import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf
import streamlit as st

st.title("Activity4\nGroup6\n3DRotation")
# 3D Rotation by Carado, Molet & Pendon


def _plt_basic_object_(points):
    fig = plt.figure()
    tri = Delaunay(points).convex_hull
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],
                        triangles=tri,
                        shade=True, cmap=cm.rainbow, lw=0.5)
    
    ax.set_xlim3d(-8.5, 8.5)
    ax.set_ylim3d(-8.5, 8.5)
    ax.set_zlim3d(-8.5, 8.5)
    
    ax.set_xlabel ("X axis")
    ax.set_ylabel ("Y Axis")
    ax.set_zlabel ("Z Axis")
    
    plt.show()
    st.pyplot(fig)

def _90deg_(bottom_lower):
    
    bottom_lower = np.array(bottom_lower)
    
    points = np.vstack([
        bottom_lower + [-7.5, -7.5, -7.5],
        bottom_lower + [-7.5, -7.5, 7.5],
        bottom_lower + [7.5, -7.5, -7.5],
        bottom_lower + [-7.5, 7.5, 7.5],
        bottom_lower + [-7.5, 7.5, 7.5],
        bottom_lower + [7.5, 7.5, -7.5],
        bottom_lower + [-7.5, 7.5, -7.5],
    ])
    
    return points

def _pyramid_(bottom_lower):
    0
    bottom_lower = np.array(bottom_lower)
    
    points = np.vstack([
        bottom_lower,
        bottom_lower + [-5, -5, -5],
        bottom_lower + [5, -5, -5],
        bottom_lower + [5, 5, -5],
        bottom_lower + [-5, 5, -5],
        bottom_lower + [0, 0, 1]
    ])
    
    return points

def _diamond_(bottom_lower):

    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,  
        bottom_lower + [0, 3, 0],
        bottom_lower + [0, 0, 5],
        bottom_lower + [3, 0, 0],
        bottom_lower + [0, 0, -5],
        bottom_lower + [3, 0, 0],
        bottom_lower + [0, 3, 0],
        bottom_lower
       
    ])
    
    return points

def _prism_(bottom_lower):
    
    bottom_lower = np.array(bottom_lower)
    
    points = np.vstack([
        bottom_lower + [5, -7.5, -2.5],
        bottom_lower + [5, 5, -2.5],
        bottom_lower + [0, 5, 2.5],
        bottom_lower + [0, -7.5, 2.5],
        bottom_lower + [-5, -7.5, -2.5],
        bottom_lower + [5, 5, -2.5],
        bottom_lower + [-5, 5, -2.5],
        bottom_lower,
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
    
    st.write('Translation Values')
    x = st.slider('X: ', 0, 10, 1)
    y = st.slider('Y: ', 0, 10, 1)
    z = st.slider('Z: ', 0, 10, 1)
    
    bottom_lower=(x, y, z)
    
    shapeChoice = st.selectbox('Choose 3D Shape', ('Pyramid', '90 Degree Angled Shape', 'Diamond', 'Prism'))
    
    if shapeChoice == "Pyramid":
        init_shape_ = _pyramid_(bottom_lower)
        trans = st.selectbox('Choose Transformation', ('Rotation', 'Shear'))
        
        if trans == "Rotation":
            angle = st.slider('Rotation Size : ', 0, 1500, 1)
            with tf.compat.v1.Session() as session:
                object = session.run(rotate_obj(init_shape_, angle))
            
        if trans == "Shear":
            trans2 = st.selectbox('Choose Shear', ('Shear X', 'Shear Y'))
            
            if trans2 == 'Shear Y':
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                yold = st.slider('Y Old:', 0.0, 5.0, 0.001)
                ynew = st.slider('Y New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_y(init_shape_, yold, ynew, zold, znew))
                    
            elif trans2 == 'Shear X':
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                xold = st.slider('X Old:', 0.0, 5.0, 0.001)
                xnew = st.slider('X New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_x(init_shape_, xold, xnew, zold, znew))
            
    
    elif shapeChoice == "90 Degree Angled Shape":
        init_shape_ = _90deg_(bottom_lower)
        
        trans = st.selectbox('Choose Transformation', ('Rotation', 'Shear'))
        
        if trans == "Rotation":
            angle = st.slider('Rotation Size : ', 0, 1500, 1)
            with tf.compat.v1.Session() as session:
                object = session.run(rotate_obj(init_shape_, angle))
            
        if trans == "Shear":
            trans2 = st.selectbox('Choose Shear', ('Shear X', 'Shear Y'))
            
            if trans2 == 'Shear Y':
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                yold = st.slider('Y Old:', 0.0, 5.0, 0.001)
                ynew = st.slider('Y New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_y(init_shape_, yold, ynew, zold, znew))
                    
            elif trans2 == 'Shear X':
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                xold = st.slider('X Old:', 0.0, 5.0, 0.001)
                xnew = st.slider('X New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_x(init_shape_, xold, xnew, zold, znew))
  
    elif shapeChoice == "Diamond":
        init_shape_ = _diamond_(bottom_lower)
        trans = st.selectbox('Choose Transformation', ('Rotation', 'Shear'))
        
        if trans == "Rotation":
            angle = st.slider('Rotation Size : ', 0, 1500, 1)
            with tf.compat.v1.Session() as session:
                object = session.run(rotate_obj(init_shape_, angle))
            
        if trans == "Shear":
            trans2 = st.selectbox('Choose Shear', ('Shear X', 'Shear Y'))
            
            if trans2 == 'Shear Y':
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                yold = st.slider('Y Old:', 0.0, 5.0, 0.001)
                ynew = st.slider('Y New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_y(init_shape_, yold, ynew, zold, znew))
                    
            elif trans2 == 'Shear X':
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                xold = st.slider('X Old:', 0.0, 5.0, 0.001)
                xnew = st.slider('X New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_x(init_shape_, xold, xnew, zold, znew))

    elif shapeChoice == "Prism":
        init_shape_ = _prism_(bottom_lower)
        
        trans = st.selectbox('Choose Transformation', ('Rotation', 'Shear'))
        
        if trans == "Rotation":
            angle = st.slider('Rotation Size : ', 0, 1500, 1)
            with tf.compat.v1.Session() as session:
                object = session.run(rotate_obj(init_shape_, angle))
            
        if trans == "Shear":
            trans2 = st.selectbox('Choose Shear', ('Shear X', 'Shear Y'))
            
            if trans2 == 'Shear Y':
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                yold = st.slider('Y Old:', 0.0, 5.0, 0.001)
                ynew = st.slider('Y New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_y(init_shape_, yold, ynew, zold, znew))
                    
            elif trans2 == 'Shear X':
                zold = st.slider('Z Old:', 0.0, 5.0, 0.001)
                znew = st.slider('Z New:', 0.0, 5.0, 0.001)
                xold = st.slider('X Old:', 0.0, 5.0, 0.001)
                xnew = st.slider('X New:', 0.0, 5.0, 0.001)
                with tf.compat.v1.Session() as session:
                    object = session.run(shear_obj_x(init_shape_, xold, xnew, zold, znew))
        
    _plt_basic_object_(object)
    
if __name__ == '__main__':
    main()
