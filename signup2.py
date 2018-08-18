from Tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import tkMessageBox
import Tkinter as tk
import os, sys

def desigup():
    R.destroy()
    sigup()
    
def sigup():
    def Sigups():
        usernames = username.get()
        passwords = password.get()
        emails=email.get()
        phonenos=phoneno.get()
                        
        aa= mysql.connector.connect(host='localhost',port= 3306,user="root",passwd="root",db="anonymous")
        mm = aa.cursor()
        #mm.execute("CREATE TABLE IF NOT EXISTS singup ( username varchar(30) not null, passwords int(30), email varchar(30), phoneno varchar(20))")
        #mm.execute("""INSERT INTO singup VALUES (%s,%s,%s,%s)""",(usernames,passwords,email,phoneno))
       
        mm.execute("""INSERT INTO usersignup VALUES (%s,%s,%s,%s)""",(usernames,passwords,emails,phonenos))
        aa.commit()
        
        if username.get() == "" or password.get() == "":
            tkMessageBox.showinfo("Error","Please fill the required information")
        else:
            tkMessageBox.showinfo("Welcome to %s" %usernames, "Registered Successfully....Lets Login")
        
        
        deslogin()
        
    gw = '#134e86'
    g="#0a2845#"
    gg ="white"
    global R1
    R1 = Tk()

    R1.geometry('712x712')
    R1.title('SigUp Now')
    R1.resizable(width = FALSE ,height= FALSE)
    Image_open = Image.open("image/z.png")
    image = ImageTk.PhotoImage(Image_open)
    sigup = Label(R1,image=image,bg=gg)
    sigup.place(x=0,y=0,bordermode="outside")
    username=Entry(R1,width=20,font=("bold",15),highlightthickness=2,bg=gg,relief=SUNKEN)
    username.place(x=242,y= 140 )
    password=Entry(R1,width=20,show="*",font=("bold",15),highlightthickness=2,bg=gg,relief=SUNKEN)
    password.place(x=242,y=190 )
    email=Entry(R1,width=20,font=("bold",15),highlightthickness=2,bg=gg,relief=SUNKEN)
    email.place(x=242,y= 240 )
    phoneno=Entry(R1,width=20,font=("bold",15),highlightthickness=2,bg=gg,relief=SUNKEN)
    phoneno.place(x=242,y= 290 )
    loginbt = Button(R1,text = "Login",width=10,height=2,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=deslogin)
    signUpbt = Button(R1,text = "SignUp",width=10,height=2,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=Sigups)
    loginbt.place(x =225 ,y=350)
    signUpbt.place( x =400,y=350)
    R1.mainloop()

    
