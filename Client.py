import os
import socket
import time

ncServerPort = 30006
ncFilePort = 30010  # data file port
mlServerPort = 30012
mlFilePort = 30017

# TODO: Create 2 servers we will be connecting to. One for to netcat dataFile and the other to lauchml/netcat back.
"hostname -I"
serverIP = "129.32.22.10"
# PORT = 30006
ADDR = (serverIP, ncServerPort)
mlAdDDR = (serverIP, mlServerPort)
FORMAT = "utf-8"
SIZE = 1024


def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # permission net permitted for some reason
    # socket.sethostname("cis-linux2.temple.edu")
    """ Connecting to the server. """
    client.connect(ADDR)
    """ Opening and reading the file data. """
    myhostname = socket.gethostname()
    extendedIP = socket.gethostbyname_ex(myhostname)
    myIPAddr = extendedIP[2][len(extendedIP[2]) - 1]

    "send data file to server"
    client.send(("$nc -v -w 30 -p" + str(ncFilePort) + " -l > datafile.txt").encode(FORMAT))  # prep receiver (severer)
    os.system("nc -v -w 2 " + str(serverIP) + " " + str(ncFilePort) + " < datafile.txt")  # send file
    print("data file sent")
    client.send("$exit".encode(FORMAT))
    client.close()

    "new connection to server via another port "
    mlClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mlClient.connect(mlAdDDR)
    print("new connection")
    "receive data file from console"
    #os.system("nc -v -w 30 -p" + str(mlFilePort) + " -l > mlResult.txt")


if __name__ == "__main__":
    main()
