import numpy

def mexican_hat(size):
  # a. Create empty matrix
  A = numpy.zeros((size,size))

  # b. Calculate values
  for x in range(-size // 2, (size // 2) + 1):
    for y in range(-size // 2, (size // 2) + 1):
      inner_calc = (x + y) ** 2
      inner_calc = (-1 * inner_calc) / 2
      A[x][y] = numpy.exp(inner_calc)

  # d. Return matrix
  return A

def gaussian(size):
  # a. Define sigma value 
  sigma = 1
  # b. Create empty matrix
  A = numpy.zeros((size,size))

  # c. Calculate values
  for x in range(-size // 2, (size // 2) + 1):
    for y in range(-size // 2, (size // 2) + 1):
      value_1 = (1/(2*numpy.pi*(sigma**2)))
      value_2 = numpy.exp(-((x**2+y**2)/(2*(sigma**2))))
      A[x][y] = value_1 * value_2

  # d. Return matrix
  return A

def sharpen():
  # a. Create sharpen matrix
  A = numpy.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
  
  # b. Return matrix
  return A

def ridge():
  # a. Apply Hessian Matrix
  A = numpy.array([[-1, -1, -1],
                   [-1, 8,-1],
                   [-1, -1, -1]])
  
  # b. Return matrix
  return A


