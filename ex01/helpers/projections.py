import numpy as np
import math

def projects_points(points_wordl, K, M):

    world_to_uv = np.matmul(K, M)
    points_uv = np.matmul(world_to_uv, points_wordl.T)

    points_uv /= points_uv[2,:]
    points_uv = points_uv.T

    return points_uv


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


def distort(uvs, D, K):
    k1, k2 = D[0], D[1]
    u0, v0 = K[0,2], K[1,2]

    dist_u = (uvs[:,0] - u0)
    dist_v = (uvs[:,1] - v0)

    radial =  dist_u** 2 + dist_v ** 2
    factor = 1 + k1 * radial + k2 * radial ** 2 

    u_d = dist_u * factor + u0
    v_d = dist_v * factor + v0

    return np.stack([u_d, v_d], axis = -1)


def undistort_img(img, D, K):
    img_data = np.asarray(img)
    height, width = img_data.shape[-2:]
    X, Y = np.meshgrid(np.arange(width), np.arange(height))
    px_locs = np.stack([X, Y], axis=-1).reshape([height*width, 2])

    dist_px_locs = distort(px_locs, D, K)
    print(np.max(dist_px_locs))
    intensity_vals = img_data[np.floor(dist_px_locs[:, 1]).astype(np.int),
                         np.floor(dist_px_locs[:, 0]).astype(np.int)]
    undimg = intensity_vals.reshape(img_data.shape).astype(np.uint8)

    return undimg