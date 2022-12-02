import socket
import os

#ncServerPort = 30006
#ncFilePort = 30010
mlServerPort = 30012
#mlFilePort 30017



IP = "129.32.22.10"
#PORT = 3000
ADDR = (IP, mlServerPort)
SIZE = 1024
FORMAT = "utf-8"


def main():
    print("Port: " + str(mlServerPort) + "\nIP: " + str(IP) + "\nAddress: " + str(ADDR))
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")

    msg = ""
    """ Server has accepted the connection from the client. """
    conn, addr = server.accept()
    # print(f"[NEW CONNECTION] {addr} connected.")
    print("New Connection" + str(addr))


    while msg != "-1":
        """ Receiving the filename from the client. """
        msg = conn.recv(SIZE).decode(FORMAT)
        # print(f"[RECV] message: {msg}")
        if "$" in msg:
            msg = msg.replace('$', '')
            print("Command: " + msg)
            os.system(msg)


    """ Closing the connection from the client. """
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()
    print("[DISCONNECTED] disconnected form: " + str(addr))


if __name__ == "__main__":
    main()

