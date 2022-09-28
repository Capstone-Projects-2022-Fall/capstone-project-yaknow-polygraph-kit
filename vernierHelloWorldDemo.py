from gdx import gdx

theAPIs = gdx()

theAPIs.open_usb()
theAPIs.select_sensors()
theAPIs.start()
deviceMeasurements = theAPIs.read()
theAPIs.stop()
theAPIs.close()