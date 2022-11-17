import socket
import time
import sys
senderIP = "10.0.0.1"
senderPort   = 20001
recieverAddressPort = ("10.0.0.2", 20002)
bufferSize  = 1024 #Message Buffer Size

# Create a UDP socket at reciever side
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
TIMEOUT = 1/1000
socket_udp.settimeout(TIMEOUT) # value in seconds

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


# Implement Go Back N protocol
# send chunks in chunks dictionary

WINDOWS_SIZE = 2
base = 0
nextSeqNum = 0
while base < chunkNumber:
    while nextSeqNum < base + WINDOWS_SIZE and nextSeqNum < chunkNumber:
        # send chunk
        chunk = chunks[nextSeqNum]
        # add sequence number to chunk
        # chunk =  + chunk
        # add checksum to chunk
        # checksum = sum(chunk)
        # chunk = chunk + checksum.to_bytes(1, byteorder='big')
        last_file_chunk = False
        if base == chunkNumber-1:
            last_file_chunk = True
        # send chunk to reciever
        last_file_chunk = last_file_chunk.to_bytes(1, byteorder='big')
        chunk = nextSeqNum.to_bytes(2, byteorder='big') + last_file_chunk + chunk
        socket_udp.sendto(chunk, recieverAddressPort)
        print("Sending chunk number: ", nextSeqNum)
        nextSeqNum += 1
    try:
        # recieve ack
        ack, address = socket_udp.recvfrom(bufferSize)
        ack = int.from_bytes(ack, byteorder='big')
        print("Recieved ack for chunk number: ", ack)
        base = ack + 1
    except socket.timeout:
        print("Timeout occured")
        nextSeqNum = base

# close the socket
socket_udp.close()



# import socket
# import time
# import sys
# senderIP = "10.0.0.1"
# senderPort   = 20001
# recieverAddressPort = ("10.0.0.2", 20002)
# bufferSize  = 1024 #Message Buffer Size

# # Create a UDP socket at reciever side
# socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# socket_udp.settimeout(1) # value in seconds

# # open image file
# image = open("testFile.jpg", "rb")
# # read image file in chunks
# chunk = image.read(bufferSize-3)
# # store chunks in a dictionary
# chunks = {}
# chunkNumber = 0
# while chunk:
#     chunks[chunkNumber] = chunk
#     chunkNumber += 1
#     chunk = image.read(bufferSize-3)
# # close image file
# image.close()
# print(chunkNumber)

# total_transmissions = 0
# total_retransmissions = 0
# total_size = 0
# start_time = time.time()
# # send chunks to reciever
# for chunk in chunks:
#     # time.sleep(0.01)
#     # Send to server using created UDP socket
#     chunk_number = chunk.to_bytes(2, byteorder='big')
#     last_file_chunk = False
#     if chunk == chunkNumber-1:
#         last_file_chunk = True
#     last_file_chunk = last_file_chunk.to_bytes(1, byteorder='big')
    
#     #combine chunk number and chunk data
#     chunk_data = chunk_number + last_file_chunk + chunks[chunk]
#     message = chunk_data
#     total_size += sys.getsizeof(message)

#     isACK = False
#     socket_udp.sendto(message, recieverAddressPort)
#     total_transmissions += 1
#     print("Message sent successfully..... {}".format(chunk) )
#     while isACK == False:
#         try:
#             recievedMessage, senderAddress = socket_udp.recvfrom(bufferSize)
#             print("Message from Server: {}".format(recievedMessage))
#             print("Server IP Address: {}".format(senderAddress))
#             isACK = True
#         except socket.timeout:
#             print("Timeout occured, sending again")
#             socket_udp.sendto(message, recieverAddressPort)
#             total_retransmissions += 1
#             total_transmissions += 1
    
# socket_udp.close()

# end_time = time.time()
# print("Total transmissions: {}".format(total_transmissions))
# print("Total retransmissions: {}".format(total_retransmissions))
# print("Average retransmissions per transmission: {}".format(total_retransmissions/total_transmissions))
# #average throughput in kilobytes per second
# print("Average throughput: {}".format(total_size/(end_time-start_time)/1024))
# print("Average Throughput: {}".format(total_size/(end_time-start_time)))
