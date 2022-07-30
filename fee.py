from tkinter import *
import pymysql
import datetime
import tkinter.ttk
import tkinter.messagebox as tmsg
def save():
    if receiptV.get()=="" :
        tmsg.showinfo("Attention","Receipt Number is required to be filled")
    else:
        con=pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="cms"
        )
        mycursor=con.cursor()
        sql="INSERT INTO fee (receipt_no,std_name,admn_no,date,branch,sem,paid,balance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(receiptV.get(),nameV.get(),admnV.get(),dateV.get(),branchV.get(),semV.get(),paidV.get(),balV.get())
        mycursor.execute(sql,val)
        con.commit()
        display()
        update()
        con.close()
        tmsg.showinfo("Attention","Data has been submitted successfully!!")
def display():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute("select * from fee where receipt_no=%s",receiptV.get())
    rows=mycursor.fetchall()
    if(rows)!=0:
        Fee_table.delete(*Fee_table.get_children())
        for row in rows:
            Fee_table.insert("",END,values=row)
        con.commit()
    con.close()

def fetchall():
    con=pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor=con.cursor()
    mycursor.execute("select * from fee")
    rows=mycursor.fetchall()
    if (rows)!=0:
        Fee_table.delete(*Fee_table.get_children())
        for row in rows:
            Fee_table.insert("",END,values=row)
        con.commit()
    con.close()
def getcursor(ev):
    cursor=Fee_table.focus()
    rows=Fee_table.item(cursor)
    row=rows['values']
    receiptV.set(row[0])
    nameV.set(row[1])
    admnV.set(row[2])
    dateV.set(row[3])
    branchV.set(row[4])
    semV.set(row[5])
    paidV.set(row[6])
    balV.set(row[7])
def reset():
    receiptV.set("")
    nameV.set("")
    admnV.set("")
    branchV.set("")
    semV.set("")
    paidV.set("0.0")
    balV.set("0.0")
    feereptxt.delete("1.0",END)
    Fee_table.delete(*Fee_table.get_children())
def update():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute(
        "update fee set std_name=%s,admn_no=%s,date=%s,branch=%s,sem=%s,paid=%s,balance=%s where receipt_no=%s",
        (nameV.get(), admnV.get(), dateV.get(), branchV.get(), semV.get(), paidV.get(),balV.get(),receiptV.get()))
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
    mycursor.execute("delete from fee where receipt_no=%s",receiptV.get())
    con.commit()
    reset()
    con.close()

def search():
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="cms"
    )
    mycursor = con.cursor()
    mycursor.execute(f"select * from fee where receipt_no like '%{receiptV.get()}%' and std_name like '%{nameV.get()}%' and admn_no like '%{admnV.get()}%' and date like '%{dateV.get()}%' and branch like '%{branchV.get()}%' and sem like '%{semV.get()}%'")
    rows = mycursor.fetchall()
    if (rows)!=0:
        Fee_table.delete(*Fee_table.get_children())
        for row in rows:
            Fee_table.insert("", END, values=row)
        con.commit()
    con.close()
def receipt():
    feereptxt.delete("1.0",END)
    feereptxt.insert(END,  "\t\tRECEIPT"+'\n\n')
    feereptxt.insert(END,'\tReceipt No :'+'\t'+ receiptV.get() +'\n')
    feereptxt.insert(END,'\tStudent Name  :'+'\t'+ nameV.get() +'\n')
    feereptxt.insert(END,'\tDate :'+'\t'+ dateV.get() +'\n')
    feereptxt.insert(END,'\tBranch :'+'\t'+ branchV.get() +'\n')
    feereptxt.insert(END,'\tSemester :'+'\t'+ semV.get() +'\n')
    x1=(totalV.get())
    x2=(paidV.get())
    x3=(x1-x2)
    feereptxt.insert(END,'\tTotal Amount :'+'\t'+ str(x1) +'\n')
    feereptxt.insert(END,'\tPaid Amount :'+'\t'+ str(x2) +'\n')
    feereptxt.insert(END,'\tBalance Amount :'+'\t'+ str(x3) +'\n')
    balV.set(x3)

