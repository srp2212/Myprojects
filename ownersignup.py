from Tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import tkMessageBox
import tkFileDialog

import socket
global path 

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
       
        mm.execute("""INSERT INTO ownersignup VALUES (%s,%s,%s,%s)""",(usernames,passwords,emails,phonenos))

        aa.commit()
        
        if username.get() == "" or password.get() == "":
            tkMessageBox.showinfo("Error","Please fill the required information")
        else:
            tkMessageBox.showinfo("Welcome to %s" %usernames, "Registered Successfully...Lets Login")
        deslogin()

           
    gw = '#134e86'
    g="#0a2845#"
    gg ="white"
    global R1
    R1 = Tk()

    R1.geometry('712x712')
    R1.title('SigUp Now')
    #R1.configure(background='sky blue')
    R1.resizable(width = FALSE ,height= FALSE)
    Image_open = Image.open("image/y.png")
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



def dataownergui():
    
    root=Tk()
    root.geometry("400x400")
    root.title("data owner page")
    #root.configure(background='sky blue')
    Tops=Frame(root, width=1600,relief=SUNKEN)
    Tops.pack(side=TOP)

    f1=Frame(root,width=800,height=700,relief=SUNKEN)
    f1.pack(side=LEFT)
    lblInfo=Label(Tops,font=('arial',20,'bold'),text="data owners",fg="BLACK",bd=35,anchor='w')
    lblInfo.grid(row=1,column=0)
    def callback():
        path = tkFileDialog.askopenfilename()
        e.delete(0, END)  # Remove current text in entry
        e.insert(0, path)  # Insert the 'path'
        #print path
    e = Entry(root,text="")
    e.pack(side=LEFT)
    
  
    def upload():
        path = e.get()
        print path
        import sys
        import socket 
        s = socket.socket()             # Create a socket object
        host = socket.gethostname()     # Get local machine name
        port = 6043                 # Reserve a port for your service.

        s.connect((host, port))

        s.send(path)
        s.close()
        tkMessageBox.showinfo("success ", " File uploaded successfully")
           
    btnbrowse=Button(f1,bd=10,fg="black",font=('arial',7,'bold'),width=10,text="Browse",bg="light blue",justify='left',command=callback).grid(row=8,column=4)
    btnupld=Button(f1,bd=10,fg="black",font=('arial',7,'bold'),width=10,text="upload",bg="light blue",justify='center',command=upload).grid(row=20,column=1)
    
    root.mainloop()

    
def login():
    def loginto():
        aa= mysql.connector.connect(host='localhost',port= 3306,user="root",passwd="root",db="anonymous")
        mm = aa.cursor()
        username = e1.get()
        password = e2.get()
        if e1.get() == "" or e2.get() == "":
            tkMessageBox.showinfo("sorry","Please complete the required field")
        else:

            mm.execute('SELECT * FROM ownersignup WHERE username = %s AND password = %s', (username, password))
            for i in username:
                print 0
            if mm.fetchall():
                tkMessageBox.showinfo("Welcome to %s" %username, "Logged in successfully")
                R.destroy()
                dataownergui()
            
            else:
                tkMessageBox.showinfo("Error" , "Invalid Login Details")
    gw = '#134e86'
    g="#0a2845#"
    gg ="white"
    global R
    
    R = Tk()
    

    R.geometry('720x720')
    #R.configure(background='sky blue')
    R.title('Login')
    R.resizable(width = FALSE ,height= FALSE)
    Image_open = Image.open("image\y1.png")
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

