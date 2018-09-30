import numpy as np
from data_preparation import *


print(attribute_names)

var = X[:,14]
print()
var = sorted(var)


print("records no: %d" % len(var))
print("median: %f" % np.median(var))
print("mean: %f" %np.mean(var))
print("standard deviation: %f" % np.std(var))

print("min var: %f" % var[0])
print("max var: %f" % var[730])
