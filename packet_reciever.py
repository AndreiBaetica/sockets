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

servadd = (socket.gethostbyname(socket.gethostname()), 1234)
print(socket.gethostbyname(socket.gethostname()))
print('starting up on %s port %s' %servadd)
s.bind(servadd)
s.listen(1)

while True:
    print('waiting for a connection')
    connection, cadd = s.accept()

    try:
        print( 'connection from:', cadd)

        while True:
            data = connection.recv(100)
            data2 = binascii.unhexlify(data)
            print ('received as: ' , data)
            print ('converted into: ' , data2)

            if data:
                print('sending data back to client')
                connection.sendall(data2)
            else:
                print('no more data from ', cadd)
                break

    finally:
        connection.close()
