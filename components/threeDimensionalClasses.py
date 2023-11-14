import numpy as np

verticalArray = lambda x, y, z: np.array([[x, y, z]]).transpose()

class threeDimensional:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.array = verticalArray(x, y, z)
  
  def get(self):
    return self.x, self.y, self.z
  
  def get_array(self):
    return self.array

class point(threeDimensional):
  def get_coords(self):
    return self.get(self.get)

class orientation(threeDimensional):
  def get_angles(self):
    return self.get(self.get)
