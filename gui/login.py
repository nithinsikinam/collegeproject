from tkinter import *  
import tkinter.font as font

root = Tk()  

root.iconbitmap('D:\collegeproject\gui\image\icon.ico')
# Defining the window size
root.geometry("1300x720")
# Fixing the window size
root.resizable()
# Title bar Title
root.title('cms project')
# Title Bar Icon

username=StringVar("")
password=StringVar("") 

userid="hasan"
userpass="1234"

def submit(): 
   
    succ=""
    err=""

    name=username.get() 
    passw=password.get() 
      
    # print("The name is : " + name) 
    # print("The password is : " + passw) 
      
    username.set("") 
    password.set("") 

    if userid == name and userpass==passw:
        # succ= Label(innerFrame,text="You are logged in successfully",bg="#fff",padx="30",fg="green")
        # succ.pack()
        print("good")

    else:
        # err= Label(innerFrame,text="Username or password wrong!",bg="#fff",padx="30",fg="red")
        # err.pack()
        print("bad")
      

#Left side poster design
#-----------------------------------------------------------------------------------
posterFont = font.Font(family='Helvetica', size=90, weight='bold')

frameLeft = Frame(root,borderwidth=0, relief="groove",width=900,height=1050,bg="#133c55",pady=220)
frameLeft.pack(side=LEFT)
frameLeft.pack_propagate(0)

poster = Label(frameLeft, text="Poster", fg="White",bg="#133c55")
poster['font']=posterFont
poster.pack()
#Right Login form design
#------------------------------------------------------------------------------------
loginFont = font.Font(family='Helvetica', size='30')



frameRight = Frame(root,width=1020,height=1050,bg="#84d2f6",pady="60",padx="10")
frameRight.pack(side=RIGHT)
frameRight.pack_propagate(0)

loginForm = Frame(frameRight,bg="#fff",pady="30",width=500,height=400)
loginForm.pack()
loginForm.pack_propagate(0)


loginTitle= Label(loginForm,text="Sign in",bg="#fff",fg="#386fa4")
loginTitle['font']=loginFont
loginTitle.pack()

innerFrame = Frame(loginForm,bg="#fff",pady="30",width=500,height=250)
innerFrame.pack(side=LEFT)
innerFrame.pack_propagate(0)

usernameTitle= Label(innerFrame,text="Username",bg="#fff",padx="30")
usernameTitle.pack()

usernameEntery = Entry(innerFrame,bg="#e3e6e8",fg="#3e3f40",bd="1",relief="solid",textvariable = username)
usernameEntery.pack(ipadx=30,ipady=3)

passTitle= Label(innerFrame,text="Password",bg="#fff",padx="30")
passTitle.pack()

passEntery = Entry(innerFrame,bg="#e3e6e8",fg="#3e3f40",bd="1",relief="solid", show='*',textvariable = password)
passEntery.pack(ipadx=30,ipady=3)

buttonFrame = Frame(innerFrame,bg="#fff",pady="10")
buttonFrame.pack()

loginButton = Button(buttonFrame,text="Sign in",command= submit)
loginButton.pack()




root.mainloop()  