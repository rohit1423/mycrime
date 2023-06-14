from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import random
import sqlite3 as c
from tkinter import messagebox
from tkinter import filedialog
import os
from tkcalendar import DateEntry
import re
import subprocess



def addtables():
    conn=c.connect("crime.db")
    my_cursor=conn.cursor()
    sql="CREATE TABLE if not exists criminal (\
        caseid varchar(30),\
        criminalno varchar(30) UNIQUE,\
        ctype char(15),\
        cname varchar(20),\
        cnick varchar(10),\
        cfather varchar(50),\
        carrest varchar(50),\
        cdoc varchar(20),\
        cgender varchar(20),\
        cadd varchar(20),\
        cage varchar(20),\
        cwanted varchar(20),\
        cocc varchar(20),\
        cbm varchar(20),\
        PRIMARY KEY (caseid));"
    my_cursor.execute(sql)

    sql="CREATE TABLE if not exists login (\
        fullname varchar(30),\
        username varchar(30) UNIQUE,\
        contact varchar(30),\
        recode varchar(30),\
        pass varchar(30),\
        conpass varchar(30),\
        PRIMARY KEY (recode));"
    my_cursor.execute(sql)

def addcri():
    global caseentry
    global codeentry
    global crimecombo
    global cname
    global cnick
    global cfather
    global carrest
    global cdoc
    global cgender
    global caddress
    global cage
    global cwanted
    global cocc
    global cbirthmark
    global com_txt_search
    global txt_search
    global crime_table

    if str(caseentry.get())=="" or str(codeentry.get())=="" or str(crimecombo.get())=="" or str(cname.get())=="" or str(cnick.get())=="" or str(cfather.get())=="" or str(carrest.get())=="" or str(cdoc.get())=="" or str(cgender.get())=="" or str(caddress.get())=="" or str(cage.get())=="" or str(cwanted.get())=="" or str(cocc.get())=="" or str(cbirthmark.get())=="":
        messagebox.showerror("Error","All Fields Required",parent=root)
    elif not str(caseentry.get()).isdigit():
        messagebox.showerror("Error","Please Enter Case ID in digits",parent=root)
    elif not str(codeentry.get()).isdigit():
        messagebox.showerror("Error","Please Enter Criminal No. in digits",parent=root)
    elif not str(cname.get()).isalpha():
        messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
    elif not str(cfather.get()).isalpha():
        messagebox.showerror("Error","Please Enter Father Name in alphabets",parent=root)
    elif not str(cage.get()).isdigit():
        messagebox.showerror("Error","Please Enter Age in digits",parent=root)
    else:
        try:
            conn=c.connect("crime.db")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into criminal (caseid,criminalno,ctype,cname,cnick,cfather,carrest,cdoc,cgender,cadd,cage,cwanted,cocc,cbm)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(str(caseentry.get()),str(codeentry.get()),crimecombo.get(),str(cname.get()),str(cnick.get()),str(cfather.get()),str(carrest.get()),str(cdoc.get()),str(cgender.get()),str(caddress.get()),str(cage.get()),str(cwanted.get()),str(cocc.get()),str(cbirthmark.get())))
            conn.commit()
            fetch_datacrime() 
            messagebox.showinfo("Success","Criminal has been added",parent=root)
            conn.close()
            reset()

        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)


    root.mainloop()

