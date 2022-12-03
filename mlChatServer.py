"""import socket

mlServerPort = 20012
IP = "129.32.22.10"
# PORT = 30006
ADDR = (IP, mlServerPort)
SIZE = 1024
FORMAT = "utf-8"


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")

    conn, addr = server.accept()
    print("New Connection")

    file = open("mlResult.txt", "r")
    print("read data")

    count = 0

    for line in file:

        conn.send(line.encode(FORMAT))  # send to Client

        if count == 0:
            print("sending Data")
            count += 1

    file.close()
    print("File Closed")

    conn.shutdown(socket.SHUT_RDWR)
    conn.close()
    print("Server closed")


if __name__ == "__main__":
    main()"""
