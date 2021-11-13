# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:34:59 2019

@author: Mina
"""

from socket import *
from _thread import *

s = socket((AF_INET), SOCK_STREAM)
host = "127.0.0.1"
port = 7777
s.bind((host, port))
s.listen(50)

sessions = []
    
def recvThread (c, ad):
    while True:
        message = str(ad[1]) + " : " + c.recv(1048).decode('utf-8')
        for session in sessions:
            if session != c:
                session.send(message.encode('utf-8'))
        
while True:
    c, ad = s.accept()
    message = "new connection from " + str(ad[1]) ;
    for session in sessions:
        session.send(message.encode('utf-8'))
    sessions.append(c)
    start_new_thread(recvThread, (c, ad))
 
    