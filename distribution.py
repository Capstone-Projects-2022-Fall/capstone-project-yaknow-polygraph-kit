import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics


cityA = [82, 84, 85, 89, 91, 91, 92, 94, 99, 99,
         105, 109, 109, 109, 110, 112, 112, 113, 114, 114]

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

for i in cityA:
    if list[i] > max:
        list[i] = max
for i in cityA:
    if list[i] < min:
        list[i] = min


# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(min,max,1)

# Calculating mean and standard deviation
mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)

plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()