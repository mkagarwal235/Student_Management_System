from tkinter import *
import os
import time
def myclock():
    c_time=time.strftime("%H:%M:%S")
    clock.config(text=c_time)
    clock.after(60,myclock)
def student_profile():
    filename='std.py'
    os.system(filename)
    os.system('notepad'+filename)

def fee_report():
    filename = 'fee.py'
    os.system(filename)
    os.system('notepad' + filename)


def library():
    filename = 'library.py'
    os.system(filename)
    os.system('notepad' + filename)


def marksheet():
    filename = 'search.py'
    os.system(filename)
    os.system('notepad' + filename)
root=Tk()
root.title("Menu")
root.config(bg="lightblue")
root.geometry('800x400+0+0')
root.maxsize(800,400)

menuL=Label(root,text="Menu",font="lucida	30	bold",bd=5,relief=SUNKEN,fg="black",width=10,bg="lightblue")
menuL.place(x=280,y=30)

clock=Label(root,font="lucida	15	bold",fg="red",bg="lightblue")
clock.place(x=50,y=20)

stdframe=Frame(root,bd=5,relief=SUNKEN,bg="lightblue")
stdframe.place(x=240,y=120,width=350,height=35)

stdL=Label(stdframe,text="STUDENT PROFILE",font="lucida 12 bold",bg="lightblue")
stdL.grid(row=0,column=0,padx=10)
stdbtn=Button(stdframe,text="VIEW",width=15,font="lucida 8 bold",command=student_profile)
stdbtn.grid(row=0,column=1,padx=20)

feeframe=Frame(root,bd=5,relief=SUNKEN,bg="lightblue")
feeframe.place(x=240,y=170,width=350,height=35)

feeL=Label(feeframe,text="FEE REPORT",font="lucida 12 bold",bg="lightblue")
feeL.grid(row=0,column=0,padx=10)
feebtn=Button(feeframe,text="VIEW",width=15,font="lucida 8 bold",command=fee_report)
feebtn.grid(row=0,column=1,padx=70)

libraryframe=Frame(root,bd=5,relief=SUNKEN,bg="lightblue")
libraryframe.place(x=240,y=220,width=350,height=35)

libraryL=Label(libraryframe,text="LIBRARY SYSTEM",font="lucida 12 bold",bg="lightblue")
libraryL.grid(row=0,column=0,padx=10)
librarybtn=Button(libraryframe,text="VIEW",width=15,font="lucida 8 bold",command=library)
librarybtn.grid(row=0,column=1,padx=40)

marksheetframe=Frame(root,bd=5,relief=SUNKEN,bg="lightblue")
marksheetframe.place(x=240,y=270,width=350,height=35)

marksheetL=Label(marksheetframe,text="MARKSHEET",font="lucida 12 bold",bg="lightblue")
marksheetL.grid(row=0,column=0,padx=10)
marksheetbtn=Button(marksheetframe,text="VIEW",width=15,font="lucida 8 bold",command=marksheet)
marksheetbtn.grid(row=0,column=1,padx=80)
myclock()
root.mainloop()
