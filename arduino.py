import csv
import datetime
import serial
import time

import PolygraphExamSetupScreen
import IndividualDeviceScreen
import conductExamScreen
import arduino

baud = 9600
file_name = "analog_data.csv"
#arduino_port = "/dev/cu.usbmodem14101"
#arduino_port = "COM1"
arduino_port = "COM4"
arduino.arduino_port = "/dev/cu.usbmodem14101"
#arduino_port = "COM4"
arduino_port2 = "/dev/cu.usbmodem101"


def connectGSRSensor():
    '''
    Purpose:
        A thread that connects and records GSR data from the Arduino GSR Sensor in a non-blocking way and communicates the stored data with the main thread.

    Pre-conditions:
        Must be started within the context of a polygraph exam.

    Post-conditions:
        Exits the thread upon exam completion.

    Parameters and data types:
        PolygraphExamSetup.window - PySimpleGUI window
        PolygrpahExamSetup.GSRSamplingRate - int
        conductExamScreen.examFinished - boolean
        conductExamScreen.skinConductivityRecordings - Array of singularRecording class instance
        conductExamScreen.skinConductivityTimings - Array of float
        conductExamScreen.skinConductivityMeasurements - Array of float

    Return value and output variables:
        conductExamScreen.skinConductivityRecordings - Array of singularRecording class instance
        conductExamScreen.skinConductivityMeasurements - Array of float
        conductExamScreen.skinConductivityTimings - Array of float

    Exceptions thrown:
        None.

    '''
    connected = False
    immediateExit = False
    while ( (connected == False) and (immediateExit == False) ):
        print(arduino.arduino_port)
        try:
            ser = serial.Serial(arduino.arduino_port, baud)
            connected = True
        except Exception as e:
            print("Board Not Connected", e)
            '''try:
                ser = serial.Serial(arduino_port2, baud)
            except:
                print("Neither Port Connected")'''

        if (connected == True):
            PolygraphExamSetupScreen.GSRConnector = True
            PolygraphExamSetupScreen.window['theImage2'].update(data=PolygraphExamSetupScreen.checkmarkImage)
            PolygraphExamSetupScreen.window.refresh()
            connected = True
        if (PolygraphExamSetupScreen.examStarted == True):
            immediateExit = True
        time.sleep(5)
    while not ( (PolygraphExamSetupScreen.examStarted) and immediateExit == False):
        time.sleep(1)
        pass

    if(immediateExit == False):
        sensor_data = []
        rate = PolygraphExamSetupScreen.GSRSamplingRate
        #examStartTime = datetime.datetime.now()
        while conductExamScreen.examFinished == False:
            if (conductExamScreen.inQuestion == True):
                getData = ser.readline()
                data = int(getData.decode('utf-8'))
                currentTime = (datetime.datetime.now() - conductExamScreen.examStartTime).total_seconds()
                final_reading = ((1024 + 2 * data) * 10000) / (512 - data)
                tempMeasurement = conductExamScreen.singularRecording(currentTime, final_reading, conductExamScreen.newQuestion, conductExamScreen.yn)
                conductExamScreen.skinConductivityRecordings.append(tempMeasurement)
                conductExamScreen.skinConductivityMeasurements.append(final_reading)
                conductExamScreen.skinConductivityTimings.append(currentTime)
                #conductExamScreen.window.write_event_value('-UPDATED-', None)
                print("Failed GSR")
                time.sleep(rate)
                print(final_reading)
            else:
                time.sleep(.5)
    print("GSR Exited")



def connectGSRSensorIndividual():
    connected = False
    while connected == False:
        try:
            ser = serial.Serial(arduino_port, baud)
            connected = True
        except Exception as e:
            print("Board Not Connected", e)
            try:
                ser = serial.Serial(arduino_port2, baud)
            except:
                print("Neither Port Connected")

        if (connected == True):
            IndividualDeviceScreen.deviceConnected = True
            IndividualDeviceScreen.window['theImage1'].update(data=IndividualDeviceScreen.checkmarkImage)
            IndividualDeviceScreen.window.refresh()
            connected = True
        time.sleep(5)
    while not IndividualDeviceScreen.recordingStarted:
        pass

    sensor_data = []
    times = int (IndividualDeviceScreen.deviceTime / IndividualDeviceScreen.DeviceSamplingRate)
    print("GSR: Started")
    for i in range(times):
        getData = ser.readline()
        data = int(getData.decode('utf-8'))
        currentTime = datetime.datetime.now()
        final_reading = ((1024 + 2 * data) * 10000) / (512 - data)
        print(currentTime, final_reading)
        sensor_data.append(final_reading)
        time.sleep(IndividualDeviceScreen.DeviceSamplingRate)
    print(final_reading)

    # if devicesFound is None:
    #    logging.error('No Device connected.')
    # else:
    #    logging.info('Devices found:' + devicesFound)

    # print("Hello World")

# GUI Branch
