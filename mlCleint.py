import socket


#ncServerPort = 30006
#ncFilePort = 30010  # data file port
mlServerPort = 30012
#mlFilePort = 30017

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
LOCALHOST = '129.32.22.10'
#port = 9990

s.connect((LOCALHOST,mlServerPort))
print("New client created:")

while True:
    client_message = input("Me: ")
    s.send(client_message.encode())

    msg_received = s.recv(1024)
    msg_received = msg_received.decode()
    print("Server:",msg_received)

    if msg_received == 'exit':
        break
s.close()
