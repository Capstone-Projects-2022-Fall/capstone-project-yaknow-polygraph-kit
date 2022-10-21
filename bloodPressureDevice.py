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
    connected = False
    while connected == False:
        devicesFound = theAPIs.open_ble('GDX-BP 141014A2')
        if devicesFound == True:
            connected = True
        # else:
        #     logging.info('Devices found:' + devicesFound)
#     theAPIs.select_sensors([1])
#     theAPIs.start(500)
#     correctPressure = False
# # This continuously reads cuff pressure, until the pressure is above 155 and then it stops reading
# # Cuff pressure needs to be at least 155 for the device to start reading blood pressure
# # then when the cuff pressure is around 50, the device spits out your blood pressure measurements (and any other data collected would be printed at this time)
#     while correctPressure == False:
#         measurements = theAPIs.read()
#         print(measurements)
#         if measurements[0] > 155:
#             correctPressure = True

#    theAPIs.stop()
    theAPIs.select_sensors([2])

    theAPIs.start(500)
# This will continuously print out empty arrays - I thought if we just made it go longer, eventually it would print out the result, but it didnt
    for i in range(40):
        measurements = theAPIs.read()
        if measurements == None:
            break
        print(measurements)
#IDEA: print out the values (they are nothing) until a result is more than 0 (the blood pressure) *this prints absolutely nothing tho*
    # while correctPressure == False:
    #     measurements = theAPIs.read()
    #     print(measurements)
    #     if measurements[0] > 0:
    #         correctPressure = True

    theAPIs.stop()

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
    theAPIs.select_sensors([1])         #should this be 2 since we are using '1' for respiration ?

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

