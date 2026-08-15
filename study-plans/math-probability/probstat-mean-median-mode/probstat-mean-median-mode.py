import numpy as np
from collections import Counter

def mean_median_mode(x):
    x = np.array(x)
    mean = float(np.mean(x))
    median = float(np.median(x))

    counts = Counter(x)
    max_fre = max(counts.values())
    mode = min(v for v, fre in counts.items() if fre == max_fre)

    return {
    "mean": mean,
    "median": median,
    "mode": float(mode)
}