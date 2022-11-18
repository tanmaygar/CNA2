import socket
import time
import sys
import os
senderIP = "10.0.0.1"
senderPort   = 20001
recieverAddressPort = ("10.0.0.2", 20002)
bufferSize  = 1024 #Message Buffer Size

# Create a UDP socket at reciever side
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
TIMEOUTTIME = 100/1000
socket_udp.settimeout(TIMEOUTTIME) # value in seconds

# open image file
image = open("testFile.jpg", "rb")
# read image file in chunks
chunk = image.read(bufferSize-3)
# store chunks in a dictionary
chunks = {}
chunkNumber = 0
while chunk:
    chunks[chunkNumber] = chunk
    chunkNumber += 1
    chunk = image.read(bufferSize-3)
# close image file
image.close()
print(chunkNumber)

total_transmissions = 0
total_retransmissions = 0
total_size = 0
start_time = time.time()
# send chunks to reciever
for chunk in chunks:
    # time.sleep(0.01)
    # Send to server using created UDP socket
    chunk_number = chunk.to_bytes(2, byteorder='big')
    last_file_chunk = False
    if chunk == chunkNumber-1:
        last_file_chunk = True
    last_file_chunk = last_file_chunk.to_bytes(1, byteorder='big')
    
    #combine chunk number and chunk data
    chunk_data = chunk_number + last_file_chunk + chunks[chunk]
    message = chunk_data
    total_size += len(message)#sys.getsizeof(message)

    isACK = False
    socket_udp.sendto(message, recieverAddressPort)
    total_transmissions += 1
    print("Message sent successfully..... {}".format(chunk) )
    while isACK == False:
        try:
            recievedMessage, senderAddress = socket_udp.recvfrom(bufferSize)
            print("Message from Server: {}".format(recievedMessage))
            print("Server IP Address: {}".format(senderAddress))
            isACK = True
        except socket.timeout:
            print("Timeout occured, sending again")
            socket_udp.sendto(message, recieverAddressPort)
            total_retransmissions += 1
            total_transmissions += 1

# send empty chunk to indicate end of file
socket_udp.sendto(b'', recieverAddressPort)    
socket_udp.close()

end_time = time.time()
total_size = os.path.getsize("testFile.jpg")
print("Total transmissions: {}".format(total_transmissions))
print("Total retransmissions: {}".format(total_retransmissions))
print("Average retransmissions per transmission: {}".format(total_retransmissions/total_transmissions))
#average throughput in kilobytes per second
print("Average throughput: {}".format(total_size/(end_time-start_time)/1024))
print("Average Throughput: {}".format(total_size/(end_time-start_time)))

# output the results in a file
with open("output2.txt", "a") as f:
    f.write("{}:{}:{}\n".format(TIMEOUTTIME * 1000, total_retransmissions, total_size/(end_time-start_time)))
#close the file
f.close()


# import socket
# import time

# senderIP = "10.0.0.1"
# senderPort   = 20001
# recieverAddressPort = ("10.0.0.2", 20002)
# bufferSize  = 1024 #Message Buffer Size

# # Create a UDP socket at reciever side
# socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# socket_udp.settimeout(1) # value in seconds

# # open image file
# image = open("testFile (1).jpg", "rb")

# # read image file in chunks
# chunk = image.read(bufferSize)

# # store chunks in a dictionary
# chunks = {}
# chunkNumber = 0
# while chunk:
#     chunks[chunkNumber] = chunk
#     chunkNumber += 1
#     chunk = image.read(bufferSize)

# # close image file
# image.close()

# while True:

#     time.sleep(0.01)
#     # Send to server using created UDP socket
#     msg = input("Please enter message to send: ")
#     if msg == "q":
#         break
#     message = str.encode(msg)
#     isACK = False
#     socket_udp.sendto(message, recieverAddressPort)
#     print("Message sent successfully....." )
#     while isACK == False:
#         try:
#             recievedMessage, senderAddress = socket_udp.recvfrom(bufferSize)
#             print("Message from Server:{}".format(recievedMessage))
#             print("Server IP Address:{}".format(senderAddress))
#             isACK = True
#         except socket.timeout:
#             print("Timeout occured, sending again")
#             socket_udp.sendto(message, recieverAddressPort)
#     # #wait for reply message from reciever
#     # msgFromServer = socket_udp.recvfrom(bufferSize)

#     # msgString = "Message from Server {}".format(msgFromServer[0])
#     # print(msgString)

# socket_udp.close()
