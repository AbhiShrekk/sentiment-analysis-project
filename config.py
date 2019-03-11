# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:25:54 2018

@author: Hp
"""


import sqlite3
db=sqlite3.connect("users.db")
cur=db.cursor()


#mydb1.execute("create table Users( name char(20), pwd char(20))")
#db.execute("insert into Users values ('Abhishek', 'N036')")
#db.execute("insert into Users values ('Avnish', 'N046')")
#db.execute("insert into Users values ('a', 'a')")
d#b.commit()
result=db.execute("select name,pwd from Users")
for row in result:
    print('HI')
    print(row[0])
    print(row[1])
db.close()
print('executed')