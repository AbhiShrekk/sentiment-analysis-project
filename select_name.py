import sqlite3
from tkinter import *

user_root=Tk()

db=sqlite3.connect("xyz.db")
cur=db.cursor()

list_of_user_names=[]

def create_table():
    cur.execute("drop table if exists users")
    cur.execute("create table users (name char(20), pwd char(20))")
    cur.execute("insert into users values ('a','a')")
    cur.execute("insert into users values ('b','b')")
    cur.execute("insert into users values ('c','c')")

def authenticate():
    name_entrybox=nameentry.get()
    result=cur.execute("select * from users")
    for row in result:
        x=row[0]
        list_of_user_names.append(x)
    if name_entrybox in list_of_user_names:
        print('You are one of the valid users')
    else:
        print('Your username is not valid')

create_table()

namelabel=Label(user_root,text='name: ')
namelabel.grid(row=0,column=0)
nameentry=Entry(user_root)
nameentry.grid(row=0,column=1)
verifybtn=Button(user_root,text="Verify",command=authenticate)
verifybtn.grid(row=1,column=0)

user_root.mainloop()