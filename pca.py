from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show, xticks, legend
from scipy.linalg import svd
import numpy as np
from data_preparation import X, attribute_names
from variance import XX, N
from mpl_toolkits.mplot3d import Axes3D


Y = XX - np.ones((N,1))*XX.mean(axis=0)
# normalization
Y = Y/Y.std(axis=0)

U,S,V = svd(Y,full_matrices=False)
V = V.T

Z = Y @ V

i = 0
j = 1
l = 2



y = np.asarray(X[:,0])
C = len(set(y))

seasons = ["spring", "summer", "fall", "winter"];
f = figure()
title('NanoNose data: PCA')
# ax = f.gca(projection='3d')
fig = figure()
ax = fig.add_subplot(111, projection='3d')
# Z = Z.tolist()
for c in range(1,C+1):
    # select indices belonging to class c:
    class_mask = y==c
    # plot(Z[class_mask,i], Z[class_mask,j],"o")
    ax.scatter(Z[class_mask,i], Z[class_mask,j], Z[class_mask,l])

legend(seasons)
# xlabel('PC{0}'.format(i+1))
# ylabel('PC{0}'.format(j+1))
ax.set_xlabel('PC{0}'.format(i+1))
ax.set_ylabel('PC{0}'.format(j+1))
ax.set_zlabel('PC{0}'.format(l+1))

# Output result to screen
show()