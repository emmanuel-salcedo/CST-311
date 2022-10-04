# PA3 Group Assignment
# Christian Rodriguez
# Crystian Chavez
# Ranjita Summan
# Emmanuel Salcedo
# 10/04/22

# The purpose of this assignement is to develop a simple program using sockets
# to acheive communication between two (or more) computer.
# Ctrl + Q, is for commenting and uncommenting after highlighting.

#TCPCapitalizationServer.py
from socket import *
import threading
import time

#Setup threading
totalConnections = 2 #counter for the ammount of connections allowed on serverName
clients =list() # creates list with clients and assignsname
threads = list() # Creates list for threads
messageHistory= list() #list for messages recived
clientDisconnect = [False] * totalConnections #makes list for clients as they need to Disconnect
messageCount = 0 #counts number of messages that have been sent

#Server CRAP
serverPort = 12000
serverHost = "127.0.0.1" #localhost
serverSocket = socket(AF_INET,SOCK_STREAM)

#create thread function to establish new client connection with server
def clientThread(connectionSocket, clientName):
    global messageCount
    global messageHistory

    #Send a "Connected" message to client and decode
    serverMessage = "Client" + clientName + " Connected."
    connectionSocket.send(serverMessage.encode())

    #Recieve message sent from client and decode
    clientMessage = connectionSocket.recv(1024).decode()

    #Update and keep track of messages and clientSocket
    messageCount += 1
    messageHistory.append((messageCount,clientName,clientMessage))
    print("Client "+clientName+" sent message "+ str(messageCount)+ ": "+ clientMessage)

    #update the Client Disconnect list
    for i, disconnectReady in enumerate(clientDisconnect):
        if disconnectReady == False:
            clientDisconnect[i]= True
            break

    #wait until another message is recieved
    while any(disconnectReady == False for disconnectReady in clientDisconnect):
        time.sleep(1)

    #Creates Client message with messages from both clients in order recived and send back to clients
    clientMessage = messageHistory[0][1] +": "+messageHistory[0][2]+ " recieved before " + messageHistory[1][1]+ ": "+ messageHistory[1][2]
    connectionSocket.send(clientMessage.encode())
    connectionSocket.close()


# start server and wait for connections
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)

print("The server is ready to receive " + str(totalConnections) + " connections...\n")

#Find new connections and create a new thread each connection
for i in range(totalConnections):
    connectionSocket, addr = serverSocket.accept()
    clientName = chr(88+i) # will set Clientname to ASCII X or next char Y
    clients.append(clientName)
    print("Accepted connection "+str(i+1)+", calling it client "+clientName)
    currentThread = threading.Thread(target=clientThread, args=(connectionSocket, clientName,))
    threads.append(currentThread)

#start threads
for thread in threads:
    thread.start()

#Server Messages
message = "Waiting to receive messages from "
for i, clientName in enumerate(clients):
    if i == (totalConnections-1):
        message += "Client " + clients[i]
    else:
        message += "Client " + clients[i] +" and "
print(message+"\n")

while any(disconnectReady == False for disconnectReady in clientDisconnect):
    time.sleep(1)

# Wait for threads to terminate
print("\nWaiting a bit for clients to close their connections")
for thread in threads:
    thread.join()

print("Done.")
