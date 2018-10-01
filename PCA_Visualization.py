# 0: season
# 1: year
# 2: month
# 3: holiday
# 4: weekday
# 5: workingday
# 6: weather
# 7: temp
# 8: atemp
# 9: humidity
# 10: windspeed
# 11: casual
# 12: registered
# 13: total bikes

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from data_preparation import *

features = ['season', 'year', 'month', 'holiday', 'weekday', 'workingday', 'weather', 'temp', 'atemp', 'humidity',
            'windspeed', 'casual', 'registered', 'total bikes']

df = pd.DataFrame(X)
df.head()

plt.show()
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(1, 1, 1)
# ax.set_xlabel('Principal Component 1', fontsize=15)
# ax.set_ylabel('Principal Component 2', fontsize=15)
# ax.set_title('2 component PCA', fontsize=20)
# targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
# colors = ['r', 'g', 'b']
# for target, color in zip(targets, colors):
#     indicesToKeep = finalDf['target'] == target
#     ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
#                , finalDf.loc[indicesToKeep, 'principal component 2']
#                , c=color
#                , s=50)
# ax.legend(targets)
# ax.grid()
