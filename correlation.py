from data_preparation import X, attribute_names
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.DataFrame()
indices = [2,7,11,12,13]

print(attribute_names)

# plt.plot(X[:,7],X[:,13], 'o')
# plt.xlabel("normalized temperature")
# plt.ylabel("bikes rented")
# plt.show()

for i in range(len(attribute_names)):
    if(i in indices):
        df[attribute_names[i]] = X[:, i]

print(df.corr())
# pd.plotting.scatter_matrix(df,figsize=(50,50))
#
# plt.show()



