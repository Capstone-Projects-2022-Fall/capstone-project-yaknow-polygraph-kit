import socket


#ncServerPort = 30006
#ncFilePort = 30010  # data file port
mlServerPort = 30012
#mlFilePort = 30017

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '129.32.22.10'
#port = 9990

server_socket.bind((HOST, mlServerPort))
server_socket.listen(5)

print("Server started...")

client_sockets, addr = server_socket.accept()
while True:
    msg_received = client_sockets.recv(1024)
    msg_received = msg_received.decode()
    print("Client:", msg_received)

    msg_send = input("Me:")
    client_sockets.send(msg_send.encode("ascii"))

client_sockets.close()