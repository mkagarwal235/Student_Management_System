from tkinter import *
import tkinter.ttk
import pymysql
import tkinter.messagebox as tmsg
rootL=Tk()
rootL.title("LIBRARY SYSTEM")
rootL.geometry("1200x600+0+0")
rootL.maxsize(1200,600)
rootL.config(bg="yellow")

# ****************** Variables**************************
membertypeV=StringVar()
referenceV=StringVar()
fnameV=StringVar()
lnameV=StringVar()
addressV=StringVar()
postV=StringVar()
mobileV=StringVar()
IdV=StringVar()
titleV=StringVar()
authorV=StringVar()
dateborrowedV=StringVar()
datedueV=StringVar()
dayloanV=StringVar()
editor=StringVar()
publisheryear=StringVar()

def save():
    if referenceV.get()=="":
        tmsg.showerror("Error","Reference feild must be filled")
    else:
        con=pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="cms"
        )
        mycursor=con.cursor()
        sql="INSERT INTO library (member_type,reference_no,first_name,last_name,address,post_code,mobile,book_id,book_title,author,date_borrowed,date_due,day_in_loan) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(membertypeV.get(),referenceV.get(),fnameV.get(),lnameV.get(),addressV.get(),postV.get(),mobileV.get(),IdV.get(),titleV.get(),authorV.get(),dateborrowedV.get(),datedueV.get(),dayloanV.get())
        mycursor.execute(sql,val)
        con.commit()
        con.close()
        tmsg.showinfo("Attention","Data has been submitted successfully!")
def getdata():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute("select * from library")
    rows=mycursor.fetchall()
    if (rows)!=0:
        Library_table.delete(*Library_table.get_children())
        for row in rows:
            Library_table.insert("",END,values=row)
        con.commit()
    con.close()

def getcursor1(ev):
    cursor=Library_table.focus()
    content=Library_table.item(cursor)
    row=content['values']
    membertypeV.set(row[0])
    referenceV.set(row[1])
    fnameV.set(row[2])
    lnameV.set(row[3])
    addressV.set(row[4])
    postV.set(row[5])
    mobileV.set(row[6])
    IdV.set(row[7])
    titleV.set(row[8])
    authorV.set(row[9])
    dateborrowedV.set(row[10])
    datedueV.set(row[11])
    dayloanV.set(row[12])
def reset():
    membertypeV.set('')
    referenceV.set('')
    fnameV.set('')
    lnameV.set('')
    addressV.set('')
    postV.set('')
    mobileV.set('')
    IdV.set('')
    titleV.set('')
    authorV.set('')
    dateborrowedV.set('')
    datedueV.set('')
    dayloanV.set('')
    booktxt.delete("1.0",END)
    Library_table.delete(*Library_table.get_children())

def exit():
    a=tmsg.askyesno("Attention","Confirm if you want to exit!!!")
    if a==True:
        rootL.destroy()
    else:
        pass
def search():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute(f"select * from library where member_type like '%{membertypeV.get()}%' and reference_no like '%{referenceV.get()}%' and first_name like '%{fnameV.get()}%' and last_name like '%{lnameV.get()}%' and address like '%{addressV.get()}%' and post_code like '%{postV.get()}%' and mobile like '%{mobileV.get()}%'")
    rows=mycursor.fetchall()
    if(rows)!=0:
        Library_table.delete(*Library_table.get_children())
        for row in rows:
            Library_table.insert("",END,values=row)
        con.commit()
    con.close()

def update():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute("update Library set member_type=%s,first_name=%s,last_name=%s,address=%s,post_code=%s,mobile=%s,book_id=%s,book_title=%s,author=%s,date_borrowed=%s,date_due=%s,day_in_loan=%s where reference_no=%s",(membertypeV.get(),fnameV.get(),lnameV.get(),addressV.get(),postV.get(),mobileV.get(),IdV.get(),titleV.get(),authorV.get(),dateborrowedV.get(),datedueV.get(),dayloanV.get(),referenceV.get()))
    con.commit()
    reset()
    con.close()
