import socket

mlServerPort = 20012
serverIP = "129.32.22.10"
ADDR = (serverIP, mlServerPort)
FORMAT = "utf-8"
SIZE = 1024


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(ADDR)
    print("connected")
    file = open("mlResult.txt", "w")
    print("file created")
    msg = " "
    count = 0
    while count < 9:
        msg = client.recv(SIZE).decode(FORMAT)
        file.write(msg)
        print(msg)
        count += 1

    client.close()
    file.close()
    print("file closed")



if __name__ == "__main__":
    main()
