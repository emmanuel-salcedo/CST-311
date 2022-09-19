# CST311-PA1
- [Instructions](#instructions)
- [Grading Objectives](#grading-objectives)
- [What to Hand in](#what-to-hand-in)
- [Optional Extra-credit Exercises](#optional-extra-credit-exercises)
## Programming Assignment 1 

*CST 311, Introduction to Computer Networks*

**READ INSTRUCTIONS CAREFULLY BEFORE YOU START THE ASSIGNMENT.**
This programming assignment is due at 11:59 pm on the due date.

Assignment must be submitted electronically to Canvas before the due date and time . Late assignments have a 15% penalty per day and will not be accepted after 2 days late.

Use the Teams on the Team Assignment Document.  This first assignment is a warmup. Select your Team leader and divide up work per the Programming Process instructions. 

## Instructions: ##
In this assignment, you will learn the basics of socket programming for UDP and TCP in Python. 

You will learn how to send and receive datagram packets using UDP sockets and TCP sockets. Throughout the assignment, you will gain familiarity with a Client Server architecture.  **You will use Python 3 for your programming language.**

This assignment basically requires you to submit the Python client and server code for the UDP socket programming example in Section 2.7.1 and then also the TCP socket programming example in Section 2.7.2. (Note that these examples are written in Python 2.  You will have to modify a few lines of code to convert to Python 3.)  You should each try to do this on your own first but you will then work with your assigned team for this assignment. Split up your team to have one group do the UDP example together and another group to do the TCP example. The goal of this assignment is a) to learn about how UDP and TCP works and how to program with UDP and TCP and also b) to make sure your computer is set up and working, ready for the next assignment where you will be writing your own code. You are welcome to use whatever IDE the team prefers; for this assignment with about 10 lines of code, you may prefer to simply use an editor but this is up to you. Code it, test it with the following cases:  

    abcdef abc123def  
    ABcdEF  
    AB12cdEF  
    Two Words HERE !!  

This assignment is worth 100 points. The grading objectives for the assignment are given below. 

## Grading Objectives ##
For TCP and for UDP each: (30 + 30 = 60 points)
    (5 points) Socket set up correctly on server 
    (5 points) Socket set up correctly on client 
    (5 points) Server waits for input 
    (5 points) Client sends message to server
    (5 points) Server takes input and changes it to all CAPS
    (5 points) Client receives and prints out the modified message.
    
(10 points) All screenshots in one pdf file. Meeting Minutes in one other pdf file.
    
Teamwork grade (30 points): Each team member will evaluate other teammates on the scale of 1 to 4 by submitting a [peer evaluation form](https://forms.gle/CAYZjPi2Sfb8hers6). Your rating will be the average of all ratings from your teammates and converted to your teamwork grade as follows:

Teamwork grade = Max teamwork grade if 3 <= Rating <=  4
                 Max teamwork grade x Rating/3 otherwise
                 
## What to Hand in ##

**Since the code is already given, you need not submit python files for this assignment.**

Your team lead will hand in the following: 

1. Screenshots of the working UDP and TCP client/server programs for all test cases given above. All screenshots must be in one pdf file.
2. Meeting Minutes including: Team Lead name, attendance, work division narrative. Here are the recommended Meeting Minutes [template](https://docs.google.com/document/d/1V89On3pIGiXsV01vON6VP87bVrg28iyL/edit?usp=sharing&ouid=118002461567495079155&rtpof=true&sd=true) and [example](https://docs.google.com/document/d/1V89On3pIGiXsV01vON6VP87bVrg28iyL/edit?usp=sharing&ouid=118002461567495079155&rtpof=true&sd=true).  Submit one pdf file containing all Meeting Minutes.

You must also fill in the [peer evaluation form for teamwork rating. In peer evaluation, you evaluate yourself and also your team members. If you do not fill in the peer evaluation form, you will get rating 1 automatically.


## Optional Extra-credit Exercises ##
(15 Extra Credit points) If you have time, try to do this in the mininet virtual machine. Submit screenshots of TCP and UDP client/server programs running some test cases on the mininet emulated hosts h1 and h2.

You must submit extra credit work to a separate portal on Canvas. Since this part is extra credit, everyone in the team may not choose to work on it. Submit a separate pdf for the extra credit with the names of the team members who did work on the extra credit sections. 

*Note: The Extra Credit for PA #1 is not due until the end of Week 2.*


 
 


