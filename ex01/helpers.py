import numpy as np
import math

def projects_point(point, K, M):

    return K * (M * point)

def create_transformation_matrix(w, t):
    theta = np.linalg.norm(w)
    k = w / theta
    cpk = np.array([[0, -k[0], k[1]],
                    [k[2], 0, -k[0]],
                    [-k[1], k[0], 0]])
    R = np.identity(3) + math.sin(theta) * cpk +\
        (1 - math.cos(theta)) * cpk

    M = np.zeros((3,4))
    M[0:3,0:3] = R
    M[:,3] = t
    return M

