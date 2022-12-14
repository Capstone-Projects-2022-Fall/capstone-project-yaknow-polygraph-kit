import logging
import datetime

import PolygraphExamSetupScreen
import IndividualDeviceScreen
import conductExamScreen

import math
import numpy as np

import time
import PySimpleGUI as sg


global pressureBar


from scipy.signal import find_peaks
#from ProgressBar import manually_updated_meter_test

# import numpy as np


with open('polygraphExamKitLogging.log', 'w'):
    pass

log_format = '%(asctime)s %(filename)s - %(levelname)s: %(message)s'
logging.basicConfig(filename='polygraphExamKitLogging.log', level=logging.DEBUG, force=True, format=log_format, datefmt='%H:%M:%S')






def connectBloodPressureDevice():
    '''
    Purpose:
        A thread that connects and records blood presssure and pulse data from the Arduino GSR Sensor in a non-blocking way and communicates the stored data with the main thread.

    Pre-conditions:
        Must be started within the context of a polygraph exam.

    Post-conditions:
        Exits the thread upon exam completion.

    Parameters and data types:
        PolygraphExamSetup.window - PySimpleGUI window
        PolygrpahExamSetup.GSRSamplingRate - int
        conductExamScreen.examFinished - boolean
        conductExamScreen.bloodPressureRecordings - Array of singularRecording class instance
        conductExamScreen.bloodPressureTimings - Array of Flaot
        conductExamScreen.bloodPressureMeasurements - Array of float
         conductExamScreen.pulseMeasurements - Array of float
        conductExamScreen.pulseTimings - Array of float

    Return value and output variables:
        conductExamScreen.bloodPressureRecordings - Array of singularRecording class instance
        conductExamScreen.bloodPressureTimings - Array of Flaot
        conductExamScreen.bloodPressureMeasurements - Array of float
         conductExamScreen.pulseMeasurements - Array of float
        conductExamScreen.pulseTimings - Array of float

    Exceptions thrown:
        None.

    '''
    from gdx2 import gdx
    theAPIs = gdx()
    connected = False
    while connected == False:
        if (conductExamScreen.exited):
            connected = True
            print("Changed: ", connected)
            PolygraphExamSetupScreen.examStarted = True
            PolygraphExamSetupScreen.examFinished = True
            theAPIs.close()
        bloodPressureConnected = theAPIs.open_ble('GDX-BP 141014A2')
        if(bloodPressureConnected == True):
            if (conductExamScreen.exited):
                connected = True
                PolygraphExamSetupScreen.examStarted = True
                PolygraphExamSetupScreen.examFinished = True
                theAPIs.close()
            else:
                PolygraphExamSetupScreen.bloodPressureConnected = True
                PolygraphExamSetupScreen.window['theImage1'].update(data=PolygraphExamSetupScreen.checkmarkImage)
                connected = True
        else:
            theAPIs.close()
    while not PolygraphExamSetupScreen.examStarted:
        time.sleep(1)
        pass

    if not conductExamScreen.exited:
        print("Starting Exam in BP")
    # blood pressure sensor can measure mean arterial pressure, systolic (the maximum), diastolic (minimum)
    # Also, sampling rate would be different then the other device, since recording blood pressure will take longer
        theAPIs.select_sensors([1,7])

        #rate = PolygraphExamSetupScreen.BloodPressureSamplingRate * 1000
        theAPIs.start(100)
        print("BloodPressure Started")

        listOfOscillations = []
        possibleBP = []
        maxOsc = 0
        conductExamScreen.inQuestion = False
        # prev = listOfOscillations[0] or 0.001
        threshold = 0.5
        peaks = []

        # for num, i in enumerate(listOfOscillations[1:], 1):
        #     if (i - prev) / prev > threshold:
        #         peaks.append(num)
        #     prev = i or 0.001
        #
        # print(peaks)

        # pulseRate = ((((len(peaks))) / totalTime) * 60)
        # print("The pulse rate is: " + str(pulseRate))
        # # This continuously reads cuff pressure, until the pressure is above 155 and then it stops reading
        # # Cuff pressure needs to be at least 155 for the device to start reading blood pressure
        # # then when the cuff pressure is around 50, the device spits out your blood pressure measurements (and any other data collected would be printed at this time)
        #examStartTime = datetime.datetime.now()
        while conductExamScreen.examFinished == False:
            measurements = theAPIs.read()
            correctPressure = False
            pressureBar = False
            conductExamScreen.inQuestion = False
            progress_bar = conductExamScreen.window['progress']
            print("Not in Question")
            if ((measurements[0] < 150)):
                # measurements1 = theAPIs.read()
                # conductExamScreen.window['-CuffPressure-'].update(measurements[0])
                # print("Paused Measurements: ", measurements[0])
                while pressureBar == False:
                    if (conductExamScreen.examFinished == True):
                        pressureBar = True
                    # make_bloodPressure_bar()
                    # progress_bar1 = sg.window['progress1']
                    measurements1 = theAPIs.read()
                    print("Paused Measurements: ", measurements1[0])
                    if measurements1[0] < 15:
                        print("you made it to 10 percent")
                        progress_bar.update_bar(1)  # show 10% complete
                        # sleep(2)

                    if 16 < measurements1[0] < 30:
                        print("you made it to 20 percent")
                        progress_bar.update_bar(2)  # show 20% complete

                        # sleep(2)
                    if 31 < measurements1[0] < 45:
                        print("you made it to 30 percent")
                        progress_bar.update_bar(3)  # show 30% complete
                        # sleep(2)

                    if 46 < measurements1[0] < 60:
                        print("you made it to 40 percent")
                        progress_bar.update_bar(4)  # show 40% complete
                        # sleep(2)
                    if 61 < measurements1[0] < 75:
                        print("you made it to 50 percent")
                        progress_bar.update_bar(5)  # show 50% complete
                        # sleep(2)

                    if 76 < measurements1[0] < 90:
                        print("you made it to 60 percent")
                        progress_bar.update_bar(6)  # show 60% complete
                        # sleep(2)
                    if 91 < measurements1[0] < 105:
                        print("you made it to 70 percent")
                        progress_bar.update_bar(7)  # show 70% complete
                        # sleep(2)
                    if 106 < measurements1[0] < 120:
                        print("you made it to 80 percent")
                        progress_bar.update_bar(8)  # show 80% complete
                        # sleep(2)
                    if 121 < measurements1[0] > 135:
                        print("you made it to 90 percent")
                        progress_bar.update_bar(9)  # show 90% complete
                        # sleep(2)

                    if measurements1[0] > 150:
                        print("you made it to 100 percent")
                        progress_bar.update_bar(10)  # show 100% complete
                        # time.sleep(.5)
                        # progress_bar.window.close()
                        pressureBar = True
            else:
                beginningTime = datetime.datetime.now()
                conductExamScreen.inQuestion = True
                while correctPressure == False:
                    measurements = theAPIs.read()
                    print("Recording Measurements: ", measurements[0])
     #               currentTime = (datetime.datetime.now() - examStartTime).total_seconds()
                    possibleBP.append(measurements)
                    listOfOscillations.append(measurements[1])
                    if measurements[1] > maxOsc:
                        maxOsc = measurements[1]
                    if measurements[0] < 70:
                        endTime = datetime.datetime.now()
                        print("Less than 70")
                        listt = []
                        prev = listOfOscillations[0] or 0.001
                        for inner_list in (possibleBP):
                            for element in (inner_list):
                                listt.append(element)
                                # if element == maxOsc:
                                #     print("Your mean arterial blood pressure is : " + str(element-1))

                        for index, elem in enumerate(listt):
                            if (index + 1 < len(listt) and index - 1 >= 0):
                                prev_el = listt[index - 1]
                                if elem == maxOsc:
                                    finalMeasurement = prev_el
                                    #print("Your real mean arterial blood pressure is : " + str(prev_el))
                        for num, i in enumerate(listOfOscillations[1:], 1):
                            if (i - prev) / prev > threshold:
                                peaks.append(num)
                            prev = i or 0.001

                        # print(peaks)

                        currentTime = (endTime - beginningTime).total_seconds()
                        relativeTime = (endTime - conductExamScreen.examStartTime).total_seconds()
                        pulseRate = ((((len(peaks))) / currentTime) * 60)
                        #print("The pulse rate is: " + str(pulseRate))
                        tempMeasurementBP = conductExamScreen.singularRecording(relativeTime, finalMeasurement, conductExamScreen.newQuestion, conductExamScreen.yn)
                        tempMeasurementPR = conductExamScreen.singularRecording(relativeTime, pulseRate,conductExamScreen.newQuestion, conductExamScreen.yn)
                        conductExamScreen.bloodPressureRecordings.append(tempMeasurementBP)
                        conductExamScreen.pulseRecordings.append(tempMeasurementPR)
                        '''print("Added BP: ", tempMeasurementBP.measurement)
                        print("Associated Time: ", tempMeasurementBP.timestamp)
                        print("BP Collections: ", len(conductExamScreen.bloodPressureRecordings))
                        print("Added PR: ", tempMeasurementPR.measurement)
                        print("Associated Time: ", tempMeasurementPR.timestamp)
                        print("PR Collections: ", len(conductExamScreen.pulseRecordings))'''
                        conductExamScreen.bloodPressureMeasurements.append(finalMeasurement)
                        conductExamScreen.bloodPressureTimings.append(relativeTime)
                        conductExamScreen.pulseMeasurements.append(pulseRate)
                        conductExamScreen.pulseTimings.append(relativeTime)
                        #conductExamScreen.window.write_event_value('-UPDATED-', None)
                        correctPressure = True
                        listOfOscillations = []
                        possibleBP = []
                        # prev = listOfOscillations[0] or 0.001
                        peaks = []

    print("Blood Pressure: exited")


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
    from gdx4 import gdx
    theAPIs = gdx()
    connected = False
    while connected == False:
        bloodPressureConnected = theAPIs.open_ble('GDX-BP 141014A2')
        if (IndividualDeviceScreen.exited):
            connected = True
            IndividualDeviceScreen.recordingStarted = True
            IndividualDeviceScreen.recordingStopped = True
            theAPIs.close()
        if (bloodPressureConnected == True):
            if (IndividualDeviceScreen.exited):
                connected = True
                IndividualDeviceScreen.recordingStarted = True
                IndividualDeviceScreen.recordingStopped = True
                theAPIs.close()
            else:
                IndividualDeviceScreen.deviceConnected = True
                IndividualDeviceScreen.window['theImage1'].update(data=IndividualDeviceScreen.checkmarkImage)
                connected = True
        else:
            theAPIs.close()
    while not IndividualDeviceScreen.recordingStarted:
        if (IndividualDeviceScreen.exited):
            IndividualDeviceScreen.recordingStarted = True
            IndividualDeviceScreen.recordingStopped = True
            theAPIs.close()
        time.sleep(1)
        pass

    if not IndividualDeviceScreen.exited:
        print("Starting Exam in BP")
        # blood pressure sensor can measure mean arterial pressure, systolic (the maximum), diastolic (minimum)
        # Also, sampling rate would be different then the other device, since recording blood pressure will take longer
        theAPIs.select_sensors([1, 7])

        # rate = PolygraphExamSetupScreen.BloodPressureSamplingRate * 1000
        theAPIs.start(100)
        print("BloodPressure Started")

        listOfOscillations = []
        possibleBP = []
        maxOsc = 0
        conductExamScreen.inQuestion = False
        # prev = listOfOscillations[0] or 0.001
        threshold = 0.5
        peaks = []

        # for num, i in enumerate(listOfOscillations[1:], 1):
        #     if (i - prev) / prev > threshold:
        #         peaks.append(num)
        #     prev = i or 0.001
        #
        # print(peaks)

        # pulseRate = ((((len(peaks))) / totalTime) * 60)
        # print("The pulse rate is: " + str(pulseRate))
        # # This continuously reads cuff pressure, until the pressure is above 155 and then it stops reading
        # # Cuff pressure needs to be at least 155 for the device to start reading blood pressure
        # # then when the cuff pressure is around 50, the device spits out your blood pressure measurements (and any other data collected would be printed at this time)
        # examStartTime = datetime.datetime.now()
        while IndividualDeviceScreen.recordingStopped == False:
            if IndividualDeviceScreen.exited:
                IndividualDeviceScreen.recordingStopped = True
                theAPIs.close()
            else:
                measurements = theAPIs.read()
                correctPressure = False
                pressureBar = False
                progress_bar = IndividualDeviceScreen.window['progress']
                if ((measurements[0] < 150)):
                    # measurements1 = theAPIs.read()
                    # conductExamScreen.window['-CuffPressure-'].update(measurements[0])
                    # print("Paused Measurements: ", measurements[0])
                    while pressureBar == False:
                        if (IndividualDeviceScreen.exited == True):
                            IndividualDeviceScreen.recordingStopped = True
                            pressureBar = True
                        # make_bloodPressure_bar()
                        # progress_bar1 = sg.window['progress1']
                        measurements1 = theAPIs.read()
                        print("Paused Measurements: ", measurements1[0])
                        if measurements1[0] < 15:
                            print("you made it to 10 percent")
                            progress_bar.update_bar(1)  # show 10% complete
                            # sleep(2)

                        if 16 < measurements1[0] < 30:
                            print("you made it to 20 percent")
                            progress_bar.update_bar(2)  # show 20% complete

                            # sleep(2)
                        if 31 < measurements1[0] < 45:
                            print("you made it to 30 percent")
                            progress_bar.update_bar(3)  # show 30% complete
                            # sleep(2)

                        if 46 < measurements1[0] < 60:
                            print("you made it to 40 percent")
                            progress_bar.update_bar(4)  # show 40% complete
                            # sleep(2)
                        if 61 < measurements1[0] < 75:
                            print("you made it to 50 percent")
                            progress_bar.update_bar(5)  # show 50% complete
                            # sleep(2)

                        if 76 < measurements1[0] < 90:
                            print("you made it to 60 percent")
                            progress_bar.update_bar(6)  # show 60% complete
                            # sleep(2)
                        if 91 < measurements1[0] < 105:
                            print("you made it to 70 percent")
                            progress_bar.update_bar(7)  # show 70% complete
                            # sleep(2)
                        if 106 < measurements1[0] < 120:
                            print("you made it to 80 percent")
                            progress_bar.update_bar(8)  # show 80% complete
                            # sleep(2)
                        if 121 < measurements1[0] > 135:
                            print("you made it to 90 percent")
                            progress_bar.update_bar(9)  # show 90% complete
                            # sleep(2)

                        if measurements1[0] > 150:
                            print("you made it to 100 percent")
                            progress_bar.update_bar(10)  # show 100% complete
                            # time.sleep(.5)
                            # progress_bar.window.close()
                            pressureBar = True
                else:
                    beginningTime = datetime.datetime.now()
                    while correctPressure == False:
                        if (IndividualDeviceScreen.exited == True):
                            IndividualDeviceScreen.recordingStopped = True
                            correctPressure = True
                        measurements = theAPIs.read()
                        print("Recording Measurements: ", measurements[0])
                        #               currentTime = (datetime.datetime.now() - examStartTime).total_seconds()
                        possibleBP.append(measurements)
                        listOfOscillations.append(measurements[1])
                        if measurements[1] > maxOsc:
                            maxOsc = measurements[1]
                        if measurements[0] < 70:
                            endTime = datetime.datetime.now()
                            print("Less than 70")
                            listt = []
                            prev = listOfOscillations[0] or 0.001
                            for inner_list in (possibleBP):
                                for element in (inner_list):
                                    listt.append(element)
                                    # if element == maxOsc:
                                    #     print("Your mean arterial blood pressure is : " + str(element-1))

                            for index, elem in enumerate(listt):
                                if (index + 1 < len(listt) and index - 1 >= 0):
                                    prev_el = listt[index - 1]
                                    if elem == maxOsc:
                                        finalMeasurement = prev_el
                                        # print("Your real mean arterial blood pressure is : " + str(prev_el))
                            for num, i in enumerate(listOfOscillations[1:], 1):
                                if (i - prev) / prev > threshold:
                                    peaks.append(num)
                                prev = i or 0.001

                            # print(peaks)

                            currentTime = (endTime - beginningTime).total_seconds()
                            pulseRate = ((((len(peaks))) / currentTime) * 60)
                            # print("The pulse rate is: " + str(pulseRate))
                            IndividualDeviceScreen.deviceMeasurements.append(finalMeasurement)
                            IndividualDeviceScreen.deviceMeasurements.append(pulseRate)
                            IndividualDeviceScreen.recordingStopped = True
                            correctPressure = True
                            IndividualDeviceScreen.window.write_event_value('-BPEnded-', None)

    print("Blood Pressure: exited")

