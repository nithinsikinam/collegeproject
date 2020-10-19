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


#Left side poster design
#-----------------------------------------------------------------------------------
myFont = font.Font(family='Helvetica', size=90, weight='bold')

frameLeft = Frame(root,borderwidth=1, relief="groove",width=700,height=802,bg="#12dea7",pady=220)
frameLeft.pack(side=LEFT)
frameLeft.pack_propagate(0)

poster = Label(frameLeft, text="Poster", fg="White",bg="#12dea7")
poster['font']=myFont
poster.pack()
#Right Login form design
#------------------------------------------------------------------------------------
frameRight = Frame(root,borderwidth=0, relief="groove",width=850,height=802,bg="#fff",pady="60",padx="10")
frameRight.pack(side=RIGHT)
frameRight.pack_propagate(0)

loginForm = Frame(frameRight,borderwidth=1, relief="groove",width=500,height=500,bg="#000000")
loginForm.pack()
loginForm.pack_propagate(0)




root.mainloop()  