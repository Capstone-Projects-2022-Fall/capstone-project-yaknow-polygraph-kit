import matplotlib
matplotlib.use('TKAgg')
from matplotlib import pyplot as plt
import numpy as np
import csv
import matplotlib.animation as animation
import datetime
import time
from matplotlib.widgets import Slider
import conductExamScreen
import graphResults
global graph0
global graph1
global graph2
global graph3
global slider_position




def createGraphs():
    '''
    Purpose:
       Create and display all of the data recorded from all of the devices, each with their own subplot but sharing the same time domain.

    Pre-conditions:
        The exam must have been conducted and completed.

    Post-conditions:
        None.

    Parameters and data types:
        conductExamScreen.respirationRecordings, conductExamScreen.skinConductivityRecordings, conductExamScreen.pulseRecordings, conductExamScreen.bloodPressureRecordings - Array of singularRecording class instance

    Return value and output variables:
        graph1, graph2, graph3 - MatPlotLib Subplot

    Exceptions thrown:
        None.
    '''
    
    fig, (graphResults.graph0, graphResults.graph1, graphResults.graph2, graphResults.graph3) = plt.subplots(nrows=4, ncols=1, sharex=True)
    plt.subplots_adjust(bottom=0.25)

    axis_position = plt.axes([0.25, 0.1, 0.65, 0.03])
    graphResults.slider_position = Slider(axis_position, 'Pos', valmin=0, valmax=100, valstep=1)

    #fig.subplots_adjust(hspace=0)

    GSRMeasurement = []
    GSRTime = []
    RespirationMeasurement = []
    RespirationTime = []
    bloodPressureMeasurement = []
    bloodPressureTime = []
    pulseRateMeasurement = []
    pulseRateTime = []

    # with open('TestData.csv', 'r') as csvfile:
    #    lines = csv.reader(csvfile, delimiter=',')
    #    for row in lines:
    #        x.append(row[0])
    #        y.append(int(row[1]))

    for respirationRecording in conductExamScreen.respirationRecordings:
        RespirationMeasurement.append(respirationRecording.measurement)
        RespirationTime.append(respirationRecording.timestamp)

    graphResults.graph0.plot(RespirationTime, RespirationMeasurement, color='b', marker='o')
    graphResults.graph0.set_ylabel("Respiration")

    for skinConductivityRecording in conductExamScreen.skinConductivityRecordings:
        GSRMeasurement.append(skinConductivityRecording.measurement)
        GSRTime.append(skinConductivityRecording.timestamp)

    graphResults.graph1.plot(GSRTime, GSRMeasurement, color='k', marker='o')
    graphResults.graph1.set_ylabel("Siemens")

    print("BP Collections: ", len(conductExamScreen.bloodPressureRecordings))
    for bloodPressureRecording in conductExamScreen.bloodPressureRecordings:
        bloodPressureMeasurement.append(bloodPressureRecording.measurement)
        bloodPressureTime.append(bloodPressureRecording.timestamp)

    graphResults.graph2.plot(bloodPressureTime, bloodPressureMeasurement, color='k', marker='o')
    graphResults.graph2.set_ylabel("Blood Pressure")

    print("Pulse Rate Collections: ", len(conductExamScreen.pulseRecordings))
    for pulseRateRecording in conductExamScreen.pulseRecordings:
        pulseRateMeasurement.append(pulseRateRecording.measurement)
        pulseRateTime.append(pulseRateRecording.timestamp)

    graphResults.graph3.plot(pulseRateTime, pulseRateMeasurement, color='k', marker='o')
    graphResults.graph3.set_ylabel("Pulse Rate")

    # runs through a loop of each question timestamp and prints a red line indicating the data for the question
    #for i in conductExamScreen.questionTime:
        # plt.annotate('question %s' % i+1, xy=(conductExamScreen.questionTime[i], .03), arrowprops=dict(arrowstyle='-', connectionstyle='arc3,rad=0'),
        #              xytext=(85, .01))
    #    plt.axhline(conductExamScreen.questionTime[i], ymin=0, ymax=1, color='red')
    #    plt.text(conductExamScreen.questionTime[i], .1, "question %s" % i + 1, horizontalalignment='center',
    #             verticalalignment='center', transform=plt.transAxes)

    # plt.annotate('question 1', xy=(85, .03), arrowprops=dict(arrowstyle='-', connectionstyle='arc3,rad=0'),
    #              xytext=(85, .01))
    # plt.annotate('question 2', xy=(105.03, .02986), arrowprops=dict(arrowstyle='-', connectionstyle='arc3,rad=0'),
    #              xytext=(105.03, .01))
    # conductExamScreen.questionTime[0]


'''
    graph2.plot(x, y, color='g', marker='o')
    graph2.set_ylabel("Respiration")
    graph3.plot(x, y, color='b', marker='o')
    graph3.set_ylabel("BPM")

    graph3.set_xlabel("Time (seconds)")
'''

def update(val):
    '''
    Purpose:
       Updates the scope of view in the end-of-exam graph when the user moves the scroll bar.

    Pre-conditions:
        The exam must have been conducted and completed, as well as an internet connection before completion.

    Post-conditions:
        None.

    Parameters and data types:
        graphResults.graph3 - MatPlotLib subplot

    Return value and output variables:
        graphResults.fig.canvas - MatPlotLib Canvas

    Exceptions thrown:
        None.
    '''
    
    current_value = graphResults.slider_position.val

    graph3.axis([current_value, current_value + 10, 0, 100])
    graphResults.fig.canvas.draw()

#ani = animation.FuncAnimation(fig, animate, fargs=(x, y), interval=1000)

# createGraphs()
# slider_position.on_changed(update)

#plt.show()


