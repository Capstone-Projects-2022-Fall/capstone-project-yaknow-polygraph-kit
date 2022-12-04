

#import tensorflow as tensorflow
import logging
from PIL import Image, ImageTk
import datetime
import time
import PolygraphExamSetupScreen

import IndividualDeviceScreen

import conductExamScreen

with open('polygraphExamKitLogging.log', 'w'):
    pass

log_format = '%(asctime)s %(filename)s - %(levelname)s: %(message)s'

logging.basicConfig(filename='polygraphExamKitLogging.log', level=logging.DEBUG, force=True, format=log_format, datefmt='%H:%M:%S')

def connectRespirationBelt():
    '''
    Purpose:
        A thread that connects and records respiration force from the respiration belt in a non-blocking way and communicates the stored data with the main thread.

    Pre-conditions:
        Must be started within the context of a polygraph exam.

    Post-conditions:
        Exits the thread upon exam completion.

    Parameters and data types:
        PolygraphExamSetup.window - PySimpleGUI window
        PolygrpahExamSetup.RespirationSamplingRate - int
        conductExamScreen.examFinished - boolean
        conductExamScreen.respirationRecordings - Array of singularRecording class instance
        conductExamScreen.respirationTimings - Array of float
        conductExamScreen.respirationMeasurements - Array of float

    Return value and output variables:
        conductExamScreen.respirationRecordings - Array of singularRecording class instance
        conductExamScreen.respirationTimings - Array of float
        conductExamScreen.respirationMeasurements - Array of float

    Exceptions thrown:
        None.

    '''
    from gdx import gdx
    theAPIs = gdx()
    connected = False
    while connected == False:
        if (conductExamScreen.exited):
            connected = True
            PolygraphExamSetupScreen.examStarted = True
            PolygraphExamSetupScreen.examFinished = True
            theAPIs.close()
        respirationConnected = theAPIs.open_ble('GDX-RB 0K4007N0')
        if(respirationConnected == True):
            PolygraphExamSetupScreen.respirationConnected = True
            PolygraphExamSetupScreen.window['theImage3'].update(data=PolygraphExamSetupScreen.checkmarkImage)
            PolygraphExamSetupScreen.window.refresh()
            connected = True
        else:
            theAPIs.close()
    while not PolygraphExamSetupScreen.examStarted:
        if (conductExamScreen.exited):
            PolygraphExamSetupScreen.examStarted = True
            PolygraphExamSetupScreen.examFinished = True
            theAPIs.close()
        time.sleep(1)
        pass

    if not conductExamScreen.exited:

        theAPIs.select_sensors([1])

        rate = PolygraphExamSetupScreen.RespirationSamplingRate * 1000
        theAPIs.start(rate)
    #examStartTime = datetime.datetime.now()
    while conductExamScreen.examFinished == False:
        if(conductExamScreen.inQuestion == True):
            print("Recording Respiration")
            measurements = theAPIs.read()
            currentTime = (datetime.datetime.now() - conductExamScreen.examStartTime).total_seconds()
            if measurements is None:
                break
            tempMeasurement = conductExamScreen.singularRecording(currentTime, measurements[0], conductExamScreen.newQuestion, conductExamScreen.yn)
            conductExamScreen.respirationRecordings.append(tempMeasurement)
            conductExamScreen.respirationTimings.append(currentTime)
            conductExamScreen.respirationMeasurements.append(measurements[0])
            #conductExamScreen.window.write_event_value('-UPDATED-', None)
            print("Failed Respiration")
        else:
            time.sleep(.5)
    print("Respiration Exited")


def connectRespirationBeltIndividual():
    from gdx import gdx
    theAPIs = gdx()
    connected = False
    while connected == False:
        respirationConnected = theAPIs.open_ble('GDX-RB 0K4007N0')
        if(IndividualDeviceScreen.exited):
            connected = True
            IndividualDeviceScreen.recordingStarted = True
            IndividualDeviceScreen.recordingStopped = True
            theAPIs.close()
        if (respirationConnected == True):
            IndividualDeviceScreen.deviceConnected = True
            IndividualDeviceScreen.window.write_event_value('-Connected-', None)
            #IndividualDeviceScreen.window['theImage1'].update(data=IndividualDeviceScreen.checkmarkImage)
            #IndividualDeviceScreen.window.refresh()
            connected = True
        else:
            theAPIs.close()
    while not IndividualDeviceScreen.recordingStarted:
        if IndividualDeviceScreen.exited:
            IndividualDeviceScreen.recordingStarted = True
            IndividualDeviceScreen.recordingStopped = True
            theAPIs.close()
        time.sleep(1)
        pass

    if not IndividualDeviceScreen.exited:
        theAPIs.select_sensors([1])

        rate = IndividualDeviceScreen.DeviceSamplingRate * 1000
        theAPIs.start(rate)
        print("Respiration Started")

    while not IndividualDeviceScreen.recordingStopped:
        if IndividualDeviceScreen.exited:
            IndividualDeviceScreen.recordingStopped = True
            theAPIs.close()
        measurements = theAPIs.read()
        currentTime = (datetime.datetime.now() - IndividualDeviceScreen.recordingStartTime).total_seconds()
        if measurements == None:
            break
        IndividualDeviceScreen.deviceMeasurements.append(measurements)
        IndividualDeviceScreen.deviceTimings.append(currentTime)
        IndividualDeviceScreen.window.write_event_value('-UPDATED-', None)

    print("Respiration Exited")
    # if devicesFound is None:
    #    logging.error('No Device connected.')
    # else:
    #    logging.info('Devices found:' + devicesFound)

    # print("Hello World")
#theAPIs.stop()
#theAPIs.close()

#print("Tensorflow running as version", tensorflow.__version__)