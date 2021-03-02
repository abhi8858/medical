from tkinter import *
import sqlite3 as s
from tkinter import messagebox
import requests as r
import bs4
try:
    client=s.connect("d://MA.db")
    cu=client.cursor()
    cu.execute("create table student(username varchar(50),password varchar(50),email_id varchar(50),mob_no int,address varchar(50))")
except:
    pass

def login():
    global scr,scr1,sap
    try:
        scr1.destroy()
    except:
        pass
    scr=Tk()
    scr.title("Medical Assistance")
    scr.geometry("1024x768")
    
    global username
    global password
    
    l=Label(scr,text="Login Page",bg="blue",fg="white",font="verdana 30 bold",justify=CENTER)
    l.pack(side=TOP,fill=X)
    banner1=PhotoImage(file="home_banner.png")
    l1=Label(scr, image=banner1,height=200,width=500)
    l1.pack(side=TOP,fill=X)
    
    sap = Label(scr, text="", font=('arial', 18))
    sap.place(x=250,y=500)
    e1=Entry(scr, font=('times',15,''), bd=5)
    e1.insert(0,"User ID")
    e1.place(x=430,y=350)
    e2=Entry(scr, font=('times',15,''), bd=5, show='*')
    e2.insert(0,"Password")
    e2.place(x=430,y=400)
    def b1():
        cu.execute("select count(*) from student where username=%r and password=%r"%(e1.get(),e2.get()))
        a=cu.fetchall()
        if a[0][0]==1:
            messagebox.showinfo("Login","Login Successfull...")
            main()
        else:
            messagebox.showerror("Login","Username & Password did not matched..")
    b1=Button(scr,text='Login',font=('arial', 12),width=14,bg='blue',fg='white',command=b1)
    b1.place(x=420,y=450)
    b2=Button(scr,text='register',font=('arial', 12),width=14,bg='red',fg='white',command=register)
    b2.place(x=570,y=450)
    scr.mainloop()
    

def register():
    global scr,scr1,lr
    try:
        scr.destroy()
    except:
        pass
    scr1=Tk()
    scr1.geometry('1024x768')
    scr1.title("Medical Assistance")
    global lr
    scr1.title("Register")
    scr1.geometry("800x690")
    global email_id
    global mob_no
    global address

    global username
    global password
    username=StringVar()
    password=StringVar()
    email_id=StringVar()
    mob_no=StringVar()
    address=StringVar()
   
    l=Label(scr1, text="registration page",bg="red",fg="white",font="verdana 30 bold",justify=CENTER,).pack(side=TOP,fill=X)
    
    lr = Label(scr1, text="", font=('arial', 18))
    lr.place(x=150,y=500)
    abhi = Label(scr1, text="Username:", font=('arial', 18), bd=18)
    abhi.place(x=200,y=200)
    e1=Entry(scr1,font=('times',16,'italic'))
    e1.place(x=350,y=220)
    abhi1 = Label(scr1, text="Password:", font=('arial', 18), bd=18)
    abhi1.place(x=200,y=250)
    e2=Entry(scr1,font=('times',16,'italic'))
    e2.place(x=350,y=270)
    abhi2 = Label(scr1, text="email_id:", font=('arial', 18), bd=18)
    abhi2.place(x=200,y=300)
    e3=Entry(scr1,font=('times',16,'italic'))
    e3.place(x=350,y=320)
    mobno = Label(scr1, text="mob-no:", font=('arial', 18), bd=18)
    mobno.place(x=200,y=350)
    e4=Entry(scr1,font=('times',16,'italic'))
    e4.place(x=350,y=370)
    adds = Label(scr1, text="address:", font=('arial', 18), bd=18)
    adds.place(x=200,y=400)
    e5=Entry(scr1,font=('times',16,'italic'))
    e5.place(x=350,y=420)
    
  
    
 
    r1=Radiobutton(scr1,text="male",value=1)
    r2=Radiobutton(scr1,text="female",value=2)
    r3=Radiobutton(scr1,text="others",value=3)
    r1.place(x=280,y=450)
    r2.place(x=350,y=450)
    r3.place(x=420,y=450)
    def b1():
        
        if not re.search(r'^\S+@\w+[.][a-z]{2,3}$',e3.get()):
           messagebox.showerror("Email","Invalid Email Id")
        elif not re.search(r'^\d+$',e4.get()):
            messagebox.showerror("Contact Number",'Invalid Contact Number')
        elif not re.search(r'^\S+$',e2.get()):
            messagebox.showerror("Password",'Invalid Password')
        else:
            cu.execute("insert into student(username,password,email_id,mob_no,address) values(%r,%r,%r,%d,%r)"%(e1.get(),e2.get(),e3.get(),int(e4.get()),e5.get())
                                                                                                                )

            client.commit()
            messagebox.showinfo("Registeration","Registration successfull...")
            login()
    
       
    b1=Button(scr1,text='Submit',font=('times',16,'bold'),bg='green',fg='white',command=b1)
    b1.place(x=450,y=500)
    scr1.mainloop()


def main():
    global scr
    try: 
        scr.destroy()
    except:
        pass
    scr2=Tk()
    scr2.geometry('1024x768')
    scr2.title("Medical Assistance")
    l=Label(scr2,text="Main Page",font=('times',20,'bold'),bg='blue',fg='yellow')
    l1=Label(scr2,text="Enter the medicine name",font=('times',20,'bold'))
    l1.pack()
    e1=Entry(scr2,font=('times',16,'italic'))
    e1.pack()
    def scrap():
        lst=[]
        dt=r.request('get','https://www.1mg.com/search/all?name=%s'%(e1.get()))
        s=bs4.BeautifulSoup(dt.text,'html.parser')
        for i in s.findAll('div'):
            if i.get('class'):
                if len([x for x in i.get('class') if 'style__container__' in x])>0:
                    if i.find('a'):
                        x=i.find('a')
                        try:
                    
                            dts=r.request('get','https://www.1mg.com'+x.get('href'))
                            s1=bs4.BeautifulSoup(dts.text,'html.parser')
                            for j in s1.findAll('div'):
                                if j.get('class'):
                                    if len([x for x in j.get('class') if '_product-description' in x])>0:
                                    
                                        try:
                                            lst.append(j.text)    
                                        except:
                                            pass
                                        
                                    elif  len([x for x in j.get('class') if 'DrugOverview__container' in x])>0:
                                    
                                        try:
                                            lst.append(j.text)
                                        except:
                                            pass
                        except:
                            pass

        global data,m                    
        data=iter(lst)
        m.config(text=next(data))             
    b1=Button(scr2,text='Search',font=('times',16,'bold'),bg='green',fg='white',command=scrap)
    b1.pack()
    def nexxt():
        global m,data
        try:
            m.config(text=next(data))
        except:
            m.config(text="Finish",width=200)
    global m 
    m=Message(scr2,bg='yellow')
    m.pack()
    b2=Button(scr2,text='Next',font=('times',16,'bold'),command=nexxt)    
    b2.place(x=480,y=650)
    scr2.mainloop()
login()
