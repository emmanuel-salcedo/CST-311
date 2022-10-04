# PA3 Group Assignment
# Christian Rodriguez
# Crystian Chavez
# Ranjita Summan
# Emmanuel Salcedo
# 10/04/22

# The purpose of this assignement is to develop a simple program using sockets
# to acheive communication between two (or more) computer.
# Ctrl + Q, is for commenting and uncommenting after highlighting.

# Step 1: Client X and Y open TCP socket to server
# Step 2: One client sends a message to server follow by the other client.
# The message contains the name of the client followed by a name
# (e.g., “Client X: Alice”, “Client Y: Bob”).

# In your command prompt, type in hostname and press enter.
# What comes up is your computer's hostname

from socket import *
serverName = '127.0.0.1' #Ip of server used in local setup, adjust if server IP diff
serverPort = 12000
timeout_seconds=5

# Creating TCP connection to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(timeout_seconds)
clientSocket.connect((serverName, serverPort))

#Get Message from server
serverMessage = clientSocket.recv(1024)
print('From Server: ' + serverMessage.decode())

#Accepting input for message to send to server
clientMessage = input('Enter message to send to server: ')
clientSocket.send(clientMessage.encode())

#get another message from Server
serverMessage = clientSocket.recv(1024)
print('From Server: ' + serverMessage.decode())

# Close Client Connection
clientSocket.close()
