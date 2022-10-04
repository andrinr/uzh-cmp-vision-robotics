import numpy as np
import math

def projects_point(point, K, M):
    # using associativity
    T =  np.matmul(K, M)
    return np.matmul(T, point.T).T

def create_transformation_matrix(omega, t):
    theta = np.linalg.norm(omega)
    k = omega / theta
    #print(w, t, k)
    K = np.array([[0, -k[2], k[1]],
                [k[2], 0, -k[0]],
                [-k[1], k[0], 0]])

    R = np.identity(3) + math.sin(theta) * K +\
        (1 - math.cos(theta)) * np.linalg.matrix_power(K, 2)

    M = np.zeros((3,4))
    M[0:3,0:3] = R
    M[:,3] = t
    return M

