import numpy as np
from data_preparation import *
from matplotlib.pyplot import boxplot, xticks, ylabel, title, show, xlabel


print(attribute_names)

# var = X[:,13]
# var = sorted(var)
#
#
# print("records no: %d" % len(var))
# print("median: %f" % np.median(var))
# print("mean: %f" %np.mean(var))
# print("standard deviation: %f" % np.std(var))
#
# print("min var: %f" % var[0])
# print("max var: %f" % var[730])
#

ws = np.array(X[:,10])
print(np.where(ws == 0.507463))
# indices = [7,9,10,11,12,13]
#
# for i in range(1,len(attribute_names)):
#     if(i in indices):
#         boxplot(X[:,i])
#         xlabel(attribute_names[i])
#         show()
