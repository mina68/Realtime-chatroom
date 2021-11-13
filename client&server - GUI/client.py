# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 02:21:21 2019

@author: Mina
"""

from socket import *
from _thread import *
from tkinter import *

s = socket((AF_INET), SOCK_STREAM)
host = "127.0.0.1"
port = 7777
s.connect((host, port))

window = Tk()
window.title("chat client")
window.geometry("400x400")

label = Label(window)
label.grid(row=3, column=3)

entry = Entry(window, width="40")
entry.grid(row=1, column=3)

def clicked():
    message = entry.get()
    s.send(message.encode('utf-8'))
    entry.delete(0, END)

btn = Button(window,text="Send",bg="green",fg="white",width=8,height=1, command=clicked)
btn.grid(row=1, column=4)
    
def recvThread (s):
    while True:
        label['text'] += "\n" + s.recv(1024).decode('utf-8')
    
start_new_thread(recvThread, (s,))
        
window.mainloop()
        