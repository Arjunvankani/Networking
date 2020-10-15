from socket import *

#ip address or url like www.google.com
serverName  = '127.0.0.1'
serverPort = 1234

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


query = input("Enter your Enrollment no : \t")
query = query.encode('utf-8')

print("Sending query..")
clientSocket.send(query)


result  =  clientSocket.recv(2048)
result = result.decode('utf-8')

print("Received the data from server.....\n result = {}".format(result))


clientSocket.close()
