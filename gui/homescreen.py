from tkinter import *
import tkinter.font as font
root = Tk()  

root.iconbitmap('D:\college project\gui\image\icon.ico')
# Defining the window size
root.geometry("1300x720")
# Fixing the window size
root.resizable()
# Title bar Title
root.title('cms project')


#--------------------------------------------------------------------------------------------------------
#frames
frameL = Frame(root,borderwidth=0, relief="groove",width=640,height=1050,bg="#133c55")
frameL.grid(row=0,column=1)
frameL.pack_propagate(0)

framem = Frame(root,borderwidth=0, relief="groove",width=640,height=1050,bg="green")
framem.grid(row=0,column=2)
framem.pack_propagate(0)

framer = Frame(root,borderwidth=0, relief="groove",width=640,height=1050,bg="blue")
framer.grid(row=0,column=3)
framer.pack_propagate(0)
#--------------------------------------------------------------------------------------------------------
dashbFont = font.Font(family='Helvetica', size=90, weight='bold')
dashb = Label(frameL, text="dashboard", fg="White",bg="#133c55")
dashb['font']=dashbFont
dashb.pack()


libFont = font.Font(family='Helvetica', size=90, weight='bold')
lib = Label(framem, text="library", fg="White",bg="green")
lib['font']=libFont
lib.pack()


classvFont = font.Font(family='Helvetica', size=90, weight='bold')
classv = Label(framer, text="classes", fg="White",bg="blue")
classv['font']=classvFont
classv.pack()


root.mainloop()