def updatecri():
    global caseentry
    global codeentry
    global crimecombo
    global cname
    global cnick
    global cfather
    global carrest
    global cdoc
    global cgender
    global caddress
    global cage
    global cwanted
    global cocc
    global cbirthmark
    global com_txt_search
    global txt_search
    global crime_table

    if str(caseentry.get())=="" or str(codeentry.get())=="" or str(crimecombo.get())=="" or str(cname.get())=="" or str(cnick.get())=="" or str(cfather.get())=="" or str(carrest.get())=="" or str(cdoc.get())=="" or str(cgender.get())=="" or str(caddress.get())=="" or str(cage.get())=="" or str(cwanted.get())=="" or str(cocc.get())=="" or str(cbirthmark.get())=="":
        messagebox.showerror("Error","All Fields Required",parent=root)
    elif not str(caseentry.get()).isdigit():
        messagebox.showerror("Error","Please Enter Case ID in digits",parent=root)
    elif not str(codeentry.get()).isdigit():
        messagebox.showerror("Error","Please Enter Criminal No. in digits",parent=root)
    elif not str(cname.get()).isalpha():
        messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
    elif not str(cfather.get()).isalpha():
        messagebox.showerror("Error","Please Enter Father Name in alphabets",parent=root)
    elif not str(cage.get()).isdigit():
        messagebox.showerror("Error","Please Enter Age in digits",parent=root)
    else:
        try:
            conn=c.connect("crime.db")
            my_cursor=conn.cursor()

            sql1="UPDATE criminal SET cname='%s' WHERE caseid='%s';"%(str(cname.get()),str(caseentry.get()))
            sql2="UPDATE criminal SET cnick='%s' WHERE caseid='%s';"%(str(cnick.get()),str(caseentry.get()))
            sql3="UPDATE criminal SET cfather='%s' WHERE caseid='%s';"%(str(cfather.get()),str(caseentry.get()))
            sql4="UPDATE criminal SET criminalno='%s' WHERE caseid='%s';"%(str(codeentry.get()),str(caseentry.get()))
            sql5="UPDATE criminal SET cadd='%s' WHERE caseid='%s';"%(str(caddress.get()),str(caseentry.get()))
            sql6="UPDATE criminal SET cage='%s' WHERE caseid='%s';"%(str(cage.get()),str(caseentry.get()))

            my_cursor.execute(sql1)
            conn.commit()
            my_cursor.execute(sql2)
            conn.commit()
            my_cursor.execute(sql3)
            conn.commit()
            my_cursor.execute(sql4)
            conn.commit()
            my_cursor.execute(sql5)
            conn.commit()
            my_cursor.execute(sql6)
            conn.commit()

            conn.close()
            fetch_datacrime()
            messagebox.showinfo("Update","Criminal details has been updated successfully",parent=root)
            reset()
                
        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)
            fetch_datacrime()
            

def get_cursor(event=""):
    global caseentry
    global codeentry
    global crimecombo
    global cname
    global cnick
    global cfather
    global carrest
    global cdoc
    global cgender
    global caddress
    global cage
    global cwanted
    global cocc
    global cbirthmark
    global com_txt_search
    global txt_search
    global crime_table

    cusrsor_row=crime_table.focus()
    content=crime_table.item(cusrsor_row)
    row=content["values"]
    #calling reset func
    resetget()

    caseentry.insert(0,str(row[0]))
    codeentry.insert(0,str(row[1]))
    crimecombo.insert(0,str(row[2]))
    cname.insert(0,str(row[3]))
    cnick.insert(0,str(row[4]))
    cfather.insert(0,str(row[5]))
    carrest.insert(0,str(row[6]))
    cdoc.insert(0,str(row[7]))
    cgender.insert(0,str(row[8]))
    caddress.insert(0,str(row[9]))
    cage.insert(0,str(row[10]))
    cwanted.insert(0,str(row[11]))
    cocc.insert(0,str(row[12]))
    cbirthmark.insert(0,str(row[13]))

def resetget():
    caseentry.delete(0,END)
    codeentry.delete(0,END)
    crimecombo.delete(0,END)
    cname.delete(0,END)
    cnick.delete(0,END)
    cfather.delete(0,END)
    carrest.delete(0,END)
    cdoc.delete(0,END)
    cgender.delete(0,END)
    caddress.delete(0,END)
    cage.delete(0,END)
    cwanted.delete(0,END)
    cocc.delete(0,END)
    cbirthmark.delete(0,END)


def reset():
    
    caseentry.delete(0,END)
    codeentry.delete(0,END)
    cname.delete(0,END)
    cnick.delete(0,END)
    cfather.delete(0,END)
    caddress.delete(0,END)
    cage.delete(0,END)
    cocc.delete(0,END)
    cbirthmark.delete(0,END)
    x=random.randint(622321,753233)
    caseentry.insert(0,(x))

    
