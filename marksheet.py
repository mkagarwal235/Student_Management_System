from tkinter import *
import tkinter.ttk
import tkinter.messagebox as tmsg
import pymysql
def update():
    con = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='cms'
    )
    mycursor = con.cursor()
    mycursor.execute("update marksheet set father_name=%s,dob=%s,school_name=%s,mother_name=%s,gender=%s,email=%s,maths=%s,phy=%s,chem=%s,programming=%s,eng=%s,grand_total=%s,cpga=%s,result=%s,grade=%s,percentage=%s where roll_no=%s",(fnameV.get(),dobV.get(),schoolnameV.get(),mnameV.get(),genderV.get(),emailV.get(),mathsV.get(),phyV.get(),chemV.get(),programmingV.get(),engV.get(),grandtotV.get(),cgpaV.get(),resultV.get(),gradeV.get(),percentageV.get(),rollV.get()))
    con.commit()
    con.close()
    tmsg.showinfo("Attention","Data has been successfully updated")

def save():
    if rollV.get()=="":
        tmsg.showerror("Attention","All Field Are Required to be Filled")
    else:
        con=pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='cms'
        )
        mycursor=con.cursor()
        sql="INSERT INTO marksheet (name,father_name,dob,school_name,roll_no,mother_name,gender,email,math,phy,chem,programming,eng,grand_total,cpga,result,grade,percentage) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(nameV.get(),fnameV.get(),dobV.get(),schoolnameV.get(),rollV.get(),mnameV.get(),genderV.get(),emailV.get(),mathsV.get(),phyV.get(),chemV.get(),programmingV.get(),engV.get(),grandtotV.get(),cgpaV.get(),resultV.get(),gradeV.get(),percentageV.get())
        mycursor.execute(sql,val)
        con.commit()
        con.close()
        tmsg.showinfo("Attention","Data has been submitted successfully!")
def searchRoll(a):
    con=pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='cms'
    )
    mycursor=con.cursor()
    mycursor.execute("select * from marksheet where roll_no=%s",a)
    row=mycursor.fetchall()
    return row


def compute():
    m1=mathsV.get()
    m2=phyV.get()
    m3=chemV.get()
    m4=programmingV.get()
    m5=engV.get()
    if m1>100:
        tmsg.askokcancel("Attention","Please Enter Marks less than 100.")
    if m2>100:
        tmsg.askokcancel("Attention","Please Enter Marks less than 100.")
    if m3>100:
        tmsg.askokcancel("Attention","Please Enter Marks less than 100.")
    if m4>100:
        tmsg.askokcancel("Attention","Please Enter Marks less than 100.")
    if m5>100:
        tmsg.askokcancel("Attention","Please Enter Marks less than 100.")
    tot=(m1+m2+m3+m4+m5)
    grandtotV.set(tot)
    per=(tot*100)/500
    percentageV.set(per)
    cgpa=per/9.5
    cgpaV.set(round(cgpa,1))
    if cgpa>10:
        cgpaV.set('10')
    if per<+40:
        grd='G'
    elif(per<=50):
        grd='F'
    elif (per <= 60):
        grd = 'E'
    elif (per <= 70):
        grd = 'D'
    elif (per <= 80):
        grd = 'C'
    elif (per <= 90):
        grd = 'B'
    else:
        grd='A'
    gradeV.set(grd)

    count=0
    if m1<33:
        count=count+1
    if m2<33:
        count=count+1
    if m3<33:
        count=count+1
    if m4<33:
        count=count+1
    if m5<33:
        count=count+1

    if (count==0):
        res='Pass'
    elif(count==1 or count==2):
        res='Supply'
    else:
        res="Fail"
    resultV.set(res)
def reset():
    nameV.set("")
    fnameV.set("")
    dobV.set("")
    schoolnameV.set("")
    rollV.set("")
    mnameV.set("")
    genderV.set("")
    mathsV.set("0.0")
    phyV.set("0.0")
    chemV.set("0.0")
    programmingV.set("0.0")
    engV.set("0.0")
    grandtotV.set("0.0")
    cgpaV.set("0.0")
    resultV.set("")
    gradeV.set("")
    percentageV.set("")