def datausergui():
    root=Tk()
    root.geometry("300x300")
    root.title("data user page")

    Tops=Frame(root, width=1600,relief=SUNKEN)
    Tops.pack(side=TOP)

    f1=Frame(root,width=800,height=700,relief=SUNKEN)
    f1.pack(side=LEFT)

    lblInfo=Label(Tops,font=('arial',20,'bold'),text="data users",fg="BLACK",bd=35,anchor='w')
    lblInfo.grid(row=1,column=0)
    def files():
        def printSomething():
            import glob
            import os
            from glob import glob

            files = glob('*.pdf')
            files.extend(glob('*.txt'))
            files.extend(glob('*.docx'))

            print files
            for word in files:
                print(word)

            
                label = Label(root, text= str(word))
                # this creates x as a new label to the GUI
                label.pack()
    
   
                
        
        root = Tk()
        root.geometry("600x600")
        root.title("simpfile list")
        button = Button(root, text="file list", command=printSomething) 
        button.pack()

        root.mainloop()
    def download():
        master = Tk()
        def show_entry_fields():
           #print("Filename: %s\nkey: %s" % (e1.get(), e2.get()))
           filename1 = ""
           key1 = ""
           filename1 = e1.get()
           key1 = e2.get()
           condition = 0
           aa= mysql.connector.connect(host='localhost',port= 3306,user="root",passwd="root",db="anonymous")
           mm = aa.cursor() 
           #mm.execute('SELECT * FROM data WHERE filename = %s AND key = %s', (filename1, key1))           
           mm.execute('SELECT * FROM data WHERE filename = %s AND key1 = %s', (filename1, key1))
           #mm.execute('SELECT * FROM data')    
           if mm.fetchall():
               tkMessageBox.showinfo("success ", "KEY and file is matched..")
               tkMessageBox.showinfo("success ", "downloading file....")
               file = open(filename1, 'r') 
               #print file.read()
               
               encrcontent = file.read()
               print encrcontent
               from Crypto.Cipher import AES
               obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
               normalagain = obj2.decrypt(encrcontent)
               print normalagain

               filedecr = 'users/'+filename1
               file1 = open(filedecr,'w')
               file1.write(normalagain)
               file1.close()
 
            
           else:
               tkMessageBox.showinfo("Error" , "Invalid Key or Filename")
               
        
        Label(master, text="Filename").grid(row=0)
        Label(master, text="key").grid(row=1)

        e1 = Entry(master)
        e2 = Entry(master)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        #Button(master, text='Download').grid(row=3, column=1, sticky=W, pady=4)
        #Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
        Button(master, text='Download', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

        mainloop( )
        
       
    btndupdfiles=Button(f1,bd=20,fg="black",font=('arial',10,'bold'),width=10,text="files list",bg="white",justify='left',command=files).grid(row=3,column=4)

    btndwnldr=Button(f1,bd=20,fg="black",font=('arial',10,'bold'),width=10,text="download",bg="white",justify='center',command=download).grid(row=8,column=4)

    root.mainloop()
    
        
    #btndupdfiles=Button(f1,bd=20,fg="black",font=('arial',10,'bold'),width=10,text="files list",bg="white",justify='left',command=files).grid(row=3,column=4)

    #btndwnldr=Button(f1,bd=20,fg="black",font=('arial',10,'bold'),width=10,text="download",bg="white",justify='center',command=download1).grid(row=8,column=4)

    #root.mainloop()
    
def login():
    def loginto():
        aa= mysql.connector.connect(host='localhost',port= 3306,user="root",passwd="root",db="anonymous")
        mm = aa.cursor()
        username = e1.get()
        password = e2.get()
        if e1.get() == "" or e2.get() == "":
            tkMessageBox.showinfo("Error","Please,fill the required information")
        else:

            mm.execute('SELECT * FROM usersignup WHERE username = %s AND password = %s', (username, password))
            for i in username:
                print 0
            if mm.fetchall():
                tkMessageBox.showinfo("Welcome to %s" %username, "Logged in successfully")
                R.destroy()
                datausergui()
            
            else:
                tkMessageBox.showinfo("Error" , "Invalid Login Details")
                        
    gw = '#134e86'
    g="#0a2845#"
    gg ="white"
    global R
    R = Tk()
    R.geometry('720x720')
    R.title('Login')
    R.resizable(width = FALSE ,height= FALSE)
    Image_open = Image.open("image\z1.png")
    R.winfo_x()
    R.winfo_y()
    image = ImageTk.PhotoImage(Image_open)
    logo = Label(R,image=image,bg=gg)
    logo.place(x=0,y=0,bordermode="outside")
    e1=Entry(R,width=20,font=("bold",15),highlightthickness=2,bg=gg,relief=SUNKEN)
    e1.place(x=242,y=230 )
    e2=Entry(R,width=20,show="*",font=("bold",15),highlightthickness=2,bg=gg,relief=SUNKEN)
    e2.place(x=242,y=290 )
    loginbt = Button(R,text = "Login",width=10,height=2,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command = loginto)
    signUpbt = Button(R,text = "SignUp",width=10,height=2,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=desigup)
    loginbt.place(x =225 ,y=500)
    signUpbt.place( x =400,y=500)
    R.mainloop()
    
def deslogin():
    R1.destroy()
    login()
    



