import os
import socket

# hostname -I
IP = "129.32.22.10"
PORT = 30006
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024





def conect(dataset):
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # permission net permitted for some reason
    # socket.sethostname("cis-linux2.temple.edu")

    """ Connecting to the server. """
    client.connect(ADDR)

    """ Opening and reading the file data. """
    data = ""

    while data != "-1":
        data = input(":")
        """ Sending the file data to the server. """
        client.send(data.encode(FORMAT))
        """ 
        //ssh into cis linux 2 directly instead of 
        //we should be good to go since we have 

        """
        msg = client.recv(SIZE).decode(FORMAT)
        print("[SERVER]: " + msg)

    client.send("$")
    os.system()
    client.send("$")
    client.send("")
    client.send("")
    client.send("")

    """ Closing the connection from the server. """
    client.close()
