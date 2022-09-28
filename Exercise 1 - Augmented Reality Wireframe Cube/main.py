import numpy as np
import pandas as pd
import imageio as iio

##### READ IMAGE
img = iio.imread('data/images_undistorted/img_0001.jpg')
img_gray = np.dot(img, [1, 1, 1])
img_gray = np.round(img_gray).astype(np.uint8)
img_gray = np.stack([img_gray] * 3, axis=-1)

##### READ POSES
poses=pd.read_csv('data/poses.txt', sep=' ', header=None)
p_upper = poses.iloc[[0]].to_numpy()[0:3]
p_lower = poses.iloc[[0]].to_numpy()[3:6]


