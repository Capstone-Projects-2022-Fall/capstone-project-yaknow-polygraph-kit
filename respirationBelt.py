

#import tensorflow as tensorflow
import logging
from PIL import Image, ImageTk
import datetime

import PolygraphExamSetupScreen

with open('polygraphExamKitLogging.log', 'w'):
    pass

log_format = '%(asctime)s %(filename)s - %(levelname)s: %(message)s'

logging.basicConfig(filename='polygraphExamKitLogging.log', level=logging.DEBUG, force=True, format=log_format, datefmt='%H:%M:%S')



def connectRespirationBelt():
    from gdx import gdx
    theAPIs = gdx()
    connected = False
    while connected == False:
        respirationConnected = theAPIs.open_ble('GDX-RB 0K4007N0')
        if(respirationConnected == True):
            PolygraphExamSetupScreen.respirationConnected = True
            PolygraphExamSetupScreen.window['theImage3'].update(data=PolygraphExamSetupScreen.checkmarkImage)
            PolygraphExamSetupScreen.window.refresh()
            connected = True
        else:
            theAPIs.close()
    while not PolygraphExamSetupScreen.examStarted:
        pass

    theAPIs.select_sensors([1])

    rate = PolygraphExamSetupScreen.RespirationSamplingRate * 1000
    theAPIs.start(rate)

    for i in range(10):
        measurements = theAPIs.read()
        currentTime = datetime.datetime.now()
        if measurements == None:
            break
        print(currentTime, measurements)
    #if devicesFound is None:
    #    logging.error('No Device connected.')
    #else:
    #    logging.info('Devices found:' + devicesFound)


    #print("Hello World")




#theAPIs.stop()
#theAPIs.close()

#print("Tensorflow running as version", tensorflow.__version__)