def exit():
    ask=tmsg.askyesno("Attention","Confirn if you want to Exit!!!")
    if ask==True:
        root.destroy()
    else:
        pass

if __name__ == '__main__':
    root = Tk()
    root.title("MARKSHEETS INFO")
    root.geometry("1200x800+0+0")
    root.config(bg="orange")

    # ***************** Variables***********************

    nameV=StringVar()
    fnameV=StringVar()
    dobV=StringVar()
    schoolnameV=StringVar()
    rollV=StringVar()
    mnameV=StringVar()
    genderV=StringVar()
    emailV=StringVar()
    mathsV=DoubleVar()
    phyV=DoubleVar()
    chemV=DoubleVar()
    programmingV=DoubleVar()
    engV=DoubleVar()
    grandtotV=DoubleVar()
    passmarksV=DoubleVar()
    passmarksV.set("33")
    totmarksV=DoubleVar()
    totmarksV.set('100')
    cgpaV=DoubleVar()
    resultV=StringVar()
    gradeV=StringVar()
    percentageV=DoubleVar()


    frame1=LabelFrame(root,text='Student Details',font="lucida 20 bold",bd=10,relief=GROOVE,bg="orange")
    frame1.place(x=20,y=20,width=1150,height=270)

    nameL=Label(frame1,text="Name",font="lucida 20 bold",bg='orange')
    nameL.grid(row=0,column=0,padx=10,pady=10,sticky=W)
    nameE=Entry(frame1,textvariable=nameV,font="lucifda 15 bold")
    nameE.grid(row=0,column=1,sticky=W)

    fnameL=Label(frame1,text="Father Name",font="lucida 20 bold",bg='orange')
    fnameL.grid(row=1,column=0,padx=10,pady=10,sticky=W)
    fnameE=Entry(frame1,textvariable=fnameV,font="lucifda 15 bold")
    fnameE.grid(row=1,column=1,sticky=W)

    dobL=Label(frame1,text="Date of Birth",font="lucida 20 bold",bg='orange')
    dobL.grid(row=2,column=0,padx=10,pady=10,sticky=W)
    dobE=Entry(frame1,textvariable=dobV,font="lucifda 15 bold")
    dobE.grid(row=2,column=1,sticky=W)

    schoolnameL=Label(frame1,text="School Name",font="lucida 20 bold",bg='orange')
    schoolnameL.grid(row=3,column=0,padx=10,pady=10,sticky=W)
    schoolnameE=Entry(frame1,textvariable=schoolnameV,font="lucifda 15 bold")
    schoolnameE.grid(row=3,column=1,sticky=W)

    rollL=Label(frame1,text="Roll Number",font="lucida 20 bold",bg='orange')
    rollL.grid(row=0,column=3,padx=50,pady=10,sticky=W)
    rollE=Entry(frame1,textvariable=rollV,font="lucifda 15 bold")
    rollE.grid(row=0,column=4,sticky=W)

    mnameL=Label(frame1,text="Mother name",font="lucida 20 bold",bg='orange')
    mnameL.grid(row=1,column=3,padx=50,pady=10,sticky=W)
    mnameE=Entry(frame1,textvariable=mnameV,font="lucifda 15 bold")
    mnameE.grid(row=1,column=4,sticky=W)

    genderL=Label(frame1,text="Gender",font="lucida 20 bold",bg='orange')
    genderL.grid(row=2,column=3,padx=50,pady=10,sticky=W)
    genderE=tkinter.ttk.Combobox(frame1,textvariable=genderV,font="lucida 15 bold",state="readonly")
    genderE['values']=('Male','Female','Others')
    genderE.grid(row=2,column=4)

    emailL=Label(frame1,text="Email ID",font="lucida 20 bold",bg='orange')
    emailL.grid(row=3,column=3,padx=50,pady=10,sticky=W)
    emailE=Entry(frame1,textvariable=emailV,font="lucifda 15 bold")
    emailE.grid(row=3,column=4,sticky=W)

    frame2=LabelFrame(root,text='Grades Point Obtained',font="lucida 20 bold",bd=10,relief=GROOVE,bg="orange")
    frame2.place(x=20,y=300,width=1150,height=390)

    subL=Label(frame2,text="Subject",font="lucida 20 bold",bg="orange")
    subL.grid(row=0,column=0,sticky=W,padx=50)

    subL=Label(frame2,text="Marks",font="lucida 20 bold",bg="orange")
    subL.grid(row=0,column=1,sticky=W)

    mathL=Label(frame2,text="Maths",font="lucida 15 underline",bg="orange")
    mathL.grid(row=1,column=0,sticky=W,padx=50,pady=10)
    mathE=Entry(frame2,font="lucifda 15 bold",textvariable=mathsV,width=7)
    mathE.grid(row=1,column=1,sticky=W)

    phyL=Label(frame2,text="Physices",font="lucida 15 underline",bg="orange")
    phyL.grid(row=2,column=0,sticky=W,padx=50,pady=10)
    phyE=Entry(frame2,textvariable=phyV,font="lucifda 15 bold",width=7)
    phyE.grid(row=2,column=1,sticky=W)

    chemL=Label(frame2,text="Chemistry",font="lucida 15 underline",bg="orange")
    chemL.grid(row=3,column=0,sticky=W,padx=50,pady=10)
    chemE=Entry(frame2,font="lucifda 15 bold",textvariable=chemV,width=7)
    chemE.grid(row=3,column=1,sticky=W)

    programmingL=Label(frame2,text="Programming",font="lucida 15 underline",bg="orange")
    programmingL.grid(row=4,column=0,sticky=W,padx=50,pady=10)
    programmingE=Entry(frame2,font="lucifda 15 bold",textvariable=programmingV,width=7)
    programmingE.grid(row=4,column=1,sticky=W)

    engL=Label(frame2,text="English",font="lucida 15 underline",bg="orange")
    engL.grid(row=5,column=0,sticky=W,padx=50,pady=10)
    engE=Entry(frame2,font="lucifda 15 bold",textvariable=engV,width=7)
    engE.grid(row=5,column=1,sticky=W)

    totalL=Label(frame2,text="Grand Total",font="lucida 15 bold",bg="orange")
    totalL.grid(row=6,column=0,sticky=W,padx=50,pady=10)
    totalE=Entry(frame2,font="lucifda 15 bold",textvariable=grandtotV,width=7)
    totalE.grid(row=6,column=1,sticky=W)

    passingL=Label(frame2,text="Passing Marks",font="lucida 20 bold",bg="orange")
    passingL.grid(row=0,column=3,padx=20)

    e1=Entry(frame2,font="lucida 15 bold",width=7,textvariable=passmarksV,state="readonly")
    e1.grid(row=1,column=3)

    e2=Entry(frame2,font="lucida 15 bold",width=7,textvariable=passmarksV,state="readonly")
    e2.grid(row=2,column=3)

    e3=Entry(frame2,font="lucida 15 bold",width=7,textvariable=passmarksV,state="readonly")
    e3.grid(row=3,column=3)

    e4=Entry(frame2,font="lucida 15 bold",width=7,textvariable=passmarksV,state="readonly")
    e4.grid(row=4,column=3)

    e5=Entry(frame2,font="lucida 15 bold",width=7,textvariable=passmarksV,state="readonly")
    e5.grid(row=5,column=3)


    cpgaL=Label(frame2,text="CGPA",font="lucida 20 bold",bg="orange")
    cpgaL.grid(row=6,column=3,padx=20)

    marksL=Label(frame2,text="Total Marks",font="lucida 20 bold",bg="orange")
    marksL.grid(row=0,column=4,padx=20)

    me1=Entry(frame2,font="lucida 15 bold",width=7,textvariable=totmarksV,state="readonly")
    me1.grid(row=1,column=4)

    me2=Entry(frame2,font="lucida 15 bold",width=7,textvariable=totmarksV,state="readonly")
    me2.grid(row=2,column=4)

    me3=Entry(frame2,font="lucida 15 bold",width=7,textvariable=totmarksV,state="readonly")
    me3.grid(row=3,column=4)

    me4=Entry(frame2,font="lucida 15 bold",width=7,textvariable=totmarksV,state="readonly")
    me4.grid(row=4,column=4)

    me5=Entry(frame2,font="lucida 15 bold",width=7,textvariable=totmarksV,state="readonly")
    me5.grid(row=5,column=4)

    cgpae5=Entry(frame2,font="lucida 15 bold",textvariable=cgpaV,width=7)
    cgpae5.grid(row=6,column=4)

    resulL=Label(frame2,text="Result",font="lucida 20 bold",bg="orange")
    resulL.grid(row=0,column=5)
    resultE=Entry(frame2,font="lucida 15 bold",textvariable=resultV,width=7)
    resultE.grid(row=0,column=6,padx=20)

    gradeL=Label(frame2,text="Grade",font="lucida 20 bold",bg="orange")
    gradeL.grid(row=1,column=5)
    gradeE=Entry(frame2,font="lucida 15 bold",textvariable=gradeV,width=7)
    gradeE.grid(row=1,column=6,padx=20)

    percentageL=Label(frame2,text="Percentage",font="lucida 20 bold",bg="orange")
    percentageL.grid(row=2,column=6)
    percentageE=Entry(frame2,font="lucida 15 bold",textvariable=percentageV,width=7)
    percentageE.grid(row=2,column=7,padx=20)

    computebtn=Button(frame2,text='Compute',font="lucida 15 bold",width=10,command=compute)
    computebtn.grid(row=2,column=5,pady=10)

    savebtn=Button(frame2,text='Save',font="lucida 15 bold",width=10,command=save)
    savebtn.grid(row=3,column=5)

    resetbtn=Button(frame2,text='Reset',font="lucida 15 bold",command=reset,width=10)
    resetbtn.grid(row=4,column=5)

    updatebtn=Button(frame2,text='Update',font="lucida 15 bold",width=10,command=update)
    updatebtn.grid(row=5,column=5)

    exitbtn=Button(frame2,text='Exit',font="lucida 15 bold",width=10,command=exit)
    exitbtn.grid(row=6,column=5)

    root.mainloop()

