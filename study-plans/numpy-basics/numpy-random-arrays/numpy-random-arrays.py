import numpy as np

def generate_random_array(shape, kind, seed):
    rng = np.random.default_rng(seed)
    if kind == "uniform":
        return rng.uniform(0,1,size=shape).astype(np.float64)
    else:
        return rng.normal(0,1,size=shape).astype(np.float64)