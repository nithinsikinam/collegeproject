import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class mygridlayout(GridLayout):
    def __init__(self,**kwargs):
        

class myapp(App):
    def build(self):
        return Label(text="hello my friend")

if __name__=="__main__":
    myapp().run()

