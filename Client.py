import os
import socket
import time


ncServerPort = 30006
ncFilePort = 30010  # data file port
mlServerPort = 20012

# TODO: Create 2 servers we will be connecting to. One for to netcat dataFile and the other to lauchml/netcat back.
"hostname -I"
serverIP = "129.32.22.10"
ADDR = (serverIP, ncServerPort)
mlAdDDR = (serverIP, mlServerPort)
FORMAT = "utf-8"
SIZE = 1024


def main():
    print("here")
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # permission net permitted for some reason
    # socket.sethostname("cis-linux2.temple.edu")
    """ Connecting to the server. """
    print(client.connect(ADDR))
    """nc stuff"""
    myhostname = socket.gethostname()
    extendedIP = socket.gethostbyname_ex(myhostname)
    myIPAddr = extendedIP[2][len(extendedIP[2]) - 1]

    "send data file to server"
    client.send(("$nc -v -w 30 -p" + str(ncFilePort) + " -l > dataSetFile.csv").encode(FORMAT))  # prep receiver (severer)
    os.system("nc -v -w 2 " + str(serverIP) + " " + str(ncFilePort) + " < dataSetFile.csv")  # send file
    print("data file sent")
    client.send("$python3 3ml.py".encode(FORMAT))
    time.sleep(15)
    client.close()

    "get the data file"

    mlClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mlClient.connect(mlAdDDR)
    print("connected")
    file = open("mlResult.txt", "w")
    print("file created")
    msg = " "
    count = 0
    while count < 9:
        msg = mlClient.recv(SIZE).decode(FORMAT)
        file.write(msg)
        print(msg)
        count += 1

    mlClient.close()
    file.close()
    print("file closed")




if __name__ == "__main__":
    main()
