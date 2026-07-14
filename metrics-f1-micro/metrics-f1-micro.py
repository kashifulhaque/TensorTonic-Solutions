import numpy as np

def f1_micro(y_true, y_pred) -> float:
  """
  Compute micro-averaged F1 for multi-class integer labels.
  """
  # Write code here
  y_true = np.asarray(y_true, dtype=float)
  y_pred = np.asarray(y_pred, dtype=float)

  tp = np.sum(y_true == y_pred)
  n = len(y_true)

  fp = fn = n - tp
  return float((2 * tp) / (2 * tp + fp + fn))
