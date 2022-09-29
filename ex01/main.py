##### IO
from helpers import projects_point, create_transformation_matrix
import numpy as np
import pandas as pd
from PIL import Image
import math
# Read image
img = Image.open('data/images_undistorted/img_0001.jpg')
img.convert("1")

# Read pose data
poses=pd.read_csv('data/poses.txt', sep=' ', header=None)
points = np.ones((4,2))
#points[0:3,0] = poses.iloc[[0]].to_numpy()[:,0:3]
#points[0:3,1] = poses.iloc[[0]].to_numpy()[:,3:6]

# Read Camera data
camera_K = pd.read_csv('data/K.txt', sep=' ', header=None)
K = camera_K.to_numpy()

w = poses.iloc[[0]].to_numpy()[:,0:3]
t = poses.iloc[[0]].to_numpy()[:,3:6]
M = create_transformation_matrix(w, t)


##### Processing

##### RENDERING
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

imgplot = plt.imshow(img)
plt.scatter(uv[0,:], uv[1,:])
plt.show()