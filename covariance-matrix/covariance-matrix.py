import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X, dtype = float)
    if X.ndim < 2 or len(X) == 1: return None
    mean = np.mean(X, axis = 0)
    center = X - mean 
    return (1/(len(X)-1)) * (np.transpose(center) @ center)