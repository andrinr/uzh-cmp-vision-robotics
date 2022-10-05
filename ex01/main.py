
from helpers.projections import distort, projects_points, create_transformation_matrix, undistort_img
from helpers.generators import create_cube, create_grid

# Computations
import numpy as np
import pandas as pd
from PIL import Image
import math

# Plotting
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read camera pose data
poses = pd.read_csv('data/poses.txt', sep=' ', header=None)

# Read Camera Projection Matrix
camera_K = pd.read_csv('data/K.txt', sep=' ', header=None)
K = camera_K.to_numpy()

camera_D = pd.read_csv('data/D.txt',  sep=' ', header=None)
D = np.loadtxt('data/D.txt')

# Generate grid
cornerA = [0.5, 0.5, 0.0]
cornerB = [1.5, 1.5, 0.0]
# Each row is a point
grid_world = create_grid([8, 6], 0.04)
cube_world = create_cube(0.1)

fig = plt.figure()
ax = fig.add_subplot(111)

# Init plots
img = Image.open('data/images/img_0001.jpg')
img.convert("1")
imgplot = plt.imshow(img)
scatter_grid = plt.scatter([0,0],[1,1])
scatter_cube = plt.scatter([0,0],[1,1])

for i in range(1,100):
    # Read image
    path = 'data/images/img_' + str(i).zfill(4) + '.jpg'
    img = Image.open(path)
    # Convert to BW image
    img.convert("1")

    # Create camera transformation matrix   
    omega = poses.iloc[[i]].to_numpy()[:,0:3].flatten()
    t = poses.iloc[[i]].to_numpy()[:,3:6].flatten()
    M = create_transformation_matrix(omega, t)

    # Apply transformation
    grid_uv = projects_points(grid_world, K, M)
    cube_uv = projects_points(cube_world, K, M)

    # Account for lens distortion
    grid_uv_d = distort(grid_uv, D, K)
    cube_uv_d = distort(cube_uv, D, K)
    img_u = undistort_img(img, D, K)

    # Update plots
    scatter_grid.set_offsets(grid_uv_d[:,0:2])
    scatter_cube.set_offsets(cube_uv_d[:,0:2])
    imgplot.set_data(img_u)
    fig.canvas.draw()
    plt.pause(0.1)

plt.show()