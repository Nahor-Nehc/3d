import numpy as np
from math import sin, cos, pi
from threeDimensionalClasses import orientation, point

stepone = lambda theta: np.array(
  [
    [1,               0,            0],
    [0,    cos(theta.x), sin(theta.x)],
    [0, -1*sin(theta.x), cos(theta.x)],
  ]
)

steptwo = lambda theta : np.array(
  [
    [cos(theta.y), 0, -1*sin(theta.y)],
    [           0, 1,               0],
    [sin(theta.y), 0,    cos(theta.y)],
  ]
)

stepthree = lambda theta : np.array(
  [
    [   cos(theta.z), sin(theta.z), 0],
    [-1*sin(theta.z), cos(theta.z), 0],
    [              0,            0, 1],
  ]
)

stepfour = lambda point, camera: point.get_array() - camera.get_array()

def camera_transform(camera_orientation:orientation, camera_location:point, object_point:point, display_surface_location:point):
  transformed_point = stepone(camera_orientation).dot(steptwo(camera_orientation)).dot(stepthree(camera_orientation)).dot(stepfour(object_point, camera_location))

  transformed_point = point(transformed_point[0][0], transformed_point[1][0], transformed_point[2][0])
  print(transformed_point.get_array())
  
  e = display_surface_location
  print(e.z, transformed_point.z)
  x = (e.z / transformed_point.z) * transformed_point.x + e.x
  y = (e.z / transformed_point.z) * transformed_point.y + e.y
  
  print(x, y)
  
# class draw():
#   pass

camera_location = point(0, 0, 0)
camera_orientation = orientation(0, 0, 0)
display_surface_location = point(10, 0, 0)
p = point(1, 2, 0)

camera_transform(camera_orientation, camera_location, p, display_surface_location)