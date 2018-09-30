import csv
import numpy as np
from matplotlib.pylab import figure, plot, subplot, xlabel, ylabel, hist, show
from scipy import stats

datasetpath = "../Bike-Sharing-Dataset"

file = open(datasetpath + "/day.csv")
daydata = csv.reader(file, delimiter=',')

row1 = next(daydata)

attribute_names = [row1[0]] + row1[2:]
X = []
for row in daydata:
    X.append([row[0]] + row[2:])

X = np.array(X).astype(float)
print(attribute_names)

print((np.median(X[:, 11])))
print((np.std(X[:, 11])))
print(np.mean(X[:,11]))


# figure()
#
# plot(X[:10,9],X[:10,15],'.')
#
# show()









