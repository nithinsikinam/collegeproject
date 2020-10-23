#virson 0.1

from tkinter import *  
# from tkinter.ttk import *
import tkinter.font as font
import xml.etree.ElementTree as xml
import os
from xml.etree import ElementTree
from tkinter import messagebox
from PIL import ImageTk, Image        
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

          global profile 
          global settingB
          global icon
          global icon2
          global icon3
          self.root=root


#000000  Left manu  000000000

          LeftManu = Frame(self.root,bg="#133c55",width="350",height="1050",pady="150")
          LeftManu.pack(side=LEFT)
          LeftManu.pack_propagate(0)

          # create a profile Image
          profile = ImageTk.PhotoImage(Image.open("D:\collegeproject\gui\image\ok.png"))
          panel = Label(LeftManu, image = profile, bg="#133c55")
          panel.pack()

          #id lable
          idLabel= Label(LeftManu,text="#478214",bg="#133c55",fg="White",pady="10",font=("arial", 20, "bold"))
          idLabel.pack()

          #Email lable
          emailLabel= Label(LeftManu,text="hasanaligathamaniya476@gmail.com",bg="#133c55",fg="White",font=("arial", 13, "bold"))
          emailLabel.pack()

          #side navbar
          navFrame= Frame(LeftManu,bg="#718898",width="200",height="250")
          navFrame.place(x="80",y="250")

          #b1 manuButton1.pmg
          b1=Button(navFrame,bg="#718898",text="Manu",activebackground="#718898",pady="7",padx="70",fg="white",font=("arial", 15, "bold"))
          b1.pack()

          #b2 manuButton1.pmg
          b2=Button(navFrame,bg="#718898",text="Manu",activebackground="#718898",pady="7",padx="70",fg="white",font=("arial", 15, "bold"))
          b2.pack()

          #b3 manuButton1.pmg
          b3=Button(navFrame,bg="#718898",text="Manu",activebackground="#718898",pady="7",padx="70",fg="white",font=("arial", 15, "bold"))
          b3.pack()

          #b4 manuButton1.pmg
          b4=Button(navFrame,bg="#718898",text="Manu",activebackground="#718898",pady="7",padx="70",fg="white",font=("arial", 15, "bold"))
          b4.pack()

          #v,label
          vLabel=Label(LeftManu,text="V.0.1",fg="white",bg="#133c55")
          vLabel.place(x=5,y=615)


          #setting button
          settingB = ImageTk.PhotoImage(Image.open("D:\collegeproject\gui\image\setting2.png"))
          settingB1=Button(LeftManu,bg="#133c55",image=settingB,activebackground="#133c55")
          settingB1.place(x=280,y=580)
          
            

#000000  Right main 00000000    

          main = Frame(self.root,bg="White",width="1650",height="1050") 
          main.pack(side=RIGHT)
          main.pack_propagate(0)

#@@@@@@ three colmuns  @@@@@
          colmain = Frame(main,width="1650",height="500",bg="white")
          colmain.place(y=210,x=80)
          colmain.pack_propagate(0)

          #manu one  
          colf1 = Frame(colmain,pady="20",bg="white",width="350",height="500")
          colf1.pack(side=LEFT)
          colf1.pack_propagate(0)
          col1 = Frame(colf1,bg="#dce4e7",width="300",height="350") 
          col1.pack()
          col1.pack_propagate(0)

          icon = ImageTk.PhotoImage(Image.open("D:\collegeproject\gui\image\icon.png"))
          iconLabel=Label(col1,bg="#dce4e7",image=icon)
          iconLabel.place(y="30",x="85")

          manuLabel= Label(col1,text="Manu1",pady="40",bg="#dce4e7",fg="#233a4a",font=("arial", 20, "bold"))
          manuLabel.place(y="150",x="105")

          manuButton=Button(col1,bg="#3a6fa5",text="Manu",activebackground="#3a6fa5",pady="7",padx="55",fg="white",font=("arial", 15, "bold"))
          manuButton.place(y="250",x="63")

          #manu2
          colf2 = Frame(colmain,pady="20",bg="white",width="350",height="500")
          colf2.pack(side=LEFT)
          colf2.pack_propagate(0)
          col2 = Frame(colf2,bg="#dce4e7",width="300",height="350") 
          col2.pack()

          icon2 = ImageTk.PhotoImage(Image.open("D:\collegeproject\gui\image\icon.png"))
          iconLabel=Label(col2,bg="#dce4e7",image=icon)
          iconLabel.place(y="30",x="85")

          manuLabel= Label(col2,text="Manu1",pady="40",bg="#dce4e7",fg="#233a4a",font=("arial", 20, "bold"))
          manuLabel.place(y="150",x="105")

          manuButton=Button(col2,bg="#3a6fa5",text="Manu",activebackground="#3a6fa5",pady="7",padx="55",fg="white",font=("arial", 15, "bold"))
          manuButton.place(y="250",x="63")

          #manu3  
          colf3 = Frame(colmain,pady="20",bg="white",width="350",height="500")
          colf3.pack(side=LEFT)
          colf3.pack_propagate(0)
          col3 = Frame(colf3,bg="#dce4e7",width="300",height="350") 
          col3.pack()

          icon3 = ImageTk.PhotoImage(Image.open("D:\collegeproject\gui\image\icon.png"))
          iconLabel=Label(col3,bg="#dce4e7",image=icon)
          iconLabel.place(y="30",x="85")

          manuLabel= Label(col3,text="Manu1",pady="40",bg="#dce4e7",fg="#233a4a",font=("arial", 20, "bold"))
          manuLabel.place(y="150",x="105")

          manuButton=Button(col3,bg="#3a6fa5",text="Manu",activebackground="#3a6fa5",pady="7",padx="55",fg="white",font=("arial", 15, "bold"))
          manuButton.place(y="250",x="63")

          
         






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

