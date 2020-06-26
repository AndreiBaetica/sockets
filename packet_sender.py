import sys, socket,binascii
#Temporary debug args
sys.argv = ["packet_sender.py", "192.168.0.3", "COLOMBIA 2 - MESSI 0"]

serverIP = sys.argv[1]
payload = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#commenting this out until we get a server. Running it will keep the script hanging on this command
#s.connect((server, 1234))

payload = payload.encode('utf-8').hex()

sourceIP = socket.gethostbyname(socket.gethostname()).encode('utf-8')
#TODO: translate source and server ip addresses to hex

#temporary
checksum = '0000'

headerLength = (len('4500') + 4 + len('1c4640004006') 
	+ len(checksum) + len(sourceIP) + len(serverIP) + len(payload)) // 2
headerLength = hex(headerLength)[2:]

if len(headerLength) == 2:
	headerLength = '00' + headerLength


#TODO: compute checksum
packetNoChecksum = '4500' + headerLength + '1c4640004006' + checksum + sourceIP + serverIP + payload


#TODO: send packet to server
