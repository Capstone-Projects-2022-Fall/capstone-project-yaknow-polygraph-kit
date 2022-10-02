import serial
import time


def main_func():
    arduino = serial.Serial('com3', 9600)
    arduinoRead = arduino.readline()
    decodedRead = str(arduinoRead[0:len(arduinoRead)].decode("utf-8"))
    list_values = decodedRead.split('sensorValue=')