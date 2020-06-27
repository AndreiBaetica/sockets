import sys, socket, binascii
#Temporary debug args
sys.argv = ["packet_sender.py", "192.168.56.1", "COLOMBIA 2 - MESSI 0"]


def ipToHex(ipAddress):
        return binascii.hexlify(socket.inet_aton(ipAddress)).decode('utf-8')

def calculateChecksum(packet):
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
        result = int(hex(65535)[2:], 16) - int(result, 16)
        result = hex(result)[2:]
        return result

def main():
        serverIP = ipToHex(sys.argv[1])
        sourceIP = ipToHex(socket.gethostbyname(socket.gethostname()))

        payload = sys.argv[2].encode('utf-8').hex()

        #temporary
        checksum = '0000'

        headerLength = (len('4500') + 4 + len('1c4640004006') 
                + len(checksum) + len(sourceIP) + len(serverIP)) // 2
        headerLength = hex(headerLength)[2:]

        if len(headerLength) == 2:
                headerLength = '00' + headerLength

        packet = '4500' + headerLength + '1c4640004006' + checksum + sourceIP + serverIP + payload
        #padding
        while (len(packet) % 8 != 0):
                packet = packet + '0'
        
        #omit payload 
        checksum = calculateChecksum('4500' + headerLength + '1c4640004006' + checksum + sourceIP + serverIP)
        
        packet = '4500' + headerLength + '1c4640004006' + checksum + sourceIP + serverIP + payload
        #padding
        while (len(packet) % 8 != 0):
                packet = packet + '0'
        #TODO: send packet to server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #commenting this out until we get a server. Running it will keep the script hanging on this command
        s.connect((serverIP, 1234))

if __name__ == "__main__":
        main()
