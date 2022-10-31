import logging
import datetime

import PolygraphExamSetupScreen
import IndividualDeviceScreen
import conductExamScreen

import math
import numpy as np

import time


from scipy.signal import find_peaks

# import numpy as np


with open('polygraphExamKitLogging.log', 'w'):
    pass

log_format = '%(asctime)s %(filename)s - %(levelname)s: %(message)s'
logging.basicConfig(filename='polygraphExamKitLogging.log', level=logging.DEBUG, force=True, format=log_format, datefmt='%H:%M:%S')



def connectBloodPressureDevice():
    from gdx2 import gdx
    theAPIs = gdx()
    connected = False
    while connected == False:
        bloodPressureConnected = theAPIs.open_ble('GDX-BP 141014A2')
        if(bloodPressureConnected == True):
            PolygraphExamSetupScreen.bloodPressureConnected = True
            PolygraphExamSetupScreen.window['theImage1'].update(data=PolygraphExamSetupScreen.checkmarkImage)
            connected = True
        else:
            theAPIs.close()
    while not PolygraphExamSetupScreen.examStarted:
        pass
    print("Starting Exam in BP")
# blood pressure sensor can measure mean arterial pressure, systolic (the maximum), diastolic (minimum)
# Also, sampling rate would be different then the other device, since recording blood pressure will take longer    
    theAPIs.select_sensors([1,7])

    #rate = PolygraphExamSetupScreen.BloodPressureSamplingRate * 1000
    theAPIs.start(100)

    listOfOscillations = []
    possibleBP = []
    maxOsc = 0
    conductExamScreen.inQuestion = False
    # # This continuously reads cuff pressure, until the pressure is above 155 and then it stops reading
    # # Cuff pressure needs to be at least 155 for the device to start reading blood pressure
    # # then when the cuff pressure is around 50, the device spits out your blood pressure measurements (and any other data collected would be printed at this time)
    while conductExamScreen.examFinished == False:
        measurements = theAPIs.read()
        correctPressure = False
        conductExamScreen.inQuestion = False
        if ( (measurements[0] < 150)):
            #conductExamScreen.window['-CuffPressure-'].update(measurements[0])
            print("Paused Measurements: ", measurements[0])
        else:
            conductExamScreen.inQuestion = True
            while correctPressure == False:
                measurements = theAPIs.read()
                print("Recording Measurements: ", measurements[0])
                currentTime = datetime.datetime.now()
                possibleBP.append(measurements)
                listOfOscillations.append(measurements[1])
                if measurements[1] > maxOsc:
                    maxOsc = measurements[1]
                if measurements[0] < 70:
                    print("Less than 70")
                    listt = []
                    for inner_list in (possibleBP):
                        for element in (inner_list):
                            listt.append(element)
                            # if element == maxOsc:
                            #     print("Your mean arterial blood pressure is : " + str(element-1))

                    for index, elem in enumerate(listt):
                        if (index + 1 < len(listt) and index - 1 >= 0):
                            prev_el = str(listt[index - 1])
                            if elem == maxOsc:
                                finalMeasurement = prev_el
                                #print("Your real mean arterial blood pressure is : " + str(prev_el))
                    tempMeasurement = conductExamScreen.singularRecording(currentTime, finalMeasurement,conductExamScreen.newQuestion, conductExamScreen.yn)
                    conductExamScreen.bloodPressureRecordings.append(tempMeasurement)
                    correctPressure = True
                    listOfOscillations = []
                    possibleBP = []


    #t1 = time.time()
    #theAPIs.stop()
    #totalTime = t1 - t0

    #print("Max oscillation is : " + str(maxOsc))

    #print("the time it took to find blood pressure: " + str(totalTime))


    # Creates a list of lists from the measurements, then creats a list of each value going from cuff pressure, oscillation, cuff pressure, oscillation, etc
    # then from there finds the max value of the oscilation, then gets the corresponding cuff pressure, which is mean arterial pressure



    # for i in range(12):
    #     measurements = theAPIs.read()
    #     currentTime = datetime.datetime.now()
    #     if measurements == None:
    #         break
    #     print("Blood Pressure Recordings: ", currentTime, measurements)



def connectBloodPressureDeviceIndividual():
    from gdx import gdx
    theAPIs = gdx()
    connected = False
    while connected == False:
        bloodPressureConnected = theAPIs.open_ble('GDX-BP 141014A2')
        if (bloodPressureConnected == True):
            IndividualDeviceScreen.deviceConnected = True
            IndividualDeviceScreen.window['theImage1'].update(data=IndividualDeviceScreen.checkmarkImage)
            IndividualDeviceScreen.window.refresh()
            connected = True
        else:
            theAPIs.close()
    while not IndividualDeviceScreen.recordingStarted:
        pass

    theAPIs.select_sensors([1])

    times = int(IndividualDeviceScreen.deviceTime / IndividualDeviceScreen.DeviceSamplingRate)
    for i in range(times):
        measurements = theAPIs.read()
        currentTime = datetime.datetime.now()
        if measurements == None:
            break
        print(currentTime, measurements)