def exit():
    ask=tmsg.askyesno("Attention","Want to Exit??")
    if ask==True:
        rootF.destroy()
    else:
        pass
rootF=Tk()
rootF.title("FEE REPORT")
rootF.geometry("1200x600+0+0")
rootF.maxsize(1200,600)
rootF.config(bg="red")
headingframe=Frame(rootF,bd=10,relief=GROOVE,bg="red")
headingframe.place(x=100,width=950,height=60)
# ************* All the required variables*************

receiptV=StringVar()
nameV=StringVar()
admnV=StringVar()
dateV=StringVar()
branchV=StringVar()
semV=StringVar()
totalV=DoubleVar()
paidV=DoubleVar()
balV=DoubleVar()

headingL=Label(headingframe,text="FEE REPORT",bd=2,relief=SUNKEN,font="lucida 20 bold",bg="red")
headingL.place(x=350)

mainframe=Frame(rootF,bd=10,relief=GROOVE,bg="red")
mainframe.place(x=20,y=60,width=1150,height=300)

infoframe=LabelFrame(mainframe,text="Information",font="lucida 15 bold",bd=5,relief=GROOVE,bg="red")
infoframe.place(x=10,y=10,width=700,height=270)

receiptL = Label(infoframe,text="Receipt No:",font="lucida 15 bold",bg="red")
receiptL.grid(row=0,column=0,padx=5,pady=5,sticky=W)
receiptE=Entry(infoframe,font="lucida 10 bold",textvariable=receiptV,bd=3,relief=RIDGE)
receiptE.grid(row=0,column=1,sticky=W)

studentnameL = Label(infoframe,text="Student Name:",font="lucida 15 bold",bg="red")
studentnameL.grid(row=1,column=0,padx=5,pady=5,sticky=W)
studentnameE=Entry(infoframe,font="lucida 10 bold",textvariable=nameV,bd=3,relief=RIDGE)
studentnameE.grid(row=1,column=1,sticky=W)

admnL = Label(infoframe,text="Admission No:",font="lucida 15 bold",bg="red")
admnL.grid(row=2,column=0,padx=5,pady=5,sticky=W)
admnE=Entry(infoframe,font="lucida 10 bold",textvariable=admnV,bd=3,relief=RIDGE)
admnE.grid(row=2,column=1,sticky=W)

dateL = Label(infoframe,text="Date:",font="lucida 15 bold",bg="red")
dateL.grid(row=3,column=0,padx=5,pady=5,sticky=W)
dateE=Entry(infoframe,font="lucida 10 bold",textvariable=dateV,bd=3,relief=RIDGE)
dateE.grid(row=3,column=1,sticky=W)

d=datetime.date.today()
dateV.set(d)

branchL = Label(infoframe,text="Branch:",font="lucida 15 bold",bg="red")
branchL.grid(row=4,column=0,padx=5,pady=5,sticky=W)
branchE = tkinter.ttk.Combobox(infoframe,textvariable=branchV, font="lucida 10 bold")
branchE["values"] = ("","Electrical", "Mechcanical", "CSE","Chemical","Automobile","B.A","Bsc","BCA","MCA","BBA","MBA","Msc")
branchE.grid(row=4, column=1)

semL = Label(infoframe,text="Semester:",font="lucida 15 bold",bg="red")
semL.grid(row=5,column=0,padx=5,pady=5,sticky=W)
semE = tkinter.ttk.Combobox(infoframe,textvariable=semV, font="lucida 10 bold")
semE["values"] = ("","First", "Second", "Third","Forth","Fifth","sixth","seventh","Eigth")
semE.grid(row=5, column=1)

totalL=Label(infoframe,text="Total Amount:",font="lucida 15 bold",bg="red")
totalL.grid(row=1,column=2,padx=5,sticky=W)
totalE=Entry(infoframe,font="lucida 10 bold",textvariable=totalV,bd=3,relief=RIDGE,state="readonly")
totalE.grid(row=1,column=3,sticky=W)
totalV.set('36800')



