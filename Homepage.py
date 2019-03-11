from tkinter import *
import sqlite3

root=Tk()
root.minsize(300,300)
mydb=sqlite3.connect("users.db")
cur=mydb.cursor()


def newroot2():
    pass

def authenticate():
    pwdfromdb=""
    name=nameentry.get()
    pwd=pwdentry.get()
    result=cur.execute("select pwd from users where name='%s'"%(name))
    for row in result:
        pwdfromdb=row[0]
    if pwd==pwdfromdb:
        print("Valid user!")
        option_window()
    else:
        print("Invalid user!")
        

def option_window():
    root2=Tk()
    root.destroy()
    root2.minsize(500,500)
    root2.columnconfigure(0,weight=1)
    root2.columnconfigure(1,weight=1)
    root2.columnconfigure(2,weight=1)
    root2.rowconfigure(0,weight=1)
    root2.rowconfigure(1,weight=1)
    def singlesentence():
        def analyse():
            pass
        root3=Tk()
        root2.destroy()
        root3.minsize(500,500)
        root3.rowconfigure(0,weight=1)
        root3.rowconfigure(1,weight=1)
        root3.columnconfigure(0,weight=1)
        root3.columnconfigure(1,weight=1)
        root3.columnconfigure(2,weight=1)
        inputlabel=Label(root3,text="Input Entry: ")
        inputlabel.grid(row=0,column=0)
        inputEntry=Entry(root3)
        inputEntry.grid(row=0,column=2)
        autbtn=Button(root3,text="Analyse",command=analyse)
        autbtn.grid(row=1,column=1)
        
        
        autbtn.grid(row=1,column=1)
        root3.mainloop()
    
    def multisentence():
        root3=Tk()
        root2.destroy()
        root3.minsize(500,500)
        root3.rowconfigure(0,weight=1)
        root3.rowconfigure(1,weight=1)
        root3.columnconfigure(0,weight=1)
        root3.columnconfigure(1,weight=1)
        listOfSentences=[]
        def input_multiple_sentences():
            noOfSent=1
            noOfSent=nentry.get()
            root4=Tk()
            root3.destroy()
            textbox4=Entry(root4)
            nextbtn=Button(root4,text="next",command=destroytemp)
            def temp():
                for i in range(0,int(noOfSent)):
                    textbox4.grid(row=0,column=0)
                    
                    nextbtn.grid(row=1,column=0)
            
            def destroytemp():
                        koibhi=text4.get()
                        listOfSentences.append(koibhi)
                        textbox4.destroy()
                        nextbtn.destroy()
                        
            temp()        
                        
            root4.mainloop()    
            
            
        numberofsentencelabel=Label(root3,text="Enter the number of sentences you wish to analyze: ")
        numberofsentencelabel.grid(row=0,column=0)
        nentry=Entry(root3)
        nentry.grid(row=0,column=2)
        submitbtn=Button(root3,text="submit",command=input_multiple_sentences)
        submitbtn.grid(row=1,column=1)
        root3.mainloop()
        
        
        
    titlelabel=Label(root2,text="Sentiment Analyzer")
    titlelabel.grid(row=0,column=1)
    singlesentence=Button(root2,text="Single sentence analysis",command=singlesentence)
    singlesentence.grid(row=1,column=0)
    multisentence=Button(root2,text="Multi sentence analysis",command=multisentence)
    multisentence.grid(row=1,column=2)
      
    
        
        
    root2.mainloop()

    
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)

namelabel=Label(root,text="Name : ")
namelabel.grid(row=0,column=0)
nameentry=Entry(root)
nameentry.grid(row=0,column=1)
pwdlabel=Label(root,text="Password : ")
pwdlabel.grid(row=1,column=0)
pwdentry=Entry(root,show="*")
pwdentry.grid(row=1,column=1)
authenticatebtn=Button(root,text="Authenticate",command=authenticate)
authenticatebtn.grid(row=2,column=0)
root.mainloop()