from gdx import gdx

#import tensorflow as tensorflow
import logging

with open('polygraphExamKitLogging.log', 'w'):
    pass

log_format = '%(asctime)s %(filename)s - %(levelname)s: %(message)s'

logging.basicConfig(filename='polygraphExamKitLogging.log', level=logging.DEBUG, force=True, format=log_format, datefmt='%H:%M:%S')

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


#theAPIs.stop()
#theAPIs.close()

#print("Tensorflow running as version", tensorflow.__version__)