paidL = Label(infoframe, text="Paid Amount:", font="lucida 15 bold",bg="red")
paidL.grid(row=2, column=2, padx=5,sticky=W)
paidE=Entry(infoframe,font="lucida 10 bold",textvariable=paidV,bd=3,relief=RIDGE)

paidE.grid(row=2,column=3,sticky=W)


balL = Label(infoframe, text="Balance Amount:", font="lucida 15 bold",bg="red")
balL.grid(row=3, column=2, padx=5,sticky=W)
balE=Entry(infoframe,font="lucida 10 bold",textvariable=balV,bd=3,relief=RIDGE)
balE.grid(row=3,column=3,sticky=W)




feerepframe= LabelFrame(mainframe, text="FEE RECEIPT", font="lucida 15 bold", bd=5, relief=GROOVE,bg="red")
feerepframe.place(x=720, y=5, width=400, height=265)

feereptxt=Text(feerepframe,font="lucida 13 bold")
feereptxt.pack(fill=BOTH)

tableframe = Frame(rootF, bd=10, relief=GROOVE,bg="red")
tableframe.place(x=25, y=370, width=1150,height=150)
scroll_y=Scrollbar(tableframe,orient=VERTICAL)
scroll_x=Scrollbar(tableframe,orient=HORIZONTAL)
Fee_table=tkinter.ttk.Treeview(tableframe,column=("Receipt no","Student name","Admission number","Date","Branch","Semester","Paid amount","Balance amount"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=Fee_table.xview)
scroll_y.config(command=Fee_table.yview)

Fee_table.heading("Receipt no",text="Receipt number")
Fee_table.heading("Student name",text="Student Name")
Fee_table.heading("Admission number",text="Admission number")
Fee_table.heading("Date",text="Date")
Fee_table.heading("Branch",text="Branch")
Fee_table.heading("Semester",text="Semester")
Fee_table.heading("Paid amount",text="Paid Amount")
Fee_table.heading("Balance amount",text="Balance Amount")

Fee_table['show']="headings"

Fee_table.column("Receipt no",width=5)
Fee_table.column("Student name",width=5)
Fee_table.column("Admission number",width=5)
Fee_table.column("Date",width=5)
Fee_table.column("Branch",width=5)
Fee_table.column("Semester",width=5)
Fee_table.column("Paid amount",width=5)
Fee_table.column("Balance amount",width=5)

Fee_table.pack(fill=BOTH,expand=1)
Fee_table.bind("<ButtonRelease-1>",getcursor)


btnframe = Frame(rootF, bd=10, relief=GROOVE,bg="red")
btnframe.place(x=200, y=525, width=900,height=50)

savebtn=Button(btnframe,text="SAVE",font="lucida 10 bold",width=10,command=save)
savebtn.grid(row=0,column=0,padx=10,pady=2)

displaybtn=Button(btnframe,text="DISPLAY",font="lucida 10 bold",width=10,command=fetchall)
displaybtn.grid(row=0,column=1,padx=10,pady=2)

resetbtn=Button(btnframe,text="RESET",font="lucida 10 bold",width=10,command=reset)
resetbtn.grid(row=0,column=2,padx=10,pady=2)

updatebtn=Button(btnframe,text="UPDATE",font="lucida 10 bold",width=10,command=update)
updatebtn.grid(row=0,column=3,padx=10,pady=2)

delbtn=Button(btnframe,text="DELETE",font="lucida 10 bold",width=10,command=delete)
delbtn.grid(row=0,column=4,padx=10,pady=2)

searchbtn=Button(btnframe,text="SEARCH",font="lucida 10 bold",width=10,command=search)
searchbtn.grid(row=0,column=5,padx=10,pady=2)

reciptbtn=Button(btnframe,text="RECEIPT",font="lucida 10 bold",width=10,command=receipt)
reciptbtn.grid(row=0,column=6,padx=10,pady=2)

exitbtn=Button(btnframe,text="EXIT",font="lucida 10 bold",width=10,command=exit)
exitbtn.grid(row=0,column=7,padx=10,pady=2)




rootF.mainloop()