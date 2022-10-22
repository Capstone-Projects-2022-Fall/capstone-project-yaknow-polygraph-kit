# Data - Structure -> timestamp, measurement, question, response

import serial
import time
from matplotlib import pyplot as plt

list_question = ["Are You Keshav Saraogi?", "Are Your 23 Years Old?", "Are You Getting 7 Hours of Sleep?",
                 "Are You On Drugs?"]
list_response = []
list_timestamp = []
list_measurement = []
samples_per_question = 10

baud = 9600
file_name = "analog_data.csv"
arduino_port = "/dev/cu.usbmodem2101"

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)


def data_collection(samples):
    collected_samples = 0
    sensor_data = []
    sensor_time = []
    while collected_samples < samples:
        getData = ser.readline()
        local_time = time.asctime(time.localtime(time.time()))
        data = int(getData.decode("utf-8"))
        final_reading = ((1024 + 2 * data) * 10000) / (512 - data)
        sensor_data.append(final_reading)
        sensor_time.append(local_time)
        collected_samples += 1

    return sensor_data, sensor_time


for i in range(len(list_question)):
    print("Question: " + list_question[i])
    response = input("What Is Your Response (y/n): ")
    if (response == "y" or response == "n"):
        list_response.insert(i, response)
        timestamp, measurement = data_collection(samples_per_question)

        list_measurement.insert(i, measurement)
        list_timestamp.insert(i, timestamp)
    else:
        break


