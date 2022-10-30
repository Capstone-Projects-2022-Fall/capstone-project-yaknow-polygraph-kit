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

# # Plot between -10 and 10 with .001 steps.
# x_axis = np.arange(-20, 20, 0.01)
#
# # Calculating mean and standard deviation
# mean = statistics.mean(x_axis)
# sd = statistics.stdev(x_axis)
#
# plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
# plt.show()

max = 0
lowest = 100000

# for i in cityA:
#     if list[i] > max:
#         list[i] = max
# for i in cityA:
#     if list[i] < min:
#         list[i] = min

max_val1 = cityA[0]
for check in cityA:
    if check > max_val1:
        max_val1 = check

min_val1 = cityA[0]
for check in cityA:
    if check < min_val1:
        min_val1 = check

max_val2 = cityB[0]
for check in cityA:
    if check > max_val2:
        max_val2 = check

min_val2 = cityB[0]
for check in cityA:
    if check < min_val2:
        min_val2 = check


        # Plot between -10 and 10 with .001 steps.
x1_axis = np.arange(min_val1,max_val1,1)
x2_axis = np.arange(min_val2,max_val2,1)

# Calculating mean and standard deviation
mean1 = statistics.mean(cityA)
sd1 = statistics.stdev(cityA)

mean2 = statistics.mean(cityB)
sd2 = statistics.stdev(cityB)

plt.plot(cityA, norm.pdf(cityA, mean1, sd1), 'r')
plt.annotate('question 1',xy=(85,.03),arrowprops=dict(arrowstyle='-',connectionstyle='arc3,rad=0'),xytext=(85,.01))
plt.annotate('question 2',xy=(105.03,.02986),arrowprops=dict(arrowstyle='-',connectionstyle='arc3,rad=0'),xytext=(105.03,.01))

plt.show()



#if we have a timestamp:
# plt.annotate('question 1',xy=(timeOfEndOfQuestion,topOfGraphValue),arrowprops=dict(arrowstyle='-',connectionstyle='arc3,rad=0'),xytext=(timeOfEndOfQuestion,.1))




