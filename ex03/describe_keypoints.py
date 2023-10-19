import numpy as np


def describeKeypoints(img, keypoints, r):
    """
    Returns a (2r+1)^2xN matrix of image patch vectors based on image img and a 2xN matrix containing the keypoint
    coordinates. r is the patch "radius".
    """
    N = keypoints.shape[1]
    keypoint_patches = np.zeros(((2 * r + 1) ** 2, N))

    # add padding
    img = np.pad(img, r, 'constant', constant_values=0)
    
    for i in range(N):
        x = keypoints[0, i] + r
        y = keypoints[1, i] + r
        
        keypoint_patches[:, i] = img[int(x-r):int(x+r+1), int(y-r):int(y+r+1)].flatten()
    
    return keypoint_patches


