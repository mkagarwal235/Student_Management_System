from tkinter import *
import os
import tkinter.messagebox as tmsg
from marksheet import searchRoll,result_search_marksheet
def search():
    if len(roll.get())!=0:
        row=searchRoll(roll.get())
        result_search_marksheet(row)
    else:
        tmsg.showerror("Attention","Please Enter valid Roll number")

def new():
    filename='marksheet.py'
    os.system(filename)
    os.system('notepad'+filename)

root=Tk()
root.title("Search Info")
root.geometry("500x400+500+100")
root.maxsize(500,400)
root.config(bg="green")


roll=StringVar()

frame1=Frame(root,bd=5,relief=GROOVE,bg="green")
frame1.place(x=30,y=150,width=400,height=120)
rollL=Label(frame1,text="Roll Number",font="lucida 15 bold",bg="green")
rollL.place(x=20,y=20)
rollE=Entry(frame1,font="lucida 15 bold",textvariable=roll)
rollE.place(x=150,y=20)

searchbtn=Button(frame1,text='Search',font='lucida 10 bold',width=10,command=search,bg="green")
searchbtn.place(x=20,y=70)

createbtn=Button(frame1,text='Create New',font='lucida 10 bold',width=10,command=new,bg="green")
createbtn.place(x=200,y=70)
root.mainloop()