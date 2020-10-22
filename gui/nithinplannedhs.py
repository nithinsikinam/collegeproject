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

class channel:
    def __init__(self,name,type):
        self.name= name
        self.type= type       
        globals()[self.name] = Button(root, text=self.name)
        globals()[self.name].pack()
    

bca=channel("bca","ok")
bsc=channel("bsc","done")
b_com=channel("b_com","hello")


root.mainloop()  