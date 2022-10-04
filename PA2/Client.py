# Crystian Chavez, Christian Rodriguez, Emmanuel Salcedo, Ranjita Summan
# PA2_<client/server>_ Chavez_Rodriguez_Salcedo_Summan.py
# Group Programming Assignment 2

import time
from socket import *

# typical values for RTT
alpha = 0.125
beta = 0.25
estimatedRTT = 0
averageRTT = 0

# initalize varibale for Sucessful Packets
packetsReceived=0
server=''
port=12000
 #total number of pings
pings=10

# Create a UDP client
# Notice the use of SOCK_DGRAM for UDP packets
# Setting up a socket for later use
clientSocket = socket(AF_INET, SOCK_DGRAM)

# sets timeout to 1 sec
clientSocket.settimeout(1)


for i in range(pings):
    # creates message to send to server
    message = 'Ping' + str(i+1)
    # try block for ping
    try:
        #Record Start time
        startTime = time.time()

        # send packet to server
        clientSocket.sendto(message.encode(), (server, port))
        print("Mesg sent: " + message)

        #recieve Sucessful packet, print recived message and increase packet counter
        messageReceived, address = clientSocket.recvfrom(1024)
        print("Mesg rcvd: " + messageReceived.decode())
        packetsReceived+=1

        # Stop time and Calculate RTT (*1000 to convert to ms)
        endTime = time.time()
        rtt = (endTime - startTime) * 1000

        #first packet recived store value for calculations
        if(i==0):
            minRTT = rtt
            maxRTT = rtt
            averageRTT = rtt
            estimatedRTT = rtt
            devRTT = rtt / 2
        else:
            #compute avgRTT, EstRTT, DevRTT
            averageRTT += rtt
            estimatedRTT = (1 - alpha) * estimatedRTT + (alpha * rtt)
            devRTT = (1 - beta) * devRTT + beta * abs(rtt - estimatedRTT)

        #check for min and max RTT
        if (maxRTT < rtt):
            maxRTT = rtt
        if (minRTT > rtt):
            minRTT = rtt

        #print start and end time and Packet message
        print('Start time: ' + str(format(startTime, 'e')))
        print('Return Time: ' + str(format(endTime, 'e')))
        print ('PONG '+ str(i+1) + ' RTT :' + str(rtt) + ' ms\n')

    #except for failure to recive packet message
    except timeout:
        print('No Mesg rcvd')
        print('PONG '+ str(i+1) + ' Request Timed Out\n')

# Calculate timeout interval and missing packets
timeoutInterval = estimatedRTT + (4 * devRTT)
packetsMissed = pings - packetsReceived

# Print values
print('Min RTT:\t' + str(minRTT) + ' ms')
print('Max RTT:\t' + str(maxRTT) + ' ms')
#calculate and print avgRTT
print('Avg RTT:\t' + str(averageRTT / packetsReceived) + ' ms')
#calculate Packets Lost
print('Packet Loss:\t' + str((packetsMissed / pings) * 100) + '%')
print('Estimated RTT:\t' + str(estimatedRTT) + ' ms')
print('Dev RTT:\t' + str(devRTT) + ' ms')
print('Timeout Interval:' + str(timeoutInterval) + ' ms')
