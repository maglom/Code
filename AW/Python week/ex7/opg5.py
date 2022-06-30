

def quantile(series, alpha=0.05)-> int:
    """returns upper and lower index 

    Args:
        series (int): number of observations
        alpha (float, optional): alpha value. Defaults to 0.05.

    Returns:
        int: returns upper and lower index
    """
    lower_idx = round(series * alpha / 2)
    upper_idx = round(series * (1 - alpha / 2)) - 1

    return upper_idx, lower_idx

values = [2,3,535,23,62,63,7,53,43,5,23,52,6,347,73,78,34,2,34,242,37,54,6,9,760]

alpha = 0.1

values.sort()

idx = quantile(len(values), alpha)

print('Lower values = ', values[:idx[1]], 'Upper values = ', values[idx[0]:])


