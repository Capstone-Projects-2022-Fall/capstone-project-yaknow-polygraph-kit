import csv
from matplotlib import pyplot as plt
import conductExamScreen
from collections import Counter
import numpy as np

fig, (graph0, graph1, graph2, graph3) = plt.subplots(nrows=4, ncols=1, sharex=True)
plt.subplots_adjust(bottom=0.25)

binwidth = 10

def createFrequencyGraphs():
    GSRMeasurement = []
    GSRTime = []
    RespirationMeasurement = []
    RespirationTime = []

    #graph0.hist(RespirationMeasurement, bins=range(min(RespirationMeasurement), max(RespirationMeasurement) + binwidth, binwidth), color='blue', edgecolor='black')
    graph0.set_ylabel("Respiration")

    #graph1.hist(GSRMeasurement, bins=range(min(GSRMeasurement), max(GSRMeasurement) + binwidth, binwidth), color='green', edgecolor='black')
    graph1.set_ylabel("Siemens")

'''
    graph2.hist(BPMEASUREMENT, bins=range(min(BPMEASUREMENT), max(BPMEASUREMENT) + binwidth, binwidth), color='pink', edgecolor='black')
    graph2.set_ylabel("Blood Pressure")

    graph3.hist(HEARTRATEMEASUREMENT, bins=range(min(HEARTRATEMEASUREMENT), max(HEARTRATEMEASUREMENT) + binwidth, binwidth), color='orange', edgecolor='black')
    graph3.set_ylabel("BPM")
    
    graph3.set_xlabel("Frequency")
'''

# x = []
# y = []
#
# with open('TestData.csv', 'r') as csvfile:
#     lines = csv.reader(csvfile, delimiter=',')
#     for row in lines:
#         x.append(row[0])
#         y.append(int(row[1]))
#
# binwidth = 10
#
# graph0.hist(y, bins=range(min(y), max(y) + binwidth, binwidth), color='blue', edgecolor='black')
# graph1.hist(y, bins=range(min(y), max(y) + binwidth, binwidth), color='green', edgecolor='black')
# graph2.hist(y, bins=range(min(y), max(y) + binwidth, binwidth), color='pink', edgecolor='black')
# graph3.hist(y, bins=range(min(y), max(y) + binwidth, binwidth), color='orange', edgecolor='black')

createFrequencyGraphs()

plt.show()