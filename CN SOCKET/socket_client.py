from socket import *

#ip address or url like www.google.com
serverName  = '127.0.0.1'
serverPort = 9000

clientSocket = socket(AF_INET,SOCK_DGRAM)   #udp SOCK_DGRAM     tcp SOCK_STREAM

query = input("Enter your Enrollment no :")
query = query.encode('utf-8')

print("Sending the data to server ...")
clientSocket.sendto(query,(serverName,serverPort))


result, serverAddress =  clientSocket.recvfrom(2048)
result = result.decode('utf-8')

print("Received the data from server.....\n result = {}".format(result))


clientSocket.close()