def delete():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute("delete from library where reference_no=%s",referenceV.get())
    con.commit()
    reset()
    con.close()


def getcursor(event):
    value=str(lst.get(lst.curselection()))
    v=value
    if (v ==' C'):
        IdV.set('ISBN 525341')
        titleV.set('Programming using C')
        authorV.set('Yashwant Kanetkar')
        import datetime
        d1=datetime.date.today()
        d2=datetime.timedelta(days=14)
        d3=(d1+d2)
        dateborrowedV.set(d1)
        dayloanV.set('14')
        datedueV.set(d3)
        editor.set('5th')
        publisheryear.set('2019')
        details()
    elif(v==' C++'):
        IdV.set('ISBN 345687')
        titleV.set('Programming using C++')
        authorV.set('Yashwant Kanetkar')
        import datetime
        d1=datetime.date.today()
        d2=datetime.timedelta(days=10)
        d3=(d1+d2)
        dateborrowedV.set(d1)
        dayloanV.set('10')
        datedueV.set(d3)
        editor.set('4th')
        publisheryear.set('2019')
        details()
    elif (v == ' Java'):
        IdV.set('ISBN 643842')
        titleV.set('Java Programming')
        authorV.set('Joshua Bloch')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=13)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('13')
        datedueV.set(d3)
        editor.set('7th')
        publisheryear.set('2019')
        details()
    elif (v == ' Python'):
        IdV.set('ISBN 564524')
        titleV.set('Python Programming')
        authorV.set('John Zelle')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=13)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('13')
        datedueV.set(d3)
        editor.set('3th')
        publisheryear.set('2019')
        details()
    elif (v == ' PHP'):
        IdV.set('ISBN 735893')
        titleV.set('PHP Programming')
        authorV.set('Alan Forbes')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=15)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('15')
        datedueV.set(d3)
        editor.set('9th')
        publisheryear.set('2019')
        details()
    elif (v == ' Java Script'):
        IdV.set('ISBN 643842')
        titleV.set('Java Script Programming')
        authorV.set('Jon Duckett.')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=12)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('12')
        datedueV.set(d3)
        editor.set('4th')
        publisheryear.set('2019')
        details()
    elif (v == ' My SQL'):
        IdV.set('ISBN 649635')
        titleV.set('My SQL Programming')
        authorV.set('Groff James')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=10)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('10')
        datedueV.set(d3)
        editor.set('9th')
        publisheryear.set('2019')
        details()
    elif (v == ' Data Structure'):
        IdV.set('ISBN 531588')
        titleV.set('Data Structure')
        authorV.set('Karumanchi Narasimha')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=9)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('9')
        datedueV.set(d3)
        editor.set('10th')
        publisheryear.set('2019')
        details()
    elif (v == ' Linux'):
        IdV.set('ISBN 356853')
        titleV.set('Linux Administration')
        authorV.set('SOYINKA')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=15)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('15')
        datedueV.set(d3)
        editor.set('10th')
        publisheryear.set('2019')
        details()
    elif (v == ' Operating System'):
        IdV.set('ISBN 536453')
        titleV.set('OS Concepts ')
        authorV.set('Silberschatz Abraham')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=9)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('9')
        datedueV.set(d3)
        editor.set('4th')
        publisheryear.set('2019')
        details()
    elif (v == ' Web Developement'):
        IdV.set('ISBN 543548')
        titleV.set('Web Developement ')
        authorV.set('Paul McFedries')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=6)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('6')
        datedueV.set(d3)
        editor.set('2th')
        publisheryear.set('2019')
        details()
    elif (v == ' Data Science'):
        IdV.set('ISBN 835764')
        titleV.set('Data Science Concept ')
        authorV.set('David Stephenson')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=11)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('11')
        datedueV.set(d3)
        editor.set('12th')
        publisheryear.set('2019')
        details()
    elif (v == ' Algorithms'):
        IdV.set('ISBN 535674')
        titleV.set('Basics of Algorithm ')
        authorV.set('Karumanchi Narasimha')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=9)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('9')
        datedueV.set(d3)
        editor.set('4th')
        publisheryear.set('2019')
        details()
    elif (v == ' Android'):
        IdV.set('ISBN 356452')
        titleV.set('Android Programming')
        authorV.set('Harwani B. M')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=8)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('8')
        datedueV.set(d3)
        editor.set('9th')
        publisheryear.set('2019')
        details()
    elif (v == ' VB.net'):
        IdV.set('ISBN 643840')
        titleV.set('VB.net Programming')
        authorV.set('Joshep')
        import datetime
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days=15)
        d3 = (d1 + d2)
        dateborrowedV.set(d1)
        dayloanV.set('15')
        datedueV.set(d3)
        editor.set('10th')
        publisheryear.set('2019')
        details()


