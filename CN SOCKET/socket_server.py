from socket import *

mDatabase = {
             "01":"Name: x, Maths : 99, Physics : 92, Chemistry : 95",
             "02":"Name: y, Maths : 91, Physics : 93, Chemistry : 91",
             "03":"Name: z, Maths : 97, Physics : 95, Chemistry : 99"
             }
serverPort = 9000

serverSocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print("server is up and waiting for query...")

while True:
    query, clientAddress = serverSocket.recvfrom(2048)
    query = query.decode('utf-8')
    
    print("Received the query from client for enrol no = {}".format(query))
    
    res = mDatabase.get(str(query),"The student data is not present in database ...")
    res = res.encode('utf-8')
    
    print("Sending the result to client..")
    serverSocket.sendto(res,clientAddress)