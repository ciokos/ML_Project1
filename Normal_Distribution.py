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


from data_preparation import *
import seaborn as sns, numpy as np
import matplotlib.pyplot as plt

data = []
for row in X:
    data.append(row[8])

data = np.array(data).astype(float)
data.sort()

ax = sns.distplot(data, hist=True, norm_hist=True)

plt.show()