# def make_bloodPressure_bar():
#     layout = [[sg.Text('Blood pressure bar')],
#               [sg.ProgressBar(max_value=10, orientation='h', size=(20, 20), key='progress')]]
#
#     # create the form`
#     # must finalize since not running an event loop
#     window = sg.Window('Custom Progress Meter', layout, finalize=True)
#
#     # Get the element to make updating easier
#     progress_bar1 = window['progress']
    # measurements1 = theAPIs.read()
    # print("Paused Measurements: ", measurements1[0])
    # if measurements1[0] < 15:
    #     print("you made it to 10 percent")
    #     progress_bar.update_bar(1)  # show 10% complete
    #     # sleep(2)
    #
    # if 16 < measurements1[0] < 30:
    #     print("you made it to 20 percent")
    #     progress_bar.update_bar(2)  # show 20% complete
    #
    #     # sleep(2)
    # if 31 < measurements1[0] < 45:
    #     print("you made it to 30 percent")
    #     progress_bar.update_bar(3)  # show 30% complete
    #     # sleep(2)
    #
    # if 46 < measurements1[0] < 60:
    #     print("you made it to 40 percent")
    #     progress_bar.update_bar(4)  # show 40% complete
    #     # sleep(2)
    # if 61 < measurements1[0] < 75:
    #     print("you made it to 50 percent")
    #     progress_bar.update_bar(5)  # show 50% complete
    #     # sleep(2)
    #
    # if 76 < measurements1[0] < 90:
    #     print("you made it to 60 percent")
    #     progress_bar.update_bar(6)  # show 60% complete
    #     # sleep(2)
    # if 91 < measurements1[0] < 105:
    #     print("you made it to 70 percent")
    #     progress_bar.update_bar(7)  # show 70% complete
    #     # sleep(2)
    # if 106 < measurements1[0] < 120:
    #     print("you made it to 80 percent")
    #     progress_bar.update_bar(8)  # show 80% complete
    #     # sleep(2)
    # if 121 < measurements1[0] > 135:
    #     print("you made it to 90 percent")
    #     progress_bar.update_bar(9)  # show 90% complete
    #     # sleep(2)
    #
    # if measurements1[0] > 150:
    #     print("you made it to 100 percent")
    #     progress_bar.update_bar(10)  # show 100% complete
    #     time.sleep(.5)
    #     pressureBar = True
    #     progress_bar.window.close()


# def make_bloodPressure_bar():
#     layout = [[sg.Text('Blood pressure bar')],
#               [sg.ProgressBar(max_value=10, orientation='h', size=(20, 20), key='progress1')]]
#
#     # create the form`
#     # must finalize since not running an event loop
#     return sg.Window('Custom Progress Meter', layout, finalize=True)
#
#     # Get the element to make updating easier