def details():
    booktxt.delete("1.0",END)
    booktxt.insert(END," Book Details:\t"+'\n\n')
    booktxt.insert(END,'Book ID:\t'+IdV.get()+'\n')
    booktxt.insert(END,'Book Title:\t'+titleV.get()+'\n')
    booktxt.insert(END,'Author:\t'+authorV.get()+'\n')
    booktxt.insert(END,'Date Borrowed:\t'+dateborrowedV.get()+'\n')
    booktxt.insert(END,'Date Due:\t'+datedueV.get()+'\n')
    booktxt.insert(END,'Days in Loan:\t'+dayloanV.get()+'\n')
    booktxt.insert(END,'Publishing Year:\t'+publisheryear.get()+'\n')
    booktxt.insert(END,'Edition:\t'+editor.get()+'\n')

headingframe=Frame(rootL,bd=10,relief=GROOVE,bg="yellow")
headingframe.place(x=100,width=950,height=60)

headingL=Label(headingframe,text="LIBRARY MANAGEMENT SYSTEM",bg="yellow",bd=2,relief=SUNKEN,font="lucida 20 bold")
headingL.place(x=300)

mainframe=Frame(rootL,bd=10,relief=GROOVE,bg="yellow")
mainframe.place(x=5,y=60,width=1190,height=335)

infoframe=LabelFrame(mainframe,text="Library Membership Info:",font="lucida 15 bold",bg="yellow",bd=7,relief=GROOVE)
infoframe.place(x=10,y=2,width=700,height=310)

membertypeL = Label(infoframe, text="Member Type", font="lucida 15 bold",bg="yellow")
membertypeL.grid(row=0, column=0, padx=5, pady=5, sticky=W)
membertypeE = tkinter.ttk.Combobox(infoframe,textvariable=membertypeV, font="lucida 10 bold", state="readonly")
membertypeE["values"] = ("","Faculty", "Student", "HOD")
membertypeE.grid(row=0, column=1)

referencL = Label(infoframe, text="Reference No", font="lucida 15 bold",bg="yellow")
referencL.grid(row=1, column=0, padx=5, pady=5, sticky=W)
referencE = Entry(infoframe,textvariable=referenceV, font="lucida 10 bold", bd=3, relief=RIDGE)
referencE.grid(row=1, column=1, sticky=W)

firstnameL = Label(infoframe, text="First Name", font="lucida 15 bold",bg="yellow")
firstnameL.grid(row=2, column=0, padx=5, pady=5, sticky=W)
firstnameE = Entry(infoframe,textvariable=fnameV, font="lucida 10 bold", bd=3, relief=RIDGE)
firstnameE.grid(row=2, column=1, sticky=W)

lastnameL = Label(infoframe, text="Last Name", font="lucida 15 bold",bg="yellow")
lastnameL.grid(row=3, column=0, padx=5, pady=5, sticky=W)
lastnameE = Entry(infoframe,textvariable=lnameV, font="lucida 10 bold", bd=3, relief=RIDGE)
lastnameE.grid(row=3, column=1, sticky=W)

