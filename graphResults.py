from matplotlib import pyplot as plt
import numpy as np
import csv
import matplotlib.animation as animation
import datetime
import time
from matplotlib.widgets import Slider
import conductExamScreen

fig, (graph0, graph1, graph2, graph3) = plt.subplots(nrows=4, ncols=1, sharex=True)
plt.subplots_adjust(bottom=0.25)

axis_position = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_position = Slider(axis_position,'Pos', valmin=0, valmax=100, valstep=1)

fig.subplots_adjust(hspace=0)

def createGraphs():
    GSRMeasurement = []
    GSRTime = []
    RespirationMeasurement = []
    RespirationTime = []
    '''with open('TestData.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))'''

    for respirationRecording in conductExamScreen.respirationRecordings:
        RespirationMeasurement.append(respirationRecording.measurement)
        RespirationTime.append(respirationRecording.timestamp)
    

    graph0.plot(RespirationTime, RespirationMeasurement, color='b', marker='o')
    graph0.set_ylabel("Respiration")


    for skinConductivityRecording in conductExamScreen.skinConductivityRecordings:
        GSRMeasurement.append(skinConductivityRecording.measurement)
        GSRTime.append(skinConductivityRecording.timestamp)

    graph1.plot(GSRTime, GSRMeasurement, color='k', marker='o')
    graph1.set_ylabel("Siemens")
'''
    graph2.plot(x, y, color='g', marker='o')
    graph2.set_ylabel("Respiration")

    graph3.plot(x, y, color='b', marker='o')
    graph3.set_ylabel("BPM")
'''

def update(val):
    current_value = slider_position.val
    graph3.axis([current_value, current_value+10, 0, 100])
    fig.canvas.draw()

#createGraphs()
#slider_position.on_changed(update)

#plt.show()


