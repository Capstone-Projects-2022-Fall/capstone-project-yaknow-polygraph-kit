import csv
import datetime
import serial
import time

import PolygraphExamSetupScreen
import IndividualDeviceScreen

baud = 9600
file_name = "analog_data.csv"
arduino_port = "/dev/cu.usbmodem101"


def connectGSRSensor():

    connected = False
    while connected == False:
        try:
            print("Test")
            ser = serial.Serial(arduino_port, baud)
            print("Test2")
            connected = True
            print("Test3")
        except Exception as e:
            print("Board Not Connected", e)

        if(connected == True):
            PolygraphExamSetupScreen.GSRConnector = True
            PolygraphExamSetupScreen.window['theImage2'].update(data=PolygraphExamSetupScreen.checkmarkImage)
            PolygraphExamSetupScreen.window.refresh()
            connected = True
        time.sleep(5)
    while not PolygraphExamSetupScreen.examStarted:
        pass

    sensor_data = []
    rate = PolygraphExamSetupScreen.GSRSamplingRate

    times = int(IndividualDeviceScreen.DeviceSamplingTime / IndividualDeviceScreen.DeviceSamplingRate)
    for i in range(times):
        getData = ser.readline()
        data = int(getData.decode('utf-8'))
        currentTime = datetime.datetime.now()
        final_reading = ((1024 + 2 * data) * 10000) / (512 - data)
        print(currentTime, final_reading)
        sensor_data.append(final_reading)
        time.sleep(rate)
    print(final_reading)


def connectGSRSensorIndividual():

    connected = False
    while connected == False:
        try:
            print("Test")
            ser = serial.Serial(arduino_port, baud)
            print("Test2")
            connected = True
            print("Test3")
        except Exception as e:
            print("Board Not Connected", e)

        if (connected == True):
            IndividualDeviceScreen.deviceConnected = True
            IndividualDeviceScreen.window['theImage1'].update(data=IndividualDeviceScreen.checkmarkImage)
            IndividualDeviceScreen.window.refresh()
            connected = True
        time.sleep(5)
    while not IndividualDeviceScreen.recordingStarted:
        pass

    sensor_data = []
    rate = IndividualDeviceScreen.DeviceSamplingRate

    for i in range( (IndividualDeviceScreen.deviceTime) / (IndividualDeviceScreen.DeviceSamplingRate) ):
        getData = ser.readline()
        data = int(getData.decode('utf-8'))
        currentTime = datetime.datetime.now()
        final_reading = ((1024 + 2 * data) * 10000) / (512 - data)
        print(currentTime, final_reading)
        sensor_data.append(final_reading)
        time.sleep(rate)
    print(final_reading)



    #if devicesFound is None:
    #    logging.error('No Device connected.')
    #else:
    #    logging.info('Devices found:' + devicesFound)


    #print("Hello World")


# GUI Branch
