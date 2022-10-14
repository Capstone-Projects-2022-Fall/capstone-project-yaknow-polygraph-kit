import serial
import time


def main_func():
    try:
        arduino = serial.Serial('com3', 9600)
        arduinoRead = arduino.readline()
        decodedRead = str(arduinoRead[0:len(arduinoRead)].decode("utf-8"))
        list_values = decodedRead.split('sensorValue=')
        arduinoClose = arduino.close()
    except (OSError):
        print("No Board Found")

if __name__ == '__main__':
    main_func()