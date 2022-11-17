import socket
import time
import sys
from _thread import *
import threading
senderIP = "10.0.0.1"
senderPort   = 20001
recieverAddressPort = ("10.0.0.2", 20002)
bufferSize  = 1024 #Message Buffer Size

# Create a UDP socket at reciever side
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
TIMEOUT = 10/1000
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

WINDOWS_SIZE = 256
base = 0
nextSeqNum = 0
mutex_lock = threading.Lock()
total_size = 0
total_transmissions = 0

def send_func():
    global base
    global nextSeqNum
    global chunks
    global chunkNumber
    global mutex_lock
    global total_size
    global total_transmissions
    start_new_thread(receive_func, ())
    while base < chunkNumber:
        mutex_lock.acquire()
        while nextSeqNum < base + WINDOWS_SIZE and nextSeqNum < chunkNumber:
            chunk = chunks[nextSeqNum]
            last_file_chunk = False
            if nextSeqNum == chunkNumber-1:
                last_file_chunk = True
            chunk = nextSeqNum.to_bytes(2, byteorder='big') + last_file_chunk.to_bytes(1, byteorder='big') + chunk
            socket_udp.sendto(chunk, recieverAddressPort)
            print("Message sent successfully..... {}".format(nextSeqNum))
            nextSeqNum += 1
            total_size += len(chunk)
            total_transmissions += 1
        mutex_lock.release()
    print("Here now")
    # send an empty chunk to indicate end of file
    socket_udp.sendto(b'', recieverAddressPort)
    print("EOF")


def receive_func():
    global base
    global chunks
    global chunkNumber
    global nextSeqNum
    global mutex_lock
    while base < chunkNumber:
        try:
            recievedMessage, senderAddress = socket_udp.recvfrom(bufferSize)
            mutex_lock.acquire()
            recievedMessage = int(recievedMessage.decode())
            if recievedMessage != base:
                mutex_lock.release()
                raise socket.timeout
            print("Message from Server: {}".format(recievedMessage))
            base = recievedMessage + 1
            mutex_lock.release()
        except socket.timeout:
            mutex_lock.acquire()
            print("Timeout occured, sending again: ", base, nextSeqNum)
            nextSeqNum = base
            mutex_lock.release()

def main():
    send_thread = threading.Thread(target=send_func)
    # receive_thread = threading.Thread(target=receive_func)
    send_thread.start()
    # receive_thread.start()
    send_thread.join()
    # receive_thread.join()


if __name__ == "__main__":
    main()
    # close the socket
    socket_udp.close()
# try:
#     while base < chunkNumber:
#         while nextSeqNum < base + WINDOWS_SIZE and nextSeqNum < chunkNumber:
#             # send chunk
#             chunk = chunks[nextSeqNum]
#             # add sequence number to chunk
#             # chunk =  + chunk
#             # add checksum to chunk
#             # checksum = sum(chunk)
#             # chunk = chunk + checksum.to_bytes(1, byteorder='big')
#             last_file_chunk = False
#             if base == chunkNumber-1:
#                 last_file_chunk = True
#             thread = threading.Thread(target=send_func, args=(chunk, last_file_chunk))
#             thread.start()
#             thread_array.append(thread)
        
        
#         #     # send chunk to reciever
#         #     last_file_chunk = last_file_chunk.to_bytes(1, byteorder='big')
#         #     chunk = nextSeqNum.to_bytes(2, byteorder='big') + last_file_chunk + chunk
#         #     socket_udp.sendto(chunk, recieverAddressPort)
#         #     print("Sending chunk number: ", nextSeqNum)
#         #     nextSeqNum += 1
#         # try:
#         #     # recieve ack
#         #     ack, address = socket_udp.recvfrom(bufferSize)
#         #     ack = int.from_bytes(ack, byteorder='big')
#         #     print("Recieved ack for chunk number: ", ack)
#         #     base = ack + 1
#         # except socket.timeout:
#         #     print("Timeout occured")
#         #     nextSeqNum = base
# except socket.error as e:
#     print("Error occured: ", e)
# finally:
#     for t in thread_array:
#         t.join()








