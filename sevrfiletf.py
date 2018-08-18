# server.py
import mysql.connector
import socket
import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

port = 6042               # Reserve a port for your service.
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

    #print 'efore'
    print data
    z = os.path.basename(data)
    print z
    #print 'after'
    
    
    import datetime
    f = open(data,"r") 
    '''def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
        return datetime.datetime.now().strftime(fmt).format(fname=fname)
    fname = timeStamped('new.txt')
    print fname;'''
    message = f.read()
    #with open(fname,'w') as outf:
         #outf.write(message)

    
    obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
    ciphertext = obj.encrypt(message)
    # print ciphertext
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
