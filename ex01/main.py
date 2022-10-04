
from helpers.projections import projects_point, create_transformation_matrix
from helpers.generators import create_grid

import numpy as np
import pandas as pd
from PIL import Image
import math

##### IO #####

# Read image
img = Image.open('data/images_undistorted/img_0001.jpg')
# Convert to BW image
img.convert("1")

# Read cmaera pose data
poses=pd.read_csv('data/poses.txt', sep=' ', header=None)
points = np.ones((4,2))

# Read Camera Projection Matrix
camera_K = pd.read_csv('data/K.txt', sep=' ', header=None)
K = camera_K.to_numpy()

# create camera transformation matrix
omega = poses.iloc[[0]].to_numpy()[:,0:3].flatten()
t = poses.iloc[[0]].to_numpy()[:,3:6].flatten()
M = create_transformation_matrix(omega, t)


##### Processing ######

# Generate grid
cornerA = [0.0, 0.0, 0.0]
cornerB = [1.0, 1.0, 0]
points = create_grid([10, 10], cornerA, cornerB )
points_camera_space = np.matmul(M, points.T)
uvs = (np.matmul(K, points_camera_space)).T
#print(np.shape(points_camera_space))


##### Rendering #######

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

imgplot = plt.imshow(img)
plt.scatter(uvs[:,0], uvs[:,1])
plt.show()