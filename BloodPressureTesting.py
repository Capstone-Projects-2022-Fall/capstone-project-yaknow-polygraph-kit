import logging
import datetime

import PolygraphExamSetupScreen
import IndividualDeviceScreen

import math
import numpy as np

import time

from scipy.signal import find_peaks

# import numpy as np


with open('polygraphExamKitLogging.log', 'w'):
    pass

log_format = '%(asctime)s %(filename)s - %(levelname)s: %(message)s'
logging.basicConfig(filename='polygraphExamKitLogging.log', level=logging.DEBUG, force=True, format=log_format,
                    datefmt='%H:%M:%S')


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
        #        devicesFound = theAPIs.open_usb()
        if devicesFound == True:
            connected = True
        # else:
        #     logging.info('Devices found:' + devicesFound)
    theAPIs.select_sensors([1, 7])
    theAPIs.start(100)
    correctPressure = False
    possibleBP = []
    listOfOscillations = []
    maxOsc = 0
    t0 = time.time()
    # # This continuously reads cuff pressure, until the pressure is above 155 and then it stops reading
    # # Cuff pressure needs to be at least 155 for the device to start reading blood pressure
    # # then when the cuff pressure is around 50, the device spits out your blood pressure measurements (and any other data collected would be printed at this time)
    while correctPressure == False:
        measurements = theAPIs.read()
        print(measurements)
        possibleBP.append(measurements)
        listOfOscillations.append(measurements[1])
        if measurements[1] > maxOsc:
            maxOsc = measurements[1]
        if measurements[0] < 60:
            correctPressure = True

    t1 = time.time()
    theAPIs.stop()
    totalTime = t1 - t0

    print("Max oscillation is : " + str(maxOsc))

    print("the time it took to find blood pressure: " + str(totalTime))

    # oscillationPeaks = (find_peaks(listOfOscillations))
    # # x = np.linspace()
    # peak_pos = [oscillationPeaks[0]]
    # print(peak_pos)
    # oscillationPeaksList = (list(oscillationPeaks))


# Pulse rate math
    prev = listOfOscillations[0] or 0.001
    threshold = 0.5
    peaks = []

    for num, i in enumerate(listOfOscillations[1:], 1):
        if (i - prev) / prev > threshold:
            peaks.append(num)
        prev = i or 0.001

    print(peaks)

    #   print(oscillationPeaks.sum())
    #   print(oscillationPeaks[0].size)
    #    print(oscillationPeaksList)

    #    print(len(oscillationPeaksList))

    #  print("Length of number of peaks: " + str(len(find_peaks(listOfOscillations))))
    #  print("Length of number of peaks: " + str(np.count_nonzero((find_peaks(listOfOscillations)))))
    print("Length of number of peaks: " + str(peaks))

    pulseRate = ((((len(peaks))) / totalTime) * 60)
    print("The pulse rate is: " + str(pulseRate))

    #  print(possibleBP)

    # Creates a list of lists from the measurements, then creats a list of each value going from cuff pressure, oscillation, cuff pressure, oscillation, etc
    # then from there finds the max value of the oscilation, then gets the corresponding cuff pressure, which is mean arterial pressure

    listt = []
    for inner_list in (possibleBP):
        for element in (inner_list):
            listt.append(element)
            # if element == maxOsc:
            #     print("Your mean arterial blood pressure is : " + str(element-1))

    for index, elem in enumerate(listt):
        if (index + 1 < len(listt) and index - 1 >= 0):
            prev_el = str(listt[index - 1])
            if elem == maxOsc:
                print("Your real mean arterial blood pressure is : " + str(prev_el))

    #    theAPIs.select_sensors([1])

    #    theAPIs.start()
    #    correctPressure = False
    # This will continuously print out empty arrays - I thought if we just made it go longer, eventually it would print out the result, but it didnt
    #     for i in range(40):
    #         measurements = theAPIs.read()
    #         if measurements == None:
    #             break
    #         print(measurements)
    # IDEA: print out the values (they are nothing) until a result is more than 0 (the blood pressure) *this prints absolutely nothing tho*
    # while correctPressure == False:
    #     measurements = theAPIs.read()
    #     print(measurements)
    #     if measurements[0] > 1:
    #         correctPressure = True

    theAPIs.stop()

if __name__ == "__main__":
    main()

