#module for encrypting text
from cryptography.fernet import Fernet

# def key():
#     key= Fernet.generate_key()
#     #wb is write in bytes
#     with open("key.key", "wb") as key_f: 
#         key_f.write(key)

# key()

def load_key():
    #rb is read byte
    file=open("key.key", "rb")
    key=file.read()
    file.close()
    return key


#encode converts strings
key=load_key() 
fer=Fernet(key)
def view(): 
    with open('passwords.txt', "r") as f:
        for lines in f.readlines():
            data=lines.rstrip()
            user, pwd =data.split("|")
            print("site:",user , "pass:",fer.decrypt(pwd.encode()))

def add():
    name=input("enter site's name:")
    pwd=input("enter your password:")

#w; write, r: read; a: append 
#using w, it closes automatically, with variable method, we have to manually close it. 
    with open('passwords.txt', 'a') as f:
       f.write(name + "|" + fer.encrypt(pwd.encode()).decode()  +"\n")


while True:
   action=input("add a new password(add), quit(quit) or view your passwords(view)?")
   if action=="add":
       add()
   elif action=="quit":
        break
   elif action=="view":
       view()
   else:
       print("bruh.")
       continue
