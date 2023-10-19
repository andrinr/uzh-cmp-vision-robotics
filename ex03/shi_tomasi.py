import numpy as np
from scipy import signal

def shi_tomasi(img, patch_size):
    """ Returns the shi-tomasi scores for an image and patch size patch_size
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

    M = np.array([[sum_xx, sum_xy], [sum_xy, sum_yy]])
    M = np.moveaxis(M, [0, 1], [-2, -1])
    eigvals = np.linalg.eigvalsh(M)
    print(eigvals.shape)
    shi_tomasi_score = np.min(eigvals, axis=-1)

    shi_tomasi_score[0:patch_size//2, :] = 0
    shi_tomasi_score[-patch_size//2:, :] = 0
    shi_tomasi_score[:, 0:patch_size//2] = 0
    shi_tomasi_score[:, -patch_size//2:] = 0

    return shi_tomasi_score






    

    




