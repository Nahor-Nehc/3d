import numpy as np
from math import sin, cos
from components.threeDimensionalClasses import orientation, point

STEPONE = lambda theta: np.array(
  [
    [1,               0,            0],
    [0,    cos(theta.x), sin(theta.x)],
    [0, -1*sin(theta.x), cos(theta.x)],
  ]
)

STEPTWO = lambda theta:np.array(
  [
    [cos(theta.y), 0, -1*sin(theta.y)],
    [           0, 1,               0],
    [sin(theta.y), 0,    cos(theta.y)],
  ]
)

STEPTHREE = lambda theta : np.array(
  [
    [   cos(theta.z), sin(theta.z), 0],
    [-1*sin(theta.z), cos(theta.z), 0],
    [              0,            0, 1],
  ]
)
