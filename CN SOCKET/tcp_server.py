from socket import *

DataEmployy = {
             "101":"Firstname : Ved, Lastname : Shukla , Dep : Mechnical , Experience(years) : 2 ",
             "102":"Firstname : Meet, Lastname : Shah , Dep : IT , Experience(years) : 3.5 ",
             "103":"Firstname : Sujit, Lastname : Maniya , Dep : Computer , Experience(years) : 1.5 ",
             "104":"Firstname : John, Lastname : Patel , Dep : Electrical , Experience(years) : 4 ",
             "105":"Firstname : Kaushal, Lastname : Jani , Dep : Mechnical , Experience(years) : 4.5 "
             }

serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("server is up and waiting for query...")


while True:
    connectionSocket, addr = serverSocket.accept()
    query = connectionSocket.recv(2048)
    query = query.decode('utf-8')
    
    
    print("Received the query from client for enrol no = {}".format(query))
    
    res = DataEmployy.get(str(query),"The student data is not present in database ...")
    res = res.encode('utf-8')
    
    print("Sending the result to client..")
    connectionSocket.send(res)
    connectionSocket.close()
