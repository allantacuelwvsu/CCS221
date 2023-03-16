import numpy as np
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf

tf.compat.v1.disable_eager_execution()

def _plt_basic_object_(points):
    """Plots a basic object, assuming its convex and not too complex"""

    tri = Delaunay(points).convex_hull

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection = '3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],
                        triangles=tri,
                        shade = True, cmap = cm.seismic, lw = 0.5)
    ax.set_xlim3d(-6, 6)
    ax.set_ylim3d(-6, 6)
    ax.set_zlim3d(-6, 6)

    ax.set_xlabel ("X axis")
    ax.set_ylabel ("Y Axis")
    ax.set_zlabel ("Z Axis")
    plt.show()

def _cube_(bottom_lower = (0, 0, 0), side_length = 3):

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

def _prism_(bottom_lower = (0, 0, 0), side_length = 3):

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
    
def _rectangle_(bottom_lower = (0, 0, 0), side_length = 3):

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

def _pyramid_(bottom_lower = (0, 0, 0), side_length = 3):

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

def rotate_obj(points, angle):
    
    angle = float(angle)
    rotation_matrix = tf.stack([[tf.cos(angle), tf.sin(angle), 0],
                                [-tf.sin(angle), tf.cos(angle), 0],
                                [0, 0, 1]
                                ])

    return tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))

def _diamond_(bottom_lower = (0, 0, 0), side_length = 3):

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

def main():
    init_cube_ = _cube_(side_length = 3)
    init_prism_ = _prism_(side_length = 3)
    init_rectangle_ = _rectangle_(side_length = 3)
    init_pyramid_ = _pyramid_(side_length = 3)
    init_diamond_ = _diamond_(side_length = 3)
    points = tf.constant(init_cube_, dtype = tf.float32)
    
    
    choice = (int(input("Which shape do you like to make? [Input 1 for cube, 2 for prism, 3 for rectangle, 4 for pyramid, >5 or <1 for error]: ")))
    if (choice == 1):
        _cube_(bottom_lower = (0, 0, 0), side_length = 5)
        _plt_basic_object_(init_cube_)
    elif (choice == 2):
        _prism_(bottom_lower = (0, 0, 0), side_length = 5)
        _plt_basic_object_(init_prism_)
    elif (choice == 3):
        _rectangle_(bottom_lower = (0, 0, 0), side_length = 5)
        _plt_basic_object_(init_rectangle_) 
    elif (choice == 4):
        _pyramid_(bottom_lower = (0, 0, 0), side_length = 5)
        _plt_basic_object_(init_pyramid_)  
    else:
        print("Error.")
        exit

    choice1 = (int(input("Which of the shapes would you like to rotate? [Input 1 for cube, 2 for prism, 3 for rectangle, 4 for pyramid, >5 or <1 for error]: ")))
    if (choice1 == 1):
            objcttbrttd = "init_cube_"
    elif (choice1 == 2):
            objcttbrttd = "init_prism_"
    elif (choice1 == 3):
            objcttbrttd = "init_rectangle_"
    elif (choice1 == 4):
            objcttbrttd = "init_pyramid_"
    else:
        print("Error.")
        exit
    with tf.compat.v1.Session() as session:
        rotated_object = session.run(rotate_obj(init_pyramid_, 100))
    
    _plt_basic_object_(rotated_object)
    
if __name__ == '__main__':
    main()