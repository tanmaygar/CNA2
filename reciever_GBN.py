import socket

recieverIP = "10.0.0.2"
recieverPort   = 20002
bufferSize  = 1024 #Message Buffer Size

# bytesToSend = str.encode(msgFromServer)

# Create a UDP socket
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind socket to localIP and localPort
socket_udp.bind((recieverIP, recieverPort))

print("UDP socket created successfully....." )
chunks = {}
chunkNumber = -1
prevChunkNumber = -1
num_duplicate_packet = 0
total_packets_received = 0

while True:

    #wait to recieve message from the server
    bytesAddressPair = socket_udp.recvfrom(bufferSize)
    total_packets_received += 1
    # print(bytesAddressPair) #print recieved message

    #split the recieved tuple into variables
    senderAddress = bytesAddressPair[1]
    recievedMessage = bytesAddressPair[0]
    chunk_number = int.from_bytes(recievedMessage[0:2], byteorder='big')
    chunkNumber = chunk_number
    # prevChunkNumber = chunkNumber
    # if chunk_number == prevChunkNumber:
    #     num_duplicate_packet += 1
    #     print("Duplicate packet recieved")
    #     message = str.encode("Recieved {}".format(chunk_number))
    #     socket_udp.sendto(message, senderAddress)
    #     continue
    last_file_chunk = bool.from_bytes(recievedMessage[2:3], byteorder='big')
    print("Chunk number: {}".format(chunk_number))
    print("Last chunk: {}".format(last_file_chunk))
    chunk_data = recievedMessage[3:]
    chunks[chunkNumber] = chunk_data
    prevChunkNumber = chunkNumber

    

    # #print them just for understanding
    # msgString = "Message from Client:{}".format(recievedMessage)
    # detailString  = "Client IP Address:{}".format(senderAddress)
    # print(msgString)
    # print(detailString)

    # Sending a reply to client

    message = str.encode("{}".format(chunk_number))
    socket_udp.sendto(message, senderAddress)

    if last_file_chunk == True:
        break

# open image file
image = open("received.jpg", "wb")
# read image file in chunks
for chunk in chunks:
    image.write(chunks[chunk])
# close image file
image.close()

print("Image recieved successfully")
print(len(chunks))

print("Total packets recieved: {}".format(total_packets_received))
print("Total duplicate packets recieved: {}".format(num_duplicate_packet))
print("Average packet loss: {}".format(num_duplicate_packet/total_packets_received))

