from tkinter import *
import tkinter.ttk
import pymysql
import tkinter.messagebox as tmsg
rootS = Tk()



# ****************** All the variables**********************
name_var=StringVar()
fname_var=StringVar()
mname_var=StringVar()
address_var=StringVar()
mobile_var=StringVar()
email_var=StringVar()
dob_var=StringVar()
gender_var=StringVar()

def add():
    if mobile_var.get()=="" and name_var.get()=="":
        tmsg.showerror("Error","All field are reqiured to be filled")
    else:
        con = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="cms"
        )
        mycursor = con.cursor()
        sql = "INSERT INTO student (name,father_name,mother_name,address,mobile,email,dob,gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(name_var.get(), fname_var.get(), mname_var.get(), address_var.get(), mobile_var.get(),email_var.get(), dob_var.get(), gender_var.get())
        mycursor.execute(sql, val)
        con.commit()
        display()
        con.close()
        tmsg.showinfo("Attention","Data has been Submitted successfully")
def display():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute("select * from student where mobile=%s",mobile_var.get())
    rows=mycursor.fetchall()
    if(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert("",END,values=row)
        con.commit()
    con.close()

def fetchall():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute("select * from student")
    rows=mycursor.fetchall()
    if(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert("",END,values=row)
        con.commit()
    con.close()

def getcursor(ev):
    global rows
    cursor=student_table.focus()
    row=student_table.item(cursor)
    rows=row['values']
    name_var.set(rows[0])
    fname_var.set(rows[1])
    mname_var.set(rows[2])
    address_var.set(rows[3])
    mobile_var.set(rows[4])
    email_var.set(rows[5])
    dob_var.set(rows[6])
    gender_var.set(rows[7])
def clear():
    name_var.set("")
    fname_var.set("")
    mname_var.set("")
    address_var.set("")
    mobile_var.set("")
    email_var.set("")
    dob_var.set("")
    gender_var.set("")
    student_table.delete(*student_table.get_children())
def delete():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute("delete from student where mobile=%s",mobile_var.get())
    con.commit()
    clear()
    con.close()
    # tmsg.showinfo("Attention","Selected Data has been deleted successfully")



def update():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute("update student set name=%s,father_name=%s,mother_name=%s,address=%s,email=%s,dob=%s,gender=%s where mobile=%s",(name_var.get(),fname_var.get(),mname_var.get(),address_var.get(),email_var.get(),dob_var.get(),gender_var.get(),mobile_var.get()))
    con.commit()
    con.close()
    # tmsg.showinfo("Attention","Selected Data has been updated successfully")

def search():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    if name_var.get()=="" and fname_var.get()=="" and mname_var.get()=="" and address_var.get() and mobile_var.get()=="" and email_var.get()=="" and dob_var.get()=="" and gender_var.get()=="":
        tmsg.showerror("Error","Enter given feild area to search")
    else:
        mycursor.execute(f"select * from student where name like '%{name_var.get()}%' and father_name like '%{fname_var.get()}%' and mother_name like '%{mname_var.get()}%' and address like '%{address_var.get()}%' and mobile like '%{mobile_var.get()}%' and email like '%{email_var.get()}%' and dob like '%{dob_var.get()}%' and gender like '%{gender_var.get()}%'")
        rows=mycursor.fetchall()
        if(rows)!=0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert("",END,values=row)
            con.commit()
        con.close()

def exit():
    ask=tmsg.askyesno("Attention","Do you Really want to Exit")
    if ask==True:
        rootS.destroy()
    else:
        pass

rootS.title("STUDENT PROFILE")
rootS.geometry("1200x600+0+0")
rootS.maxsize(1200,600)
rootS.config(bg="pink")



mainFrame = Frame(rootS, bd=10, relief=GROOVE,bg="pink")
mainFrame.place(x=50, y=10, width=1100, height=470)


stdinfoframe = LabelFrame(mainFrame, text="Student Information", font="lucida 15 bold", bd=7,
                          relief=GROOVE,bg="pink")
stdinfoframe.place(x=10, y=10, width=550, height=430)

nameL = Label(stdinfoframe, text="Name", font="lucida 15 bold",bg="pink")
nameL.grid(row=0, column=0, padx=10, pady=10, sticky=W)
nameE = Entry(stdinfoframe,textvariable=name_var, font="lucida 10 bold", bd=5, relief=GROOVE, width=30)
nameE.grid(row=0, column=1)

fnameL = Label(stdinfoframe, text="Father Name", font="lucida 15 bold",bg="pink")
fnameL.grid(row=1, column=0, padx=10, pady=10, sticky=W)
fnameE = Entry(stdinfoframe, textvariable=fname_var,font="lucida 10 bold", bd=5, relief=GROOVE, width=30)
fnameE.grid(row=1, column=1)

mnameL = Label(stdinfoframe, text="Mother Name", font="lucida 15 bold",bg="pink")
mnameL.grid(row=2, column=0, padx=10, pady=10, sticky=W)
mnameE = Entry(stdinfoframe, textvariable=mname_var,font="lucida 10 bold", bd=5, relief=GROOVE, width=30)
mnameE.grid(row=2, column=1)

addressL = Label(stdinfoframe, text="Address", font="lucida 15 bold",bg="pink")
addressL.grid(row=3, column=0, padx=10, pady=10, sticky=W)
addressE = Entry(stdinfoframe, textvariable=address_var,font="lucida 10 bold", bd=5, relief=GROOVE, width=30)
addressE.grid(row=3, column=1)

mnumberL = Label(stdinfoframe, text="Mobile Number", font="lucida 15 bold",bg="pink")
mnumberL.grid(row=4, column=0, padx=10, pady=10, sticky=W)
mnumberE = Entry(stdinfoframe,textvariable=mobile_var, font="lucida 10 bold", bd=5, relief=GROOVE, width=30)
mnumberE.grid(row=4, column=1)

emailL = Label(stdinfoframe, text="Email Address", font="lucida 15 bold",bg="pink")
emailL.grid(row=5, column=0, padx=10, pady=10, sticky=W)
emailE = Entry(stdinfoframe,textvariable=email_var, font="lucida 10 bold", bd=5, relief=GROOVE, width=30)
emailE.grid(row=5, column=1)

dobL = Label(stdinfoframe, text="Date of Birth", font="lucida 15 bold",bg="pink")
dobL.grid(row=6, column=0, padx=10, pady=10, sticky=W)
dobE = Entry(stdinfoframe,textvariable=dob_var, font="lucida 10 bold", bd=5, relief=GROOVE, width=30)
dobE.grid(row=6, column=1)

genderL = Label(stdinfoframe, text="Gender", font="lucida 15 bold",bg="pink")
genderL.grid(row=7, column=0, padx=10, pady=10, sticky=W)
genderE = tkinter.ttk.Combobox(stdinfoframe,textvariable=gender_var, font="lucida 10 bold", state="readonly", width=30)
genderE["values"] = ("Male", "Female", "Other")
genderE.grid(row=7, column=1)

stddatabaseframe = LabelFrame(mainFrame, text="Student DataBase", font="lucida 15 bold", bd=7,
                              relief=GROOVE,bg="pink")
stddatabaseframe.place(x=570, y=1, width=500, height=420)
scroll_y = Scrollbar(stddatabaseframe, orient=VERTICAL)
scroll_x = Scrollbar(stddatabaseframe, orient=HORIZONTAL)
student_table = tkinter.ttk.Treeview(stddatabaseframe, column=(
"Name", "Father Name", "Mother Name", "Address", "Mobile Number", "Email", "DOB", "Gender"), yscrollcommand=scroll_y,
                                     xscrollcommand=scroll_x)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.config(command=student_table.yview)
scroll_x.config(command=student_table.xview)

student_table.heading("Name", text="Name")
student_table.heading("Father Name", text="Father Name")
student_table.heading("Mother Name", text="Mother Name")
student_table.heading("Address", text="Address")
student_table.heading("Mobile Number", text="Mobile Number")
student_table.heading("Email", text="Email")
student_table.heading("DOB", text="DOB")
student_table.heading("Gender", text="Gender")

student_table["show"] = "headings"
student_table.column("Name", width=100)
student_table.column("Father Name", width=100)
student_table.column("Mother Name", width=100)
student_table.column("Address", width=100)
student_table.column("Mobile Number", width=100)
student_table.column("Email", width=100)
student_table.column("DOB", width=100)
student_table.column("Gender", width=100)

student_table.pack(fill=BOTH, expand=1)
student_table.bind("<ButtonRelease-1>",getcursor)

btnframe = Frame(rootS, bd=8, relief=GROOVE,bg="pink")
btnframe.place(x=200, y=500, width=800, height=50)

savebtn = Button(btnframe, text="SAVE", bd=3, relief=RIDGE, font="lucida 10 bold", width=10,command=add)
savebtn.grid(row=0, column=0, padx=10, pady=2)

displaybtn = Button(btnframe, text="DISPLAY", bd=3, relief=RIDGE, font="lucida 10 bold", width=10,command=fetchall)
displaybtn.grid(row=0, column=1, padx=10, pady=2)

resetbtn = Button(btnframe, text="RESET", bd=3, relief=RIDGE, font="lucida 10 bold", width=10,command=clear)
resetbtn.grid(row=0, column=2, padx=10, pady=2)

updatebtn = Button(btnframe, text="UPDATE", bd=3, relief=RIDGE, font="lucida 10 bold", width=10,command=update)
updatebtn.grid(row=0, column=3, padx=10, pady=2)

deletebtn = Button(btnframe, text="DELETE", bd=3, relief=RIDGE, font="lucida 10 bold", width=10,command=delete)
deletebtn.grid(row=0, column=4, padx=10, pady=2)

searchbtn = Button(btnframe, text="SEARCH", bd=3, relief=RIDGE, font="lucida 10 bold", width=10,command=search)
searchbtn.grid(row=0, column=5, padx=10, pady=2)

exitbtn = Button(btnframe, text="EXIT", bd=3, relief=RIDGE, font="lucida 10 bold", width=10,command=exit)
exitbtn.grid(row=0, column=6, padx=10, pady=2)

rootS.mainloop()