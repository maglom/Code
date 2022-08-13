import random


values = [2,3,535,23,62,63,7,53,43,5,23,52,6,347,73,78,34,2,34,242,37,54,6,9,760]

alpha = 0.1

values.sort()

lower_idx = round(len(values) * alpha / 2)


upper_idx = round(len(values) * (1 - alpha / 2)) - 1

print('Lower values = ', values[:lower_idx], 'Upper values = ', values[upper_idx:])