def deletecri():
    global caseentry
    global codeentry
    global crimecombo
    global cname
    global cnick
    global cfather
    global carrest
    global cdoc
    global cgender
    global caddress
    global cage
    global cwanted
    global cocc
    global cbirthmark
    global com_txt_search
    global txt_search
    global crime_table

    mDelete=messagebox.askyesno("Crime Management System","Do you want to delete this criminal",parent=root)

    if str(caseentry.get())=="" or str(codeentry.get())=="" or str(crimecombo.get())=="" or str(cname.get())=="" or str(cnick.get())=="" or str(cfather.get())=="" or str(carrest.get())=="" or str(cdoc.get())=="" or str(cgender.get())=="" or str(caddress.get())=="" or str(cage.get())=="" or str(cwanted.get())=="" or str(cocc.get())=="" or str(cbirthmark.get())=="":
        messagebox.showerror("Error","All Fields Required",parent=root)
    elif not str(caseentry.get()).isdigit():
        messagebox.showerror("Error","Please Enter Case ID in digits",parent=root)
    elif not str(codeentry.get()).isdigit():
        messagebox.showerror("Error","Please Enter Criminal No. in digits",parent=root)
    elif not str(cname.get()).isalpha():
        messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
    elif not str(cfather.get()).isalpha():
        messagebox.showerror("Error","Please Enter Father Name in alphabets",parent=root)
    elif not str(cage.get()).isdigit():
        messagebox.showerror("Error","Please Enter Age in digits",parent=root)
    elif mDelete>0:
        conn=c.connect("crime.db")
        my_cursor=conn.cursor()
        id=str(caseentry.get())
        sql="delete from criminal where caseid='%s'"%(str(id))
        my_cursor.execute(sql)
        fetch_datacrime()
        conn.commit()
        conn.close()
        fetch_datacrime()
        messagebox.showinfo("Deleted","Criminal details has been deleted successfully",parent=root)
        reset()

    else:
        if not mDelete:
            return

def searchcri():
    global caseentry
    global codeentry
    global crimecombo
    global cname
    global cnick
    global cfather
    global carrest
    global cdoc
    global cgender
    global caddress
    global cage
    global cwanted
    global cocc
    global cbirthmark
    global com_txt_search
    global txt_search
    global crime_table

    conn=c.connect("crime.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from criminal where "+str(com_txt_search.get())+" LIKE '"+str(txt_search.get())+"%'")
    rows=my_cursor.fetchall()

    if len(rows)!=0:
        crime_table.delete(*crime_table.get_children(),)
        for i in rows:
            crime_table.insert("",END,values=i)
        conn.commit()
    else:
        messagebox.showerror("Error","No Criminal details found",parent=root)
    conn.close()


def printdata():
    global caseentry
    global codeentry
    global crimecombo
    global cname
    global cnick
    global cfather
    global carrest
    global cdoc
    global cgender
    global caddress
    global cage
    global cwanted
    global cocc
    global cbirthmark
    global com_txt_search
    global txt_search
    global crime_table

    conn=c.connect("crime.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from criminal")
    rows=my_cursor.fetchall()
    filename="filebill.txt"
    f=open(filename,"w")
    f.write("-"*200+"\n")
    f.write("-"*200+"\n")
    f.write("\t\t\t\t\t\t     CRIMINAL DATABASE RECORD"+"\n")
    f.write("-"*200+"\n")
    f.write("-"*200+"\n\n")
    f.write("-"*200+"\n")
    f.write("Case ID\t Criminal Code\t Type\t Name\tNickName   Father Name\tArrest Date\tCrime Date\tGender\tAddress\t  Age   Most Wanted  Occupation\t\tBirthMark")
    f.write("\n"+"-"*200)
    if len(rows)!=0:
        for i in rows:
            f.write("\n  "+i[0]+"\t    "+i[1]+"\t\t"+i[2]+"\t "+i[3]+"\t "+i[4]+"\t      "+i[5]+"\t "+i[6]+"\t"+i[7]+"\t "+i[8]+"\t "+i[9]+"\t  "+i[10]+"\t   "+i[11]+"\t\t"+i[12]+"\t  "+i[13])
            f.write("\n"+"-"*200+"\n")
    f.flush()
    f.close()
    program="notepad.exe"
    subprocess.Popen([program,filename])

def fetch_datacrime():
    global caseentry
    global codeentry
    global crimecombo
    global cname
    global cnick
    global cfather
    global carrest
    global cdoc
    global cgender
    global caddress
    global cage
    global cwanted
    global cocc
    global cbirthmark
    global com_txt_search
    global txt_search
    global crime_table

    conn=c.connect("crime.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from criminal")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        crime_table.delete(*crime_table.get_children())
        for i in rows:
            crime_table.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()


