import numpy as np
def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype = float)
    y_pred = np.asarray(y_pred, dtype = float)
    bins = np.linspace(0,1, n_bins+1)
    print(bins[1:-1])
    ece = 0 
    print(bins)
    bins_index = np.digitize(y_pred, bins[1:-1], right = False)
    print(bins_index)
    for b in np.unique(bins_index):
        mask = bins_index == b
        acc = y_true[mask].mean()
        conf = y_pred[mask].mean()
        ece += mask.sum() / len(y_true) * abs(acc - conf)
    return ece 
