import sys, socket, binascii
#Temporary debug args
sys.argv = ["packet_sender.py", "192.168.0.3", "COLOMBIA 2 - MESSI 0"]


def ipToHex(ipAddress):
        return binascii.hexlify(socket.inet_aton(ipAddress)).decode('utf-8')

#TODO
def calculateChecksum(packet):
        return

serverIP = ipToHex(sys.argv[1])
sourceIP = ipToHex(socket.gethostbyname(socket.gethostname()))

payload = sys.argv[2].encode('utf-8').hex()

#temporary
checksum = '0000'

headerLength = (len('4500') + 4 + len('1c4640004006') 
	+ len(checksum) + len(sourceIP) + len(serverIP) + len(payload)) // 2
headerLength = hex(headerLength)[2:]

if len(headerLength) == 2:
	headerLength = '00' + headerLength


packet = '4500' + headerLength + '1c4640004006' + checksum + sourceIP + serverIP + payload
#padding
while (len(packet) % 8 != 0):
        packet = packet + '0'
#TODO: compute checksum
#TODO: send packet to server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#commenting this out until we get a server. Running it will keep the script hanging on this command
#s.connect((server, 1234))
