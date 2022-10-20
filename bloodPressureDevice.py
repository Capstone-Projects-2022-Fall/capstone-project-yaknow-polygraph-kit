import logging
import datetime

import PolygraphExamSetupScreen
import IndividualDeviceScreen


with open('polygraphExamKitLogging.log', 'w'):
    pass

log_format = '%(asctime)s %(filename)s - %(levelname)s: %(message)s'
logging.basicConfig(filename='polygraphExamKitLogging.log', level=logging.DEBUG, force=True, format=log_format, datefmt='%H:%M:%S')

def main():
    from gdx import gdx

    # import tensorflow as tensorflow
    import logging

    with open('polygraphExamKitLogging.log', 'w'):
        pass

    log_format = '%(asctime)s %(filename)s - %(levelname)s: %(message)s'

    logging.basicConfig(filename='polygraphExamKitLogging.log', level=logging.DEBUG, force=True, format=log_format,
                        datefmt='%H:%M:%S')

    theAPIs = gdx()

    devicesFound = theAPIs.open_ble('GDX-RB 0K4007N0')
    if devicesFound is None:
        logging.error('No Device connected.')
    else:
        logging.info('Devices found:' + devicesFound)

    theAPIs.select_sensors([1])

    theAPIs.start(1000)

    for i in range(10):
        measurements = theAPIs.read()
        if measurements == None:
            break
        print(measurements)


def connectBloodPressureDevice():
    from gdx import gdx
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

#TUNE THIS FOR BLOOD PRESSURE MEASUREMENTS !!!
# blood pressure sensor can measure mean arterial pressure, systolic (the maximum), diastolic (minimum)
# Also, sampling rate would be different then the other device, since recording blood pressure will take longer    
    theAPIs.select_sensors([2])         #should this be 2 since we are using '1' for respiration ?

    rate = PolygraphExamSetupScreen.BloodPressureSamplingRate * 1000
    theAPIs.start(rate)

    for i in range(12):
        measurements = theAPIs.read()
        currentTime = datetime.datetime.now()
        if measurements == None:
            break
        print("Blood Pressure Recordings: ", currentTime, measurements)



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

if __name__ == "__main__":
    main()

