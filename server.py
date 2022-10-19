import socket
import os

IP = "129.32.95.96"
PORT = 30001
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


def main():
    print("Port: " + str(PORT) + "\nIP: " + str(IP) + "\nAddress: " + str(ADDR))
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
        else:
            print("[RECV] message: " + msg)
        conn.send("Message received.".encode(FORMAT))

    """ Closing the connection from the client. """
    conn.close()
    print("[DISCONNECTED] disconnected form: " + str(addr))


if __name__ == "__main__":
    main()
