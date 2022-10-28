#This is a layout on how z-test works
#z-test takes means of baseline and problematic and then the square root of the standard deviation squared for both


# If the Z-statistic is less than 2, the two samples are the same.
# 
# If the Z-statistic is between 2.0 and 2.5, the two samples are marginally different
# 
# If the Z-statistic is between 2.5 and 3.0, the two samples are significantly different
# 
# If the Z-statistic is more then 3.0, the two samples are highly signficantly different

import math


# baselineMean = mean value of baseline
# problematicMean = mean value of problematic
#
# baselineDeviation = ((standard deviation of baseline / sqrt(number of baseline data points))^2)
# problematicDeviation = ((standard deviation of baseline / sqrt(number of baseline data points))^2)

baselineMean = 51.5
problematicMean = 39.5
baselineDeviation = 8
problematicDeviation = 7
baselineDataPoints = 25
problematicDataPoints = 25

baselineOmega = ((baselineDeviation / (math.sqrt(baselineDataPoints))))
problematicOmega = ((problematicDeviation / (math.sqrt(problematicDataPoints))))

# print(baselineOmega)
# print(problematicOmega)
# print(baselineOmega**2)
# print(problematicOmega**2)
# print(math.sqrt(baselineOmega**2 + problematicOmega**2))
# print((baselineMean - problematicMean)/math.sqrt(baselineOmega**2 + problematicOmega**2))
# print(baselineMean - problematicMean)
# print(baselineOmega**2 + problematicOmega**2)


z_test = (baselineMean - problematicMean)/(math.sqrt(baselineOmega**2 + problematicOmega**2))

print(z_test)

