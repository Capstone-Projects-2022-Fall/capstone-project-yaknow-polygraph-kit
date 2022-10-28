#this is a python z-test that only takes in an array of baseline data and then array of problematic data
# then finds z-test value and corresponding p value
# for our test, if a p value is <.05 then it is reasonable to belive the data is significantly different, i.e they are lying

import numpy as np
import statistics
import math




from statsmodels.stats.weightstats import ztest as ztest


#enter IQ levels for 20 individuals from each city
cityA = [82, 84, 85, 89, 91, 91, 92, 94, 99, 99,
         105, 109, 109, 109, 110, 112, 112, 113, 114, 114]

cityB = [90, 91, 91, 91, 95, 95, 99, 99, 108, 109,
         109, 114, 115, 116, 117, 117, 128, 129, 130, 133]

#perform two sample z-test
conclusion = list(ztest(cityA, cityB))

print(conclusion)

if conclusion[1] < .05:
    print("we reject the null hypothesis, we have reason to believe this data is fairly different... could be lying")
else:
    print("We do not have reason to believe the data has any major differences")



# np.std(cityA)
# np.std(cityB)
#
# x1 = statistics.mean(cityA)
# x2 = statistics.mean(cityB)
#
#
# baselineMean = x1
# problematicMean = x2
# baselineDeviation = np.std(cityA)
# problematicDeviation = np.std(cityB)
# baselineDataPoints = 20
# problematicDataPoints = 20
#
# baselineOmega = ((baselineDeviation / (math.sqrt(baselineDataPoints))))
# problematicOmega = ((problematicDeviation / (math.sqrt(problematicDataPoints))))
#
#
#
# z_test = (baselineMean - problematicMean)/(math.sqrt(baselineOmega**2 + problematicOmega**2))
#
# print(z_test)