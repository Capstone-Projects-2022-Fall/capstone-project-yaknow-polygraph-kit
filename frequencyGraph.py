from matplotlib import pyplot as plt
import conductExamScreen
from collections import Counter

fig, (graph0, graph1, graph2, graph3) = plt.subplots(nrows=4, ncols=1, sharex=True)
plt.subplots_adjust(bottom=0.25)

def createGraphs():
    GSRMeasurement = []
    GSRTime = []
    RespirationMeasurement = []
    RespirationTime = []

    Counter(RespirationMeasurement).keys()
    Counter(RespirationMeasurement).values()

    graph0.plot(RespirationTime, RespirationMeasurement, color='b', marker='o')
    graph0.set_ylabel("Respiration")

    Counter(GSRMeasurement).keys()
    Counter(GSRMeasurement).values()

    graph1.plot(GSRTime, GSRMeasurement, color='k', marker='o')
    graph1.set_ylabel("Siemens")

'''
    graph2.plot(x, y, color='g', marker='o')
    graph2.set_ylabel("Respiration")

    graph3.plot(x, y, color='b', marker='o')
    graph3.set_ylabel("BPM")
'''