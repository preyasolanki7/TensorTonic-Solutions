import numpy as np

def create_filled_array(shape, kind):
    if kind == "zeros":
        return np.zeros(shape, dtype=np.float64)
    else:
        return np.ones(shape, dtype=np.float64)