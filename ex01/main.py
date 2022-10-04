
from helpers.projections import projects_point, create_transformation_matrix
from helpers.generators import create_grid

import numpy as np
import pandas as pd
from PIL import Image
import math

##### IO #####

# Read camera pose data
poses = pd.read_csv('data/poses.txt', sep=' ', header=None)

# Read Camera Projection Matrix
camera_K = pd.read_csv('data/K.txt', sep=' ', header=None)
K = camera_K.to_numpy()

camera_D = pd.read_csv('data/D.txt',  sep=' ', header=None)
D = camera_D.to_numpy()

# Generate grid
cornerA = [0.5, 0.5, 0.0]
cornerB = [1.5, 1.5, 0.0]
# Each row is a point
points_world = create_grid([3, 3], cornerA, cornerB )


##### Rendering ######

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig = plt.figure()
ax = fig.add_subplot(111)

# Init plots
img = Image.open('data/images/img_0001.jpg')
img.convert("1")
imgplot = plt.imshow(img)
scatter = plt.scatter([0,0],[1,1])

for i in range(1,100):
    # Read image
    path = 'data/images/img_' + str(i).zfill(4) + '.jpg'
    img = Image.open(path)
    # Convert to BW image
    img.convert("1")

    # create camera transformation matrix   
    omega = poses.iloc[[i]].to_numpy()[:,0:3].flatten()
    t = poses.iloc[[i]].to_numpy()[:,3:6].flatten()
    M = create_transformation_matrix(omega, t)

    world_to_uv = np.matmul(K, M)
    uvs = np.matmul(world_to_uv, points_world.T).T

    scatter.set_offsets(uvs[:,0:2])
    imgplot.set_data(img)
    fig.canvas.draw()
    plt.pause(0.1)

plt.show()