addressL = Label(infoframe, text="Address", font="lucida 15 bold",bg="yellow")
addressL.grid(row=4, column=0, padx=5, pady=5, sticky=W)
addressE = Entry(infoframe,textvariable=addressV, font="lucida 10 bold", bd=3, relief=RIDGE)
addressE.grid(row=4, column=1, sticky=W)

postL = Label(infoframe, text="Post Code", font="lucida 15 bold",bg="yellow")
postL.grid(row=5, column=0, padx=5, pady=5, sticky=W)
postE = Entry(infoframe,textvariable=postV, font="lucida 10 bold", bd=3, relief=RIDGE)
postE.grid(row=5, column=1, sticky=W)

mobL = Label(infoframe, text="Mobile Number", font="lucida 15 bold",bg="yellow")
mobL.grid(row=6, column=0, padx=5, pady=5, sticky=W)
mobE = Entry(infoframe,textvariable=mobileV, font="lucida 10 bold", bd=3, relief=RIDGE)
mobE.grid(row=6, column=1, sticky=W)

bookidL = Label(infoframe, text="Book Id", font="lucida 15 bold",bg="yellow")
bookidL.grid(row=0, column=3, padx=10, pady=5, sticky=W)
bookidE = Entry(infoframe,textvariable=IdV, font="lucida 10 bold", bd=3, relief=RIDGE)
bookidE.grid(row=0, column=4, sticky=W)

booktitleL = Label(infoframe, text="Book Title", font="lucida 15 bold",bg="yellow")
booktitleL.grid(row=1, column=3, padx=10, pady=5, sticky=W)
booktitleE = Entry(infoframe,textvariable=titleV, font="lucida 10 bold", bd=3, relief=RIDGE)
booktitleE.grid(row=1, column=4, sticky=W)

authorL = Label(infoframe, text="Author", font="lucida 15 bold",bg="yellow")
authorL.grid(row=2, column=3, padx=10, pady=5, sticky=W)
authorE = Entry(infoframe,textvariable=authorV, font="lucida 10 bold", bd=3, relief=RIDGE)
authorE.grid(row=2, column=4, sticky=W)

dateborrowedL = Label(infoframe, text="Date Barrowed", font="lucida 15 bold",bg="yellow")
dateborrowedL.grid(row=3, column=3, padx=10, pady=5, sticky=W)
dateborrowedE = Entry(infoframe,textvariable=dateborrowedV, font="lucida 10 bold", bd=3, relief=RIDGE)
dateborrowedE.grid(row=3, column=4, sticky=W)

datedueL = Label(infoframe, text="Date Due", font="lucida 15 bold",bg="yellow")
datedueL.grid(row=4, column=3, padx=10, pady=5, sticky=W)
datedueE = Entry(infoframe,textvariable=datedueV, font="lucida 10 bold", bd=3, relief=RIDGE)
datedueE.grid(row=4, column=4, sticky=W)

dayinloanL = Label(infoframe, text="Days In Loan", font="lucida 15 bold", bg="yellow")
dayinloanL.grid(row=5, column=3, padx=10, pady=5, sticky=W)
dayinloanE = Entry(infoframe,textvariable=dayloanV, font="lucida 10 bold", bd=3, relief=RIDGE)
dayinloanE.grid(row=5, column=4, sticky=W)




Bookdetframe = LabelFrame(mainframe, text="Book Details", font="lucida 15 bold", bg="yellow", bd=7, relief=GROOVE)
Bookdetframe.place(x=720, y=5, width=445, height=295)

Booktableframe=Frame(Bookdetframe,bd=5, relief=GROOVE, bg="yellow")
Booktableframe.place(x=10,y=5,width=200,height=250)

scroll_y=Scrollbar(Booktableframe,orient=VERTICAL)

lst=Listbox(Booktableframe,yscrollcommand=scroll_y)

scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=lst.yview)

