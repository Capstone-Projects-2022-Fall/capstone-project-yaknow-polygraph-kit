from gdx import gdx
import tensorflow as tensorflow

theAPIs = gdx()

theAPIs.open_usb()
theAPIs.select_sensors()
theAPIs.start()
deviceMeasurements = theAPIs.read()
theAPIs.stop()
theAPIs.close()

print("Tensorflow running as version", tensorflow.__version__)

