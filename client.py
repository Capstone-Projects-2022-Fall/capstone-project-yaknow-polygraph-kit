import os
import socket
import time

# hostname -I
IP = "129.32.22.10"
PORT = 30006
ADDR = (IP, PORT)
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
    myIPAddr = socket.gethostbyname(myhostname)

    """prepare the server to output to that file on that port"""
    client.send("$nc -nlvp 4000 > dataSetFile.txt".encode(FORMAT))

    'I suspect there is no wait time needed because it is not consecutive sever commands'
    os.system("nc 129.32.22.10 4000 < dataSetFile.txt")  # send a filem to the server using that server and port
    time.sleep(10)
    client.send("$echo printed file".encode(FORMAT))


   # client.send("$python ml.py".encode(FORMAT))  # execute machine learning
    #time.sleep(20)
   # os.system("nc -nlvp 30002 >  prediction.txt")  # now the client preps to recive
   # time.sleep(14)
   # client.send(("$nc " + str(myIPAddr) + " 30002 < prediction.txt").encode(FORMAT))  # the server sends
    # read file and display data  ~make if or statements or some command, so we only get the strongest truth

    """ Closing the connection from the server. """
    client.close()

if __name__ == "__main__":
    main()


