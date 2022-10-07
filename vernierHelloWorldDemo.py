from gdx import gdx
#import tensorflow as tensorflow
#tensorflow is no loner needed as everthing regarding it will be done remotly.
import logging

with open('polygraphExamKitLogging.log', 'w'):
    pass

log_format = '%(asctime)s %(filename)s - %(levelname)s: %(message)s'

logging.basicConfig(filename='polygraphExamKitLogging.log', level=logging.DEBUG, force=True, format=log_format, datefmt='%H:%M:%S')

theAPIs = gdx()

devicesFound = theAPIs.open_usb()
if devicesFound is None:
    logging.error('No Device connected.')
else:
    logging.info('Devices found:' + devicesFound)

theAPIs.select_sensors()
theAPIs.start()
deviceMeasurements = theAPIs.read()
theAPIs.stop()
theAPIs.close()

#print("Tensorflow running as version", tensorflow.__version__)