def main():
    global root
    root=Tk()
    root.geometry("1530x790+0+0")
    root.title("Crime Management System")

    lbl_title=Label(root,text="CRIME MANAGEMENT SYSTEM",font=("algerian",37,"bold"),fg="gold",bg="black")
    lbl_title.place(x=0,y=0,width=1530,height=50)

    #1st image
    
    img_1=Image.open(r"center3.jpg")
    img_1=img_1.resize((500,160),Image.ANTIALIAS)
    photoimg_1=ImageTk.PhotoImage(img_1)

    bg_lbl=Label(root,image=photoimg_1,bd=2,relief=RIDGE)
    bg_lbl.place(x=0,y=50,width=500,height=160)

    #2st image
    
    img_2=Image.open(r"center.jpg")
    img_2=img_2.resize((530,160),Image.ANTIALIAS)
    photoimg_2=ImageTk.PhotoImage(img_2)

    bg_lbl=Label(root,image=photoimg_2,bd=2,relief=RIDGE)
    bg_lbl.place(x=499,y=50,width=530,height=160)

    #3st image
    
    img_3=Image.open(r"center2.jpg")
    img_3=img_3.resize((500,160),Image.ANTIALIAS)
    photoimg_3=ImageTk.PhotoImage(img_3)

    bg_lbl=Label(root,image=photoimg_3,bd=2,relief=RIDGE)
    bg_lbl.place(x=1028,y=50,width=500,height=160)

    Main_frame=Frame(root,bd=2,relief=RIDGE,bg='white')
    Main_frame.place(x=0,y=210,width=1520,height=560)

    upper_frame=LabelFrame(Main_frame,bd=2,text="Criminal Information",font=("times new roman",15,"bold"),fg="red",bg="white",relief=RIDGE)
    upper_frame.place(x=5,y=5,width=1505,height=270)

    #entry
    global caseentry
    global codeentry
    global crimecombo
    global cname
    global cnick
    global cfather
    global carrest
    global cdoc
    global cgender
    global caddress
    global cage
    global cwanted
    global cocc
    global cbirthmark
    global com_txt_search
    global txt_search
    global crime_table

    #case ID

    caseid=Label(upper_frame,text="Case ID:",font=("arial",11,"bold"),bg="white")
    caseid.grid(row=0,column=0,padx=10,sticky=W)

    caseentry=ttk.Entry(upper_frame,width=20,font=("arial",11,"bold"))
    caseentry.grid(row=0,column=1,padx=2,sticky=W)

    x=random.randint(622321,753233)
    caseentry.insert(0,(x))

    #criminal Code

    criminalcode=Label(upper_frame,text="Criminal Code:",font=("arial",11,"bold"),bg="white")
    criminalcode.grid(row=0,column=3,padx=10,sticky=W)

    codeentry=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
    codeentry.grid(row=0,column=4,padx=2,sticky=W)

    #crime type

    crimetype=Label(upper_frame,text="Crime Type:",font=("arial",11,"bold"),bg="white")
    crimetype.grid(row=0,column=5,padx=10,sticky=W)

    codeentry=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
    codeentry.grid(row=0,column=4,padx=2,sticky=W)

    crimecombo=ttk.Combobox(upper_frame,font=("arial",11,"bold"),width=22)
    crimecombo['value']=("Murder","Terrorist","Robbery","Cyber","Other")
    crimecombo.current(0)
    crimecombo.grid(row=0,column=6,sticky=W,padx=2)

    #criminal name

    criminalname=Label(upper_frame,text="Criminal Name:",font=("arial",11,"bold"),bg="white")
    criminalname.grid(row=1,column=0,padx=10,sticky=W,pady=10)

    cname=ttk.Entry(upper_frame,width=20,font=("arial",11,"bold"))
    cname.grid(row=1,column=1,padx=2,sticky=W)

    #criminal nickname

    criminalnick=Label(upper_frame,text="Nickname:",font=("arial",11,"bold"),bg="white")
    criminalnick.grid(row=1,column=3,padx=10,sticky=W)

    cnick=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
    cnick.grid(row=1,column=4,padx=2,sticky=W)

    #criminal nickname

    criminalfather=Label(upper_frame,text="Father Name:",font=("arial",11,"bold"),bg="white")
    criminalfather.grid(row=1,column=5,padx=10,sticky=W)

    cfather=ttk.Entry(upper_frame,width=24,font=("arial",11,"bold"))
    cfather.grid(row=1,column=6,padx=2,sticky=W)

    #criminal nickname

    criminalarrest=Label(upper_frame,text="Arrest Date:",font=("arial",11,"bold"),bg="white")
    criminalarrest.grid(row=2,column=0,padx=10,sticky=W)

    carrest=DateEntry(upper_frame,selectmode='day',date_pattern='dd/mm/y',font=("arial",10,"bold"),width=20)
    carrest.grid(row=2,column=1,padx=0,pady=3)

    #criminal nickname

    criminaldoc=Label(upper_frame,text="Crime Date:",font=("arial",11,"bold"),bg="white")
    criminaldoc.grid(row=2,column=3,padx=10,sticky=W)

    cdoc=DateEntry(upper_frame,selectmode='day',date_pattern='dd/mm/y',font=("arial",10,"bold"),width=23)
    cdoc.grid(row=2,column=4,padx=2,pady=3)

    #Gender

    crimegender=Label(upper_frame,font=("arial",11,"bold"),bg="white",text="Gender:")
    crimegender.grid(row=2,column=5,sticky=W,padx=10,pady=3)

    cgender=ttk.Combobox(upper_frame,font=("arial",10,"bold"),width=25)
    cgender['value']=("Male","Female","Other")
    cgender.current(0)
    cgender.grid(row=2,column=6,sticky=W,padx=2,pady=3)

    #address

    crimeaddress=Label(upper_frame,font=("arial",11,"bold"),bg="white",text="Address:")
    crimeaddress.grid(row=3,column=0,sticky=W,padx=10,pady=7)

    caddress=ttk.Entry(upper_frame,font=("arial",11,"bold"),width=20)
    caddress.grid(row=3,column=1,padx=2,pady=7)

    #age

    crimeage=Label(upper_frame,font=("arial",11,"bold"),bg="white",text="Age:")
    crimeage.grid(row=3,column=3,sticky=W,padx=10,pady=7)

    cage=ttk.Entry(upper_frame,font=("arial",11,"bold"),width=22)
    cage.grid(row=3,column=4,padx=2,pady=7)

    #most wanted

    crimewanted=Label(upper_frame,font=("arial",11,"bold"),bg="white",text="Most Wanted:")
    crimewanted.grid(row=3,column=5,sticky=W,padx=10,pady=3)

    cwanted=ttk.Combobox(upper_frame,font=("arial",10,"bold"),width=25)
    cwanted['value']=("Yes","No")
    cwanted.current(0)
    cwanted.grid(row=3,column=6,sticky=W,padx=2,pady=3)

    #occupation

    crimeocc=Label(upper_frame,font=("arial",11,"bold"),bg="white",text="Occupation:")
    crimeocc.grid(row=4,column=0,sticky=W,padx=10,pady=7)

    cocc=ttk.Entry(upper_frame,font=("arial",11,"bold"),width=20)
    cocc.grid(row=4,column=1,padx=2,pady=7)


    #birth mark

    crimebirthmark=Label(upper_frame,font=("arial",11,"bold"),bg="white",text="Birth Mark:")
    crimebirthmark.grid(row=4,column=3,sticky=W,padx=10,pady=7)

    cbirthmark=ttk.Entry(upper_frame,font=("arial",11,"bold"),width=22)
    cbirthmark.grid(row=4,column=4,padx=2,pady=7)

    def logoutfunc():
        x=messagebox.askyesno("Logout","Do you want to logout ?",parent=root)
        if x>0:
            root.destroy()
            log()

    btn_log=Button(upper_frame,text="Logout",command=logoutfunc,font=("arial",10,"bold"),bg="midnight blue",fg="white",activeforeground="white",activebackground="midnight blue",width=17)
    btn_log.grid(row=4,column=6,pady=2)

    #button frame

    btn_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
    btn_frame.place(x=13,y=190,width=895,height=35)


    btn_Add=Button(btn_frame,text="Save",command=addcri,font=("arial",10,"bold"),bg="midnight blue",fg="white",activeforeground="white",activebackground="midnight blue",width=17)
    btn_Add.grid(row=0,column=0,padx=1,pady=2)

    btn_Update=Button(btn_frame,text="Update",command=updatecri,font=("arial",10,"bold"),bg="midnight blue",fg="white",activeforeground="white",activebackground="midnight blue",width=17)
    btn_Update.grid(row=0,column=1,padx=1,pady=2)

    btn_Delete=Button(btn_frame,text="Delete",command=deletecri,font=("arial",10,"bold"),bg="midnight blue",fg="white",activeforeground="white",activebackground="midnight blue",width=17) 
    btn_Delete.grid(row=0,column=2,padx=1,pady=2)

    btn_Reset=Button(btn_frame,text="Reset",command=reset,font=("arial",10,"bold"),bg="midnight blue",fg="white",activeforeground="white",activebackground="midnight blue",width=17)    
    btn_Reset.grid(row=0,column=3,padx=1,pady=2)

    btn_all=Button(btn_frame,text="Print Database",command=printdata,font=("arial",10,"bold"),bg="midnight blue",fg="white",activeforeground="white",activebackground="midnight blue",width=36)    
    btn_all.grid(row=0,column=4,padx=1,pady=2)


    #bg right image
    
    img_4=Image.open(r"crimelogo.jpg")
    img_4=img_4.resize((470,220),Image.ANTIALIAS)
    photoimg_4=ImageTk.PhotoImage(img_4)

    bg_lbl=Label(upper_frame,image=photoimg_4,bd=2,relief=RIDGE)
    bg_lbl.place(x=1010,y=0,width=470,height=220)



    lower_frame=LabelFrame(Main_frame,bd=2,text="Criminal Information Table",font=("times new roman",15,"bold"),fg="red",bg="white",relief=RIDGE)
    lower_frame.place(x=5,y=275,width=1505,height=270)

    search_frame=LabelFrame(lower_frame,bd=2,text="Search Criminal Record",font=("times new roman",15,"bold"),fg="red",bg="white",relief=RIDGE)
    search_frame.place(x=3,y=0,width=1494,height=60)

    search_by=Label(search_frame,font=("arial",11,"bold"),bg="red",fg="white",text="Search By:")
    search_by.grid(row=0,column=0,sticky=W,padx=5,pady=4)

    com_txt_search=ttk.Combobox(search_frame,font=("arial",11,"bold"),width=18,state="readonly")
    com_txt_search['value']=("caseid","criminalno")
    com_txt_search.current(0)
    com_txt_search.grid(row=0,column=1,sticky=W,padx=3)

    
    txt_search=ttk.Entry(search_frame,font=("arial",11,"bold"),width=25)
    txt_search.grid(row=0,column=2,padx=3)

    btn_search=Button(search_frame,text="Search",command=searchcri,font=("arial",10,"bold"),bg="midnight blue",fg="white",activeforeground="white",activebackground="midnight blue",width=18) 
    btn_search.grid(row=0,column=3,padx=3)

    btn_ShowAll=Button(search_frame,text="Show All",command=fetch_datacrime,font=("arial",10,"bold"),bg="midnight blue",fg="white",activeforeground="white",activebackground="midnight blue",width=18)
    btn_ShowAll.grid(row=0,column=4,padx=3)

    crimeagency=Label(search_frame,font=("arial",22,"bold"),bg="red",fg="white",text="NATIONAL CRIME AGENCY")
    crimeagency.grid(row=0,column=5,padx=150)


    #table work

    table_frame=Frame(lower_frame,bd=4,relief=RIDGE)
    table_frame.place(x=0,y=61,width=1495,height=170)
    
    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
    crime_table=ttk.Treeview(table_frame,column=("caseid","criminalno","ctype","cname","cnick","cfather","carrest","cdoc","cgender","cadd","cage","cwanted","cocc","cbm"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)       
        
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=crime_table.xview)
    scroll_y.config(command=crime_table.yview)

    crime_table.heading("caseid",text="Case ID")
    crime_table.heading("criminalno",text="Criminal No.")
    crime_table.heading("ctype",text="Crime Type")
    crime_table.heading("cname",text="Name")
    crime_table.heading("cnick",text="Nickname")
    crime_table.heading("cfather",text="Father Name")
    crime_table.heading("carrest",text="Arrest Date")
    crime_table.heading("cdoc",text="Crime Date")
    crime_table.heading("cgender",text="Gender")
    crime_table.heading("cadd",text="Address")
    crime_table.heading("cage",text="Age")
    crime_table.heading("cwanted",text="Most Wanted")
    crime_table.heading("cocc",text="Occupation")
    crime_table.heading("cbm",text="Birth Mark")

    crime_table["show"]="headings"

    crime_table.column("caseid",width=100,anchor=CENTER)
    crime_table.column("criminalno",width=100,anchor=CENTER)
    crime_table.column("ctype",width=100,anchor=CENTER)
    crime_table.column("cname",width=100,anchor=CENTER)
    crime_table.column("cnick",width=100,anchor=CENTER)
    crime_table.column("cfather",width=100,anchor=CENTER)
    crime_table.column("carrest",width=100,anchor=CENTER)
    crime_table.column("cdoc",width=100,anchor=CENTER)
    crime_table.column("cgender",width=100,anchor=CENTER)
    crime_table.column("cadd",width=100,anchor=CENTER)
    crime_table.column("cage",width=100,anchor=CENTER)
    crime_table.column("cwanted",width=100,anchor=CENTER)
    crime_table.column("cocc",width=100,anchor=CENTER)
    crime_table.column("cbm",width=100,anchor=CENTER)
    

    crime_table.pack(fill=BOTH,expand=1)
    crime_table.bind("<ButtonRelease>",get_cursor)
    fetch_datacrime()

    root.mainloop()

