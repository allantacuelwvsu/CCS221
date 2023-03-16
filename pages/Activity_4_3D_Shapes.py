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
    
    
    Transformation = st.multiselect('Transformation Type:', ['cube', 'prism', 'rectangle', 'pyramid', 'diamond'])
    
    if ('cube' in Transformation):
        _cube_(bottom_lower = (0, 0, 0), side_length = 5)
        _plt_basic_object_(init_cube_)
    if ('prism' in Transformation):
        _prism_(bottom_lower = (0, 0, 0), side_length = 5)
        _plt_basic_object_(init_prism_)
    if ('rectangle' in Transformation):
        _rectangle_(bottom_lower = (0, 0, 0), side_length = 5)
        _plt_basic_object_(init_rectangle_) 
    if ('pyramid' in Transformation):
        _pyramid_(bottom_lower = (0, 0, 0), side_length = 5)
        _plt_basic_object_(init_pyramid_)  
    if ('diamond' in Transformation):
        _diamond_(bottom_lower = (0, 0, 0), side_length = 5)
        _plt_basic_object_(init_diamond_)
    
if __name__ == '__main__':
    main()
