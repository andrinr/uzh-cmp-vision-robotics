import numpy as np
import math

def create_cube(d):
    X , Y, Z = np.meshgrid(np.arange(2), np.arange(2), np.arange(-1, 1))
    points_3D = d * np.stack([X.flatten(), Y.flatten(), Z.flatten()], axis = -1)
    points_4D = np.concatenate([points_3D, np.ones([2**3, 1])], axis=-1)

    return points_4D

def create_grid(n, d):

    if (len(n) != 2):
        raise Exception("invalid gridsize")
  
    n_total = n[0] * n[1]
    X , Y = np.meshgrid(np.arange(n[0]), np.arange(n[1]))

    points_2D = d * np.stack([X, Y], axis = -1).reshape([n_total, 2])
    points_3D = np.concatenate([points_2D, np.zeros([n_total, 1])], axis=-1)

    points_4D = np.concatenate([points_3D, np.ones([n_total, 1])], axis=-1)

    return points_4D

def create_grid_3D(n, s, e):

    return