def log():
    global root
    global fname_entry
    global l_entry
    global txt_contact
    global txt_recode
    global txt_pass
    global txt_conpass
    root=Tk()
    def Register():
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global checkbtn

        root.title("Register")
        root.geometry("1600x900+0+0")

        #background image

        bg1=ImageTk.PhotoImage(file="regisf.jpg")
            
        bg1_lbl=Label(root,image=bg1,relief=RIDGE)
        bg1_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #bg 2
        bgimage=Image.open("carcrime.jpg")
        bgimage=bgimage.resize((460,550),Image.ANTIALIAS)
        bg2=ImageTk.PhotoImage(bgimage)

        
        bg2_lbl=Label(root,image=bg2,bd=4,relief=RIDGE)
        bg2_lbl.place(x=130,y=130,width=460,height=550)

        #side frame

        frame=Frame(root,bg="white")
        frame.place(x=590,y=130,width=800,height=550)

        #frame inside work

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen")
        register_lbl.place(x=20,y=20)

        #--login button--#

        loginbtnreg=Button(frame,command=Login_Window,text="Login Now",font=("Arial",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtnreg.place(x=630,y=20,width=120,height=35)

        #labels and entry fields

        framename=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="white")
        framename.place(x=50,y=100)

        #entry field for first name

        fname_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        fname_entry.place(x=50,y=135,width=230)

        #last name

        l_name=Label(frame,text="User Name",font=("times new roman",20,"bold"),bg="white")
        l_name.place(x=370,y=100)

        l_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        l_entry.place(x=370,y=136,width=230)

        #contact

        contact_name=Label(frame,text="Contact No",font=("times new roman",20,"bold"),bg="white")
        contact_name.place(x=50,y=170)

        txt_contact=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_contact.place(x=50,y=210,width=230)

        #recovery  code

        recode=Label(frame,text="Recovery Code",font=("times new roman",20,"bold"),bg="white")
        recode.place(x=370,y=170)

        txt_recode=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_recode.place(x=370,y=207,width=230)
        
        #password

        password=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="white")
        password.place(x=50,y=245)

        txt_pass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_pass.place(x=50,y=282,width=230)

        #confirm pass

        conpass=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="white")
        conpass.place(x=370,y=240)

        txt_conpass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_conpass.place(x=370,y=277,width=230)


        #check btn terms and conditions
        global var_check
        var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=var_check,text="I Agree the Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=330)
        def registerclick():
            global var_check
            global fname_entry
            global l_entry
            global txt_contact
            global txt_recode
            global txt_pass
            global txt_conpass



            if str(fname_entry.get())=="" or str(l_entry.get())=="" or str(txt_contact.get())=="" or str(txt_recode.get())=="" or str(txt_pass.get())=="" or str(txt_conpass.get())=="":
                messagebox.showerror("Error","All fields are required",parent=root)

            elif not fname_entry.get().isalpha() or not l_entry.get().isalpha():
                messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
            elif not str(txt_contact.get()).isdigit() or not str(txt_recode.get()).isdigit():
                messagebox.showerror("Error","Please Enter Digits in the desired box",parent=root)
            elif str(txt_pass.get())!=str(txt_conpass.get()):
                messagebox.showerror("Error","Password & Confirm Password must be same",parent=root)
            elif var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions",parent=root)
            else:
                messagebox.showinfo("Done","Welcome to our Crime Management System",parent=root)
                conn=c.connect("crime.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(l_entry.get())))
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist with same details\nPlease try again",parent=root)
                else:
                    my_cursor.execute("insert into login (fullname,username,contact,recode,pass,conpass)values('%s','%s','%s','%s','%s','%s')"%(str(fname_entry.get()),str(l_entry.get()),str(txt_contact.get()),str(txt_recode.get()),str(txt_pass.get()),str(txt_conpass.get())))
                    conn.commit()
                    messagebox.showinfo("Registered","Data registered successfully",parent=root)
                    conn.close()
        #register now

        img=Image.open("regisnowbtn.png")
        img=img.resize((170,50),Image.ANTIALIAS)
        photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=photoimage,borderwidth=0,command=registerclick,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=203,y=390,width=300)

        

        root.mainloop()

    def Login_Window():
        global root
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global txtuser
        global txtpass
        global txt_newpass
        
        root.title("Crime Management System Login Pannel")
        root.geometry("1550x800+0+0")

        bgimage=Image.open("bgl.jpg")
        bgimage=bgimage.resize((1550,800),Image.ANTIALIAS)
        bg=ImageTk.PhotoImage(bgimage)

        lbl_bg=Label(root,image=bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(root,bg="black")
        frame.place(x=603,y=175,width=340,height=450) #x and y pos value and width and height size of box

        img1=Image.open("get.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=180,width=100,height=100)

            #get started label

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=107,y=100)

            #user name label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=60,y=155)
            
        txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))       
        txtuser.place(x=35,y=180,width=270)

            #password label

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=60,y=225)

        txtpass=ttk.Entry(frame,font=("times new roman",13,"bold"),show="*")       
        txtpass.place(x=35,y=250,width=270)

            #Icon Images of username 

        img2=Image.open("logicon.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=330,width=25,height=25)

            #Icon Images of password

        img3=Image.open("passicon.png")
        img3=img3.resize((55,25),Image.ANTIALIAS)
        photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=639,y=400,width=25,height=25)
            
            #login btn in login pannel               here command ka kaam click karne par def login ko call karna hai
        def login():
            global txtuser
            global txtpass
            global txt_recode

            if str(txtuser.get())=="" or str(txtpass.get())=="":
                messagebox.showerror("Error","All fields required",parent=root)
            else:
                conn=c.connect("crime.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s' and pass='%s'"%(str(txtuser.get()),str(txtpass.get())))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password",parent=root)
                else:
                    root.destroy()
                    main()


        loginbtn=Button(frame,command=login,text="Login",font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtn.place(x=105,y=300,width=120,height=35)

            # registerbutton for new users

        registerbtn=Button(frame,text="New User Register",command=Register,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=5,y=353,width=160)

            #forgot passbtn
        def forgotpass():
            global txtuser
            global txtpass
            global txt_recode
            global txt_newpass

            if str(txtuser.get())=="":
                messagebox.showerror("Error","Please Enter User Name to reset Password",parent=root)
            else:
                conn=c.connect("crime.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(txtuser.get())))
                row=my_cursor.fetchone()

                if row==None:
                    messagebox.showerror("Error","Please enter valid username",parent=root)
                else:
                    conn.close()
                    root2=Toplevel()
                    root2.title("Forgot Password")
                    root2.geometry("360x480+590+170")

                    l=Label(root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="blue",bg="cyan")
                    l.place(x=0,y=10,relwidth=1)

                    #recovery  code

                    recode=Label(root2,text="Recovery Code",font=("times new roman",20,"bold"),bg="cyan")
                    recode.place(x=88,y=80)

                    txt_recode=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_recode.place(x=50,y=130,width=250)
                    
                    #password

                    newpassword=Label(root2,text="New Password",font=("times new roman",20,"bold"),bg="cyan")
                    newpassword.place(x=88,y=180)

                    txt_newpass=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_newpass.place(x=50,y=220,width=250)
                    
                    def resetpass():
                        global txtuser
                        global txt_newpass
                        global txt_recode

                        

                        if str(txt_recode.get())=="":
                            messagebox.showerror("Error","Please enter Recovery Code",parent=root2)
                        elif not str(txt_recode.get()).isdigit():
                            messagebox.showerror("Error","Please enter Recovery Code in Digits",parent=root2)
                        else:
                            conn=c.connect("crime.db")
                            my_cursor=conn.cursor()
                            my_cursor.execute("select * from login where username='%s' and recode='%s'"%(str(txtuser.get()),str(txt_recode.get())))
                            row=my_cursor.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Please enter Correct Recovery Code",parent=root2)
                            else:
                                my_cursor.execute("update login set pass='%s' where username='%s' and recode='%s'"%(str(txt_newpass.get()),str(txtuser.get()),str(txt_recode.get())))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("Info","Your password has been reset\nYou can login with your new password",parent=root2) 
                                root2.destroy()


                        



                    #btn for reset

                    btn=Button(root2,text="Reset Password",command=resetpass,font=("times new roman",15,"bold"),fg="white",bg="blue")
                    btn.place(x=100,y=290)

        forgotpassbtn=Button(frame,text="Forgot Password",command=forgotpass,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=7,y=382,width=140)

        #click login func

        

        root.mainloop()
    Login_Window()


addtables()
log()





    

