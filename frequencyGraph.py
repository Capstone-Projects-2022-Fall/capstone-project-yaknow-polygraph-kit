import csv
from matplotlib import pyplot as plt
import conductExamScreen
from collections import Counter
import numpy as np
import conductExamScreen


def createFrequencyGraphs():
    fig, (graph0, graph1, graph2, graph3) = plt.subplots(nrows=4, ncols=1)
    fig.tight_layout()
    plt.subplots_adjust(bottom=0.25)

    binwidthRespiration = .2
    binwidthGSR = .2
    binwidthBP = .2
    binWidthPulse = .2

    GSRMeasurement = []
    RespirationMeasurement = []
    BloodPressureMeasurement = []
    PulseMeasurement = []

    for respirationRecording in conductExamScreen.respirationRecordings:
        RespirationMeasurement.append(respirationRecording.measurement)

    graph0.hist(RespirationMeasurement, bins=np.arange(min(RespirationMeasurement), max(RespirationMeasurement) + binwidthRespiration, binwidthRespiration), color='blue', edgecolor='black')
    graph0.set_xlabel("Respiration")

    for skinConductivityRecording in conductExamScreen.skinConductivityRecordings:
         GSRMeasurement.append(skinConductivityRecording.measurement)

    graph1.hist(GSRMeasurement, bins=np.arange(min(GSRMeasurement), max(GSRMeasurement) + binwidthGSR, binwidthGSR), color='green', edgecolor='black')
    graph1.set_xlabel("Siemens")

    for bloodPressureRecording in conductExamScreen.bloodPressureRecordings:
         BloodPressureMeasurement.append(bloodPressureRecording.measurement)

    graph2.hist(BloodPressureMeasurement, bins=np.arange(min(BloodPressureMeasurement), max(BloodPressureMeasurement) + binwidthBP, binwidthBP), color='green', edgecolor='black')
    graph2.set_xlabel("Blood Pressure")

    for pulseRecording in conductExamScreen.pulseRecordings:
         PulseMeasurement.append(pulseRecording.measurement)

    graph3.hist(PulseMeasurement, bins=np.arange(min(PulseMeasurement), max(PulseMeasurement) + binWidthPulse, binWidthPulse), color='green', edgecolor='black')
    graph3.set_xlabel("Pulse Rate")

    graph0.set_ylabel("Frequency")
    graph1.set_ylabel("Frequency")
    graph2.set_ylabel("Frequency")
    graph3.set_ylabel("Frequency")

'''
    for bloodPressureRecording in conductExamScreen.bloodPressureRecordings:
        print(bloodPressureRecording.measurement[0])
        bloodPressureMeasurement.append(bloodPressureRecording.measurement[0])   
    
    graph2.hist(BPMEASUREMENT, bins=np.arange(min(GSRMeasurement), max(GSRMeasurement) + binwidthBP, binwidthBP), color='pink', edgecolor='black')
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

#createFrequencyGraphs()

#plt.show()