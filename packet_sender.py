import sys, socket
#Temporary debug args
sys.argv = ["packet_sender.py", "192.168.0.3", "COLOMBIA 2 - MESSI 0"]

serverIP = sys.argv[1]
payload = sys.argv[2]

print(serverIP)
print(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#commenting this out until we get a server. Running it will keep the script hanging on this command
#s.connect((server, 1234))

payload = payload.encode('utf-8').hex()

print(payload)

sourceIP = socket.gethostbyname(socket.gethostname())
print(sourceIP)
#TODO: translate ip addresses to hex

#temporary
checksum = '0000'

headerLength = (len('4500') + 4 + len('1c4640004006') + len(checksum) + len(sourceIP) + len(serverIP) + len(payload)) // 2
#TODO: convert to hex

#TODO: compute checksum

packet = '4500' + headerLength + '1c4640004006' + checksum + sourceIP + serverIP + payload


#TODO: send packet to server
