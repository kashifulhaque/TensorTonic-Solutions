import numpy as np

def entropy_node(y):
  """
  Compute entropy for a single node using stable logarithms.
  """
  # Write code here
  y = np.asarray(y, dtype=float)
  if len(y) == 0:
    return 0.0

  _, counts = np.unique(y, return_counts=True)
  probas = counts / len(y)
  probas = probas[probas > 0]

  return -np.sum(probas * np.log2(probas))
