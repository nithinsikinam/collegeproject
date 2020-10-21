#virson 0.1

from tkinter import *  
# from tkinter.ttk import *
import tkinter.font as font
import xml.etree.ElementTree as xml
import os
from xml.etree import ElementTree
from tkinter import messagebox
           
#==========Login=============
class Login:
    def __init__(self,root):

        self.root=root

#~~~~~~~~~~~~~~~~~~~~~on click function for submit button~~~~~~~~~~~~~~~~~~~~~

        username=StringVar("")
        password=StringVar("") 

        userid="hasan"
        userpass="1234"

        def submit(): 

            name=username.get() 
            passw=password.get() 

            username.set("") 
            password.set("") 

            if userid == name and userpass==passw:

               #=========session for storing data============ 
                def GenerateXML(fileName):
                    root=xml.Element("root")
                    cl=xml.Element("login")
                    root.append(cl)
                    type1=xml.SubElement(cl,"username")
                    type1.text=name

                    Amount1=xml.SubElement(cl,"password")
                    Amount1.text=passw

                    tree=xml.ElementTree(root)
                    with open(fileName,"wb") as files:
                        tree.write(files)

                if __name__=="__main__":
                    GenerateXML("session_pin.xml")
                    
                frameLeft.destroy()
                frameRight.destroy()
                obj=Home(root)    

            else:
            
                messagebox.showinfo("Login", "Username or password wrong!")

 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~           

        #Left side poster design
        #-----------------------------------------------------------------------------------
        posterFont = font.Font(family='Helvetica', size=90, weight='bold')

        frameLeft = Frame(self.root,borderwidth=0, relief="groove",width=900,height=1050,bg="#133c55",pady=220)
        frameLeft.pack(side=LEFT)
        frameLeft.pack_propagate(0)

        poster = Label(frameLeft, text="Poster", fg="White",bg="#133c55")
        poster['font']=posterFont
        poster.pack()
        #Right Login form design
        #------------------------------------------------------------------------------------

        #sign in font style
        loginFont = font.Font(family='Helvetica', size='30')



        frameRight = Frame(self.root,width=1020,height=1050,bg="#84d2f6",pady="60",padx="10")
        frameRight.pack(side=RIGHT)
        frameRight.pack_propagate(0)

        loginForm = Frame(frameRight,bg="#fff",pady="40",padx="50",width=350,height=300)
        loginForm.pack()
        loginForm.pack_propagate(0)

        #sign in label
        loginTitle= Label(loginForm,text="Sign in",bg="#fff",fg="#386fa4")
        loginTitle['font']=loginFont
        loginTitle.place(x="60",y="-20")

        #for input frame
        innerFrame = Frame(loginForm,bg="#fff",pady="30",width=500,height=250)
        innerFrame.place(x="0",y="30")
        innerFrame.pack_propagate(0)

        #username label
        usernameTitle= Label(innerFrame,text="Username",bg="#fff",padx="30")
        usernameTitle.place(x="0",y="-10")

        #username Entery input
        usernameEntery = Entry(innerFrame,bg="#ededed",fg="#3e3f40",bd="1",relief="solid",textvariable = username)
        usernameEntery.place(x="35",y="20")

        #Password label
        passTitle= Label(innerFrame,text="Password",bg="#fff",padx="30")
        passTitle.place(x="0",y="50")

        #Password Entery input
        passEntery = Entry(innerFrame,bg="#ededed",fg="#3e3f40",bd="1",relief="solid", show='*',textvariable = password)
        passEntery.place(x="35",y="80")


        #Sign in button
        loginButton = Button(innerFrame,text="Sign in",command= submit)
        loginButton.place(x="95",y="120")

#==========Home screen===========
class Home:
    def __init__(self,root):

        self.root=root
        self.label=Label(text="dddddd").pack()



root = Tk()  

#==========checking he session======

#   usernameDb="hasan"
#   passwordDb="ali"

filename= "session_pin.xml"
fullfile= os.path.abspath(os.path.join( filename))

dom = ElementTree.parse(fullfile)

username = dom.findall('login/username')
password = dom.findall('login/password')

for c in username:

    usernamexml = c.text

for l in password:

    passwordxml = l.text

    if usernamexml == 'hasan' and passwordxml == '1234':
       obj=Home(root)
    else:
       obj=Login(root)

           
root.iconbitmap('D:\collegeproject\gui\image\icon.ico')
# Defining the window size
root.geometry("1300x720")
# Fixing the window size
root.resizable()
# Title bar Title
root.title('cms project')
# Title Bar Icon
root.mainloop()

