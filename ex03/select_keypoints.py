import numpy as np


def selectKeypoints(scores, num, r):
    """
    Selects the num best scores as keypoints and performs non-maximum supression of a (2r + 1)*(2r + 1) box around
    the current maximum.
    """
    pass
    # TODO: Your code here

    keypoints = np.zeros((2, num))

    for i in range(num):
        max_index = np.argmax(scores)
        x = max_index // scores.shape[1]
        y = max_index % scores.shape[1]
        
        scores[max(0, x - r):min(scores.shape[0], x + r + 1), max(0, y - r):min(scores.shape[1], y + r + 1)] = 0

        keypoints[0, i] = x
        keypoints[1, i] = y

    return keypoints