import numpy as np
from scipy import signal


def harris(img, patch_size, kappa):
    """ Returns the harris scores for an image given a patch size and a kappa value
        The returned scores are of the same shape as the input image """
 
    sobel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])

    I_x = signal.convolve2d(img, sobel_x, mode='same')
    I_y = signal.convolve2d(img, sobel_y, mode='same')

    I_xx = I_x**2
    I_yy = I_y**2
    I_xy = I_x*I_y

    sum_xx = signal.convolve2d(I_xx, np.ones([patch_size, patch_size]), mode='same')
    sum_yy = signal.convolve2d(I_yy, np.ones([patch_size, patch_size]), mode='same')
    sum_xy = signal.convolve2d(I_xy, np.ones([patch_size, patch_size]), mode='same')

    det = sum_xx*sum_yy - sum_xy**2

    trace = sum_xx + sum_yy

    harris_score =  det - kappa * trace**2

    harris_score[0:patch_size//2, :] = 0
    harris_score[-patch_size//2:, :] = 0
    harris_score[:, 0:patch_size//2] = 0
    harris_score[:, -patch_size//2:] = 0

    return harris_score


