# implement sending an image over udp using socket library

# Path: rec.py
# Compare this snippet from reciever.py:
import socket

recieverIP = ""
recieverPort   = 20002
bufferSize  = 1024 #Message Buffer Size

# bytesToSend = str.encode(msgFromServer)

# Create a UDP socket
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind socket to localIP and localPort
socket_udp.bind((recieverIP, recieverPort))

print("UDP socket created successfully....." )

while True:

    #wait to recieve message from the server
    bytesAddressPair = socket_udp.recvfrom(bufferSize)
    print(bytesAddressPair) #print recieved message

    #split the recieved tuple into variables
    recievedMessage = bytesAddressPair[0]
    senderAddress = bytesAddressPair[1]

    #print them just for understanding
    msgString = "Message from Client:{}".format(recievedMessage)
    detailString  = "Client IP Address:{}".format(senderAddress)
    print(msgString)
    print(detailString)

    # Sending a reply to client
    message = str.encode("This is a reply message from the server")
    socket_udp.sendto(message, senderAddress)
