import numpy as np
import statistics
import math
import logging
from PIL import Image, ImageTk
import datetime

import PolygraphExamSetupScreen

import IndividualDeviceScreen

import conductExamScreen

from statsmodels.stats.weightstats import ztest as ztest

from respirationBelt import *







def conductZtest():
    '''
    This function will return the z and p values from comparing a problematic question to a baseline
    needs baselineData array/list and ProblematicQuestionData as input

    :return list of (z value, p value), also prints out a statement if we have reasonable evidence to show that someone is lying
    '''
    # baselineData = [baselineData]
    # problematicData = [problematicData.currentQuestion]
    # zTest = list(ztest(baselineData, problematicData.currentQuestion))
    # if conclusion[1] < .05:
    #     print("we reject the null hypothesis, we have reason to believe this data is fairly different... could be lying")
    # else:
    #     print("We do not have reason to believe the data has any major differences")