lst.pack(fill=BOTH,expand=1)
lst.insert(END," C")
lst.insert(END,' C++')
lst.insert(END,' Java')
lst.insert(END,' Python')
lst.insert(END,' PHP')
lst.insert(END,' Java Script')
lst.insert(END,' My SQL')
lst.insert(END,' Data Structure')
lst.insert(END,' Linux')
lst.insert(END,' Operating System')
lst.insert(END,' Web Developement')
lst.insert(END,' Data Science')
lst.insert(END, ' Algorithms')
lst.insert(END,' Android')
lst.insert(END,' VB.net')
lst.bind("<<ListboxSelect>>",getcursor)



txtframe=Frame(Bookdetframe,bd=5, relief=GROOVE, bg="yellow")
txtframe.place(x=210,y=5,width=200,height=250)

booktxt=Text(txtframe,font="lucida 10 bold")
booktxt.pack(fill=BOTH)




tableframe = Frame(rootL, bd=10, relief=GROOVE, bg="yellow")
tableframe.place(x=25, y=395, width=1150,height=150)

scroll_y=Scrollbar(tableframe,orient=VERTICAL)
scroll_x=Scrollbar(tableframe,orient=HORIZONTAL)

Library_table=tkinter.ttk.Treeview(tableframe,column=("Member Type","Referenc no","First name","Last name","Address","Post code","Mobile no","Book ID","Book Title","Author","Date borrowed","Date due","Day in loan"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=Library_table.xview)
scroll_y.config(command=Library_table.yview)

Library_table.heading("Member Type",text="Member Type")
Library_table.heading("Referenc no",text="Referenc no")
Library_table.heading("First name",text="First name")
Library_table.heading("Last name",text="Last name")
Library_table.heading("Address",text="Address")
Library_table.heading("Post code",text="Post code")
Library_table.heading("Mobile no",text="Mobile no")
Library_table.heading("Book ID",text="Book ID")
Library_table.heading("Book Title",text="Book Title")
Library_table.heading("Author",text="Author")
Library_table.heading("Date borrowed",text="Date borrowed")
Library_table.heading("Date due",text="Date due")
Library_table.heading("Day in loan",text="Day in loan")

Library_table['show']="headings"

Library_table.column("Member Type",width=100)
Library_table.column("Referenc no",width=100)
Library_table.column("First name",width=100)
Library_table.column("Last name",width=100)
Library_table.column("Address",width=100)
Library_table.column("Post code",width=100)
Library_table.column("Mobile no",width=100)
Library_table.column("Book ID",width=100)
Library_table.column("Book Title",width=100)
Library_table.column("Author",width=100)
Library_table.column("Date borrowed",width=100)
Library_table.column("Date due",width=100)
Library_table.column("Day in loan",width=100)

Library_table.pack(fill=BOTH,expand=1)
Library_table.bind("<ButtonRelease-1>",getcursor1)




btnframe = Frame(rootL, bd=10, relief=GROOVE, bg="yellow")
btnframe.place(x=200, y=548, width=720,height=50)

savebtn=Button(btnframe,text="SAVE",font="lucida 8 bold",width=10,command=save)
savebtn.grid(row=0,column=0,padx=10,pady=2)

displaybtn=Button(btnframe,text="DISPLAY",font="lucida 8 bold",width=10,command=getdata)
displaybtn.grid(row=0,column=1,padx=10,pady=2)

resetbtn=Button(btnframe,text="RESET",font="lucida 8 bold",width=10,command=reset)
resetbtn.grid(row=0,column=2,padx=10,pady=2)

updatebtn=Button(btnframe,text="UPDATE",font="lucida 8 bold",width=10,command=update)
updatebtn.grid(row=0,column=3,padx=10,pady=2)

delbtn=Button(btnframe,text="DELETE",font="lucida 8 bold",width=10,command=delete)
delbtn.grid(row=0,column=4,padx=10,pady=2)

searchbtn=Button(btnframe,text="SEARCH",font="lucida 8 bold",width=10,command=search)
searchbtn.grid(row=0,column=5,padx=10,pady=2)


exitbtn=Button(btnframe,text="EXIT",font="lucida 8 bold",width=10,command=exit)
exitbtn.grid(row=0,column=7,padx=10,pady=2)





rootL.mainloop()