def result_search_marksheet(row):
    root = Tk()
    root.title("STUDENT PROFILE")
    root.geometry("1200x800+0+0")
    root.config(bg="orange")

    # ***************** Variables***********************





    frame1 = LabelFrame(root, text='Student Details', font="lucida 20 bold", bd=10, relief=GROOVE, bg="orange")
    frame1.place(x=20, y=20, width=1150, height=270)

    nameV = StringVar(frame1, value=row[0][0])
    fnameV = StringVar(frame1, value=row[0][1])
    dobV = StringVar(frame1, value=row[0][2])
    schoolnameV = StringVar(frame1, value=row[0][3])
    rollV = StringVar(frame1, value=row[0][4])
    mnameV = StringVar(frame1, value=row[0][5])
    genderV = StringVar(frame1, value=row[0][6])
    emailV = StringVar(frame1, value=row[0][7])

    nameL = Label(frame1, text="Name", font="lucida 20 bold", bg='orange')
    nameL.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    nameE = Entry(frame1, textvariable=nameV, font="lucifda 15 bold",state="readonly")
    nameE.grid(row=0, column=1, sticky=W)

    fnameL = Label(frame1, text="Father Name", font="lucida 20 bold", bg='orange')
    fnameL.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    fnameE = Entry(frame1, textvariable=fnameV, font="lucifda 15 bold",state="readonly")
    fnameE.grid(row=1, column=1, sticky=W)

    dobL = Label(frame1, text="Date of Birth", font="lucida 20 bold", bg='orange')
    dobL.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    dobE = Entry(frame1, textvariable=dobV, font="lucifda 15 bold",state="readonly")
    dobE.grid(row=2, column=1, sticky=W)

    schoolnameL = Label(frame1, text="School Name", font="lucida 20 bold", bg='orange')
    schoolnameL.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    schoolnameE = Entry(frame1, textvariable=schoolnameV, font="lucifda 15 bold",state="readonly")
    schoolnameE.grid(row=3, column=1, sticky=W)

    rollL = Label(frame1, text="Roll Number", font="lucida 20 bold", bg='orange')
    rollL.grid(row=0, column=3, padx=50, pady=10, sticky=W)
    rollE = Entry(frame1, textvariable=rollV, font="lucifda 15 bold",state="readonly")
    rollE.grid(row=0, column=4, sticky=W)

    mnameL = Label(frame1, text="Mother name", font="lucida 20 bold", bg='orange')
    mnameL.grid(row=1, column=3, padx=50, pady=10, sticky=W)
    mnameE = Entry(frame1, textvariable=mnameV, font="lucifda 15 bold",state="readonly")
    mnameE.grid(row=1, column=4, sticky=W)

    genderL = Label(frame1, text="Gender", font="lucida 20 bold", bg='orange')
    genderL.grid(row=2, column=3, padx=50, pady=10, sticky=W)
    genderE = tkinter.ttk.Combobox(frame1, textvariable=genderV, font="lucida 15 bold", state="readonly")
    genderE['values'] = ('Male', 'Female', 'Others')
    genderE.grid(row=2, column=4)

    emailL = Label(frame1, text="Email ID", font="lucida 20 bold", bg='orange')
    emailL.grid(row=3, column=3, padx=50, pady=10, sticky=W)
    emailE = Entry(frame1, textvariable=emailV, font="lucifda 15 bold",state="readonly")
    emailE.grid(row=3, column=4, sticky=W)

    frame2 = LabelFrame(root, text='Grades Point Obtained', font="lucida 20 bold", bd=10, relief=GROOVE, bg="orange")
    frame2.place(x=20, y=300, width=1150, height=390)

    mathsV = DoubleVar(frame2,row[0][8])
    phyV = DoubleVar(frame2,row[0][9])
    chemV = DoubleVar(frame2,row[0][10])
    programmingV = DoubleVar(frame2,row[0][11])
    engV = DoubleVar(frame2,row[0][12])
    grandtotV = DoubleVar(frame2,row[0][13])
    passmarksV = DoubleVar(frame2,"33")
    totmarksV = DoubleVar(frame2,"100")
    cgpaV = DoubleVar(frame2,row[0][14])
    resultV = StringVar(frame2,row[0][15])
    gradeV = StringVar(frame2,row[0][16])
    percentageV = DoubleVar(frame2,row[0][17])

    subL = Label(frame2, text="Subject", font="lucida 20 bold", bg="orange")
    subL.grid(row=0, column=0, sticky=W, padx=50)

    subL = Label(frame2, text="Marks", font="lucida 20 bold", bg="orange")
    subL.grid(row=0, column=1, sticky=W)

    mathL = Label(frame2, text="Maths", font="lucida 15 underline", bg="orange")
    mathL.grid(row=1, column=0, sticky=W, padx=50, pady=10)
    mathE = Entry(frame2, font="lucifda 15 bold", textvariable=mathsV, width=7,state="readonly")
    mathE.grid(row=1, column=1, sticky=W)

    phyL = Label(frame2, text="Physices", font="lucida 15 underline", bg="orange")
    phyL.grid(row=2, column=0, sticky=W, padx=50, pady=10)
    phyE = Entry(frame2, textvariable=phyV, font="lucifda 15 bold", width=7,state="readonly")
    phyE.grid(row=2, column=1, sticky=W)

    chemL = Label(frame2, text="Chemistry", font="lucida 15 underline", bg="orange")
    chemL.grid(row=3, column=0, sticky=W, padx=50, pady=10)
    chemE = Entry(frame2, font="lucifda 15 bold", textvariable=chemV, width=7,state="readonly")
    chemE.grid(row=3, column=1, sticky=W)

    programmingL = Label(frame2, text="Programming", font="lucida 15 underline", bg="orange")
    programmingL.grid(row=4, column=0, sticky=W, padx=50, pady=10)
    programmingE = Entry(frame2, font="lucifda 15 bold", textvariable=programmingV, width=7,state="readonly")
    programmingE.grid(row=4, column=1, sticky=W)

    engL = Label(frame2, text="English", font="lucida 15 underline", bg="orange")
    engL.grid(row=5, column=0, sticky=W, padx=50, pady=10)
    engE = Entry(frame2, font="lucifda 15 bold", textvariable=engV, width=7,state="readonly")
    engE.grid(row=5, column=1, sticky=W)

    totalL = Label(frame2, text="Grand Total", font="lucida 15 bold", bg="orange")
    totalL.grid(row=6, column=0, sticky=W, padx=50, pady=10)
    totalE = Entry(frame2, font="lucifda 15 bold", textvariable=grandtotV, width=7,state="readonly")
    totalE.grid(row=6, column=1, sticky=W)

    passingL = Label(frame2, text="Passing Marks", font="lucida 20 bold", bg="orange")
    passingL.grid(row=0, column=3, padx=20)

    e1 = Entry(frame2, font="lucida 15 bold", width=7, textvariable=passmarksV, state="readonly")
    e1.grid(row=1, column=3)

    e2 = Entry(frame2, font="lucida 15 bold", width=7, textvariable=passmarksV, state="readonly")
    e2.grid(row=2, column=3)

    e3 = Entry(frame2, font="lucida 15 bold", width=7, textvariable=passmarksV, state="readonly")
    e3.grid(row=3, column=3)

    e4 = Entry(frame2, font="lucida 15 bold", width=7, textvariable=passmarksV, state="readonly")
    e4.grid(row=4, column=3)

    e5 = Entry(frame2, font="lucida 15 bold", width=7, textvariable=passmarksV, state="readonly")
    e5.grid(row=5, column=3)

    cpgaL = Label(frame2, text="CGPA", font="lucida 20 bold", bg="orange")
    cpgaL.grid(row=6, column=3, padx=20)

    marksL = Label(frame2, text="Total Marks", font="lucida 20 bold", bg="orange")
    marksL.grid(row=0, column=4, padx=20)

    me1 = Entry(frame2, font="lucida 15 bold", width=7, textvariable=totmarksV, state="readonly")
    me1.grid(row=1, column=4)

    me2 = Entry(frame2, font="lucida 15 bold", width=7, textvariable=totmarksV, state="readonly")
    me2.grid(row=2, column=4)

    me3 = Entry(frame2, font="lucida 15 bold", width=7, textvariable=totmarksV, state="readonly")
    me3.grid(row=3, column=4)

    me4 = Entry(frame2, font="lucida 15 bold", width=7, textvariable=totmarksV, state="readonly")
    me4.grid(row=4, column=4)

    me5 = Entry(frame2, font="lucida 15 bold", width=7, textvariable=totmarksV, state="readonly")
    me5.grid(row=5, column=4)

    cgpae5 = Entry(frame2, font="lucida 15 bold", textvariable=cgpaV, width=7,state="readonly")
    cgpae5.grid(row=6, column=4)

    resulL = Label(frame2, text="Result", font="lucida 20 bold", bg="orange")
    resulL.grid(row=0, column=5)
    resultE = Entry(frame2, font="lucida 15 bold", textvariable=resultV, width=7,state="readonly")
    resultE.grid(row=0, column=6, padx=20)

    gradeL = Label(frame2, text="Grade", font="lucida 20 bold", bg="orange")
    gradeL.grid(row=1, column=5)
    gradeE = Entry(frame2, font="lucida 15 bold", textvariable=gradeV, width=7,state="readonly")
    gradeE.grid(row=1, column=6, padx=20)

    percentageL = Label(frame2, text="Percentage", font="lucida 20 bold", bg="orange")
    percentageL.grid(row=2, column=5)
    percentageE = Entry(frame2, font="lucida 15 bold", textvariable=percentageV, width=7,state="readonly")
    percentageE.grid(row=2, column=6, padx=20)

    exitbtn = Button(frame2, text='Exit', font="lucida 15 bold", width=10, command=root.destroy)
    exitbtn.grid(row=6, column=5)

    root.mainloop()