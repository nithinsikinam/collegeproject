import kivy
from kivy.app import App
from kivy.uix.label import Label

class myapp(App):
    def build():
        return Label(text="hello my friend")

if __name__=="__main__":
    myapp().build()

