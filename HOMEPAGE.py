from Tkinter import*
import datetime
import tkMessageBox
import mysql.connector
import socket
import time
import os, random
from Crypto.Cipher import AES
#from Crypto.Hash import SHA256



def server():
                       # Import socket module

    port = 6043                  # Reserve a port for your service.
    s = socket.socket()             # Create a socket object
    host = socket.gethostname()     # Get local machine name
    s.bind((host, port))            # Bind to the port
    s.listen(5)                     # Now wait for client connection.

    print 'Server listening....'

    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        print addr
        data = conn.recv(1024)
        print('Server received', repr(data))
        print data
        z = os.path.basename(data)
        print z

        f = open(data,"r") 
        message = f.read()
    
        obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
        ciphertext = obj.encrypt(message)
        encrfile = z
        with open(encrfile,'w') as outf:
             outf.write(ciphertext)

        for x in range(1):
            key1 = random.randint(1111,9999)
            print key1
  
        filenames = encrfile
        keys = key1
        aa= mysql.connector.connect(host='localhost',port= 3306,user="root",passwd="root",db="anonymous")
        mm = aa.cursor()
             
        mm.execute("""INSERT INTO data VALUES (%s,%s)""",(filenames,keys))

        aa.commit()
        
        print('Done sending')
        #conn.send('Thank you for connecting')
        conn.close()

       
        
        

'''
    

def owner1():
    if __name__ == "__main__":
        print "owner"
        ownersgnupmain.owner()



def user1():
    if __name__ == "__main__":
        print "user"
        #Login.test()
        usersignupmain.user()
        
'''

root=Tk()
root.geometry("450x450")
root.title("Home Page")
#root.configure(background='sky blue')
Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
localtime=time.asctime(time.localtime(time.time()))


lblInfo=Label(Tops,font=('arial',19,'bold'),text="ANONYMOUS AUTHENTICATION",fg="BLACK",bd=35,anchor='w')
lblInfo.grid(row=1,column=0)

lblInfo=Label(Tops,font=('arial',10,'bold'),text=localtime,fg="Black",bd=10,anchor='w')
lblInfo.grid(row=2,column=0)

#btndataowner=Button(f1,bd=10,fg="black",font=('arial',10,'bold'),width=10,text="data owner",bg="white",justify='center',command=owner1).grid(row=3,column=0)
#btndatausr=Button(f1,bd=10,fg="black",font=('arial',10,'bold'),width=10,text="data user",bg="white",justify='center',command=user1).grid(row=3,column=3)
#btncloudsrvr=Button(f1,bd=10,fg="black",font=('arial',10,'bold'),width=10,text="cloud server",bg="green",justify='center',command=server).grid(row=1,column=0)
btncloudsrvr=Button(f1,bd=10,fg="black",font=('arial',10,'bold'),width=10,text="cloud server",bg="green",justify='center',command=server)
btncloudsrvr.place(relx=.5, rely=.5, anchor="c")
root.mainloop()

