import numpy as np
import matplotlib
from scipy.stats import norm
import statistics

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.matplotlib.MatplotlibDeprecationWarning)


cityA = [82, 84, 85, 89, 91, 91, 92, 94, 99, 99,
         105, 109, 109, 109, 110, 112, 112, 113, 114, 114]

cityB = [90, 91, 91, 91, 95, 95, 99, 99, 108, 109,
         109, 114, 115, 116, 117, 117, 128, 129, 130, 133]

max_val1 = cityA[0]
for check in cityA:
    if check > max_val1:
        max_val1 = check

min_val1 = cityA[0]
for check in cityA:
    if check < min_val1:
        min_val1 = check

# extraticks=[102, 97, 92]
#
#
# plt.xticks(list(plt.xticks()[0]) + extraticks)



plt.hist(cityA, bins=np.arange(min_val1, max_val1+1))
plt.xlabel("Data Points of Device for current question")
plt.ylabel("Frequency")

plt.show()


#Example


# max_val1 = currentQuestionData[0]
# for check in currentQuestionData:
#     if check > max_val1:
#         max_val1 = check
# 
# min_val1 = currentQuestionData[0]
# for check in currenQuestionData:
#     if check < min_val1:
#         min_val1 = check


# plt.hist(currentQuestionData, bins=np.arange(min_val1, max_val1+1))
