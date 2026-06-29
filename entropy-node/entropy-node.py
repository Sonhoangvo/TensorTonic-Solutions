import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y) == 0 : return 0.0
    entropy = 0
    counts = np.unique(y, return_counts = True)
    
    for i in counts[1]:
        print(i)
        if i > 0:
            entropy -= (i/len(y)) * np.log2(i/len(y))
    return entropy