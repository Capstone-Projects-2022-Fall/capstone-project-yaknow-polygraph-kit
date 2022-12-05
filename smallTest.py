import numpy
from numpy import loadtxt


def main():
    my_data = numpy.genfromtxt('dataSetFile.csv', delimiter=',', dtype=float)
    accData = numpy.resize(my_data, (len(my_data) - 1, 6))
    finData = numpy.resize(accData, (9, 6))
    print(finData[0])
    curQID = accData[0][0]
    tsStamp = 0.0
    pulse = 0.0
    skin_conductivity = 0.0
    respiration_belt = 0.0
    blood_pressure = 0.0
    counter = 0.1
    for x in accData:
        if curQID != x[0]:
            curQID = x[0]
            tsStamp += x[1]
            pulse += x[2]
            skin_conductivity += x[3]
            respiration_belt += x[4]
            blood_pressure += x[5]
            counter += 1
        else:
            numpy.insert(finData, 1, (curQID, tsStamp/counter, pulse/counter, skin_conductivity/counter, respiration_belt/counter, blood_pressure/counter))
            curQID = x[0]
            tsStamp = x[1]
            pulse = x[2]
            skin_conductivity = x[3]
            respiration_belt = x[4]
            blood_pressure = x[5]
            counter = 0.1

    print(finData)


if __name__ == "__main__":
    main()
