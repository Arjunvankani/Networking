from socket import *

DataEmployy = {
             "101":"Firstname : Ved, Lastname : Shukla , Dep : Mechnical , Experience(years) : 2 ",
             "102":"Firstname : Meet, Lastname : Shah , Dep : IT , Experience(years) : 3.5 ",
             "103":"Firstname : Sujit, Lastname : Maniya , Dep : Computer , Experience(years) : 1.5 ",
             "104":"Firstname : John, Lastname : Patel , Dep : Electrical , Experience(years) : 4 ",
             "105":"Firstname : Kaushal, Lastname : Jani , Dep : Mechnical , Experience(years) : 4.5 "
             }
serverPort = 4000

serverSocket = socket(AF_INET,SOCK_DGRAM)  # udp

serverSocket.bind(('', serverPort))

print("server is up and waiting for query...\n")

while True:
    query, clientAddress = serverSocket.recvfrom(2048)
    query = query.decode('utf-8')
    
    print("Received the query from client for Employee Id  = \t{}".format(query))
    
    res = DataEmployy.get(str(query),"The Employee data is not present in database ...\n")
    res = res.encode('utf-8')
    
    print("Sending the result to client..\n")
    serverSocket.sendto(res,clientAddress)
