from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show, xticks
from scipy.linalg import svd
import numpy as np
from data_preparation import X, attribute_names

N = 731
print(attribute_names)
XX = np.array(X)
XX = np.delete(XX,1,1)
XX = np.delete(XX,range(2,5),1)
print(XX[1])


Y = XX - np.ones((N,1))*XX.mean(axis=0)
Y = Y/Y.std(axis=0)

U,S,V = svd(Y,full_matrices=False)


# Compute variance explained by principal components
rho = (S*S) / (S*S).sum()

# Plot variance explained
rsum = [rho[0]];
for i in range(1,len(rho)):
    rsum.append(rsum[i-1] + rho[i])
figure()
plot(range(1,len(rsum)+1),rsum,'o-')
xticks(range(1,len(rsum)+1))
title('Variance explained by number of principal components included');
xlabel('Number of Principal components included');
ylabel('Variance explained');
show()