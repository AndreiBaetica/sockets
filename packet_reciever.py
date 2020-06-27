import binascii, socket
#debug packet
packet = '450000141c46400040066549c0a83801c0a80003434f4c4f4d4249412032202d204d455353492030'

def decodeChecksum(packet):
    header = packet[0:40]
    headerSplit = [header[i:i+4] for i in range(0, len(header), 4)]
    hexList = []
    for i in headerSplit:
        hexList.append(int(i, 16))
    result = hex(sum(hexList))[2:]
    #halde the carry
    while len(result) != 4:
        while len(result) % 4 != 0:
            result = '0' + result
        resultSplit = [result[i:i+4] for i in range(0, len(result), 4)]
        hexList = []
        for i in resultSplit:
            hexList.append(int(i, 16))
        result = hex(sum(hexList))[2:]
    return result == 'ffff'

def decodePayload(packet):
    payload = packet[40:]
    return str(binascii.unhexlify(payload))[2:len(str(binascii.unhexlify(payload)))-1]
    


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
print(f"Starting server on {socket.gethostname()}.")
s.listen(5)

clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")
clientsocket.send(bytes('Connected to server.', 'utf-8'))
    
msg = clientsocket.recv(1024)
packet = msg.decode('utf-8')

if decodeChecksum(packet):
    print("Data received: " + decodePayload(packet))
    clientsocket.send(bytes('Data successfully recieved by server.', 'utf-8'))
else:
    print("Checksum validation failed!")
    clientsocket.send(bytes('Checksum validation failed!', 'utf-8'))
