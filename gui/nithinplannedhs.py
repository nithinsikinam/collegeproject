from tkinter import *  

root = Tk()  

root.iconbitmap('D:\college project\gui\image\icon.ico')
# Defining the window size
root.geometry("200x150")
# Fixing the window size
root.resizable()
# Title bar Title
root.title('cms project')
# Title Bar Icon

def submit():
    globals()[E1.get()]=channel(E1.get())
    


channelmake=Button(root,text="new channel",command=submit)
channelmake.pack()

chname=Label(root,text="Enter Channel name:")
chname.pack()

E1 = Entry(root)
E1.pack()



class channel:
    def __init__(self,name):
        self.name= name      
        globals()[self.name+"btn"] = Button(root, text=self.name)
        globals()[self.name+"btn"].pack()
    





root.mainloop()  