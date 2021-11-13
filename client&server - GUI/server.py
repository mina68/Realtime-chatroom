# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:34:59 2019

@author: Mina
"""

from socket import *
from _thread import *
from tkinter import *

s = socket((AF_INET), SOCK_STREAM)
host = "127.0.0.1"
port = 7777
s.bind((host, port))
s.listen(50)

window = Tk()
window.title("chat client")
window.geometry("400x400")

label = Label(window)
label.grid(row=3, column=3)

entry = Entry(window, width="40")
entry.grid(row=1, column=3)

sessions = []

def clicked():
    message = "server : " + entry.get()
    for session in sessions:
        session.send(message.encode('utf-8'))
    entry.delete(0, END)

btn = Button(window,text="Send",bg="green",fg="white",width=8,height=1, command=clicked)
btn.grid(row=1, column=4)
    
def recvThread (c, ad):
    while True:
        label["text"] = str(ad[1]) + " : " + c.recv(1048).decode('utf-8')
       
def mainThread(s):
    while True:
        c, ad = s.accept()
        sessions.append(c)
        label["text"] = "new connection from " + str(ad[1])
        start_new_thread(recvThread, (c, ad))
        
start_new_thread(mainThread, (s,))
 
window.mainloop()