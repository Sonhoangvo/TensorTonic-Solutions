import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.asarray(x, dtype = float)
    mean = np.mean(x)
    x_mean = (x -mean) ** 2
    sum_mean = np.sum(x_mean)
    var = sum_mean / (len(x)-1)
    s = np.sqrt(var)
    return var, s