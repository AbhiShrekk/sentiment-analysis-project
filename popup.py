# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 19:34:18 2018

@author: Hp
"""

from tkinter import *
 
popup=Tk()
popup.rowconfigure(0,weight=1)
popup.rowconfigure(1,weight=1)
popup.rowconfigure(2,weight=1)
popup.columnconfigure(0,weight=1)
popup.columnconfigure(1,weight=1)
popup.columnconfigure(2,weight=1)
# x is the word whose polarity is not known
x="word"
labeltext=Label(popup,text="What is the polarity of the following word")
labeltext.grid(row=0,column=0)
word=Label(popup,text=x)
word.grid(row=1,column=0)
polarityentry=Entry(popup)
polarityentry.grid(row=1,column=2)
submit=Button(popup,text="Submit")
submit.grid(row=2,column=1)

popup.mainloop()