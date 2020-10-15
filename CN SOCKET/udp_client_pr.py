from socket import *


serverName  = '127.0.0.1'
serverPort = 4000

clientSocket = socket(AF_INET,SOCK_DGRAM)    #udp 

query = input("Enter your Employee id\t")
query = query.encode('utf-8')

print("Sending the data to server ...\n")
clientSocket.sendto(query,(serverName,serverPort))


result, serverAddress =  clientSocket.recvfrom(2048)
result = result.decode('utf-8')

print("Received the data from server.....\n result => \n{}".format(result))


clientSocket.close()
