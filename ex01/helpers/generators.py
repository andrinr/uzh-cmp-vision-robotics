import numpy as np
import math

def create_grid(n, s, e):
    if (len(n) == 2):
        return create_grid_2D(n, s, e)
    elif (len(n) == 3):
        return create_grid_3D(n, s, e)
    else:
        raise Exception("invalid gridsize")
  

def create_grid_2D(n, s, e):
    grid = np.zeros((n[0] * n[1], 4))
    i = 0
    for i0 in range(n[0]):
        p0 = (e[0] - s[0]) / n[0] * i0 + s[0]
        for i1 in range(n[1]):
            p1 = (e[1] - s[1]) / n[1] * i1 + s[1]
            grid[i, :] = [p0, p1, s[2], 1]
            i += 1
    return grid

def create_grid_3D(n, s, e):

    return