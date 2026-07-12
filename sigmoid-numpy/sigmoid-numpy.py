import numpy as np

def sigmoid(x):
  """
  Vectorized sigmoid function.
  """
  # Write code here
  arr = np.asarray(x, dtype=float)
  return 1 / (1 + np.exp(-arr))