import socket

IP = "129.32.95.112"
# IP = "127.0.1.1"
# IP = "192.168.1.159"
PORT = 30001
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
    data = ""

    while data != "-1":
        data = input(":")
        """ Sending the file data to the server. """
        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print("[SERVER]: " + msg)

    """ Closing the connection from the server. """
    client.close()


if __name__ == "__main__":
    main()
