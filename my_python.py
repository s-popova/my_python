# -*- coding: utf-8 -*-
from tkinter import *
from collections import *
import json


with open ("data_file1.json","tw") as KeK:
    pass

def click_1():
    with open("data_file1.json","a") as w:
        json.dump({entry1.get():{entry2.get():entry3.get()}},w)      
        
    
    
def click_2():
    with open ("data_file1.json") as r:
        rr = json.load(r)
    print(rr)
       
                       
window = Tk()
       
frame = Frame(window).grid() 
first = Label( text='Менеджер задач').grid(row=0, column=1)

label1 = Label(text="задача:").grid(row=1, column=0)
entry1 = Entry(frame)
entry1.grid(row=1, column=1)

entry2 = Entry(frame)
entry2.grid(row=2, column=1)
label2 = Label(text="категория:").grid(row=2, column=0)

entry3 = Entry(frame)
entry3.grid(row=3, column=1)
label3 = Label(text="время:").grid(row=3, column=0)

      
button1 = Button(frame,text='Заказать', command=click_1).grid(row=4, column=1)
button2 = Button(frame,text='Список задач', command=click_2).grid(row=5, column=1)
button3 = Button(frame,text='Выход').grid(row=6, column=1)    
window.mainloop()
