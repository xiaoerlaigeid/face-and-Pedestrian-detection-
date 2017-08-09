from tkinter import *
import peopledetect
import ped
import threading
class Application(Frame):
    def say_hi(self):
        print ("hi there, everyone!")
    def detect(self):
        threading.Thread(peopledetect.detect())
    def ped(self):
        ped.detect()
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "peopledetect",
        self.hi_there["command"] = self.ped
        self.hi_there.pack({"side": "left"})
        self.right = Button(self)
        self.right["text"] = "facedetect",
        self.right["command"] = self.detect
        self.right.pack({"side": "right"})

        self.up = Button(self)
        self.up["text"] = "up",
        self.up["command"] = self.say_hi
        self.up.pack({"side": "top"})

        self.down = Button(self)
        self.down["text"] = "down",
        self.down["command"] = self.say_hi
        self.down.pack({"side": "bottom"})

        self.left = Button(self)
        self.left["text"] = "left",
        self.left["command"] = self.say_hi
        self.left.pack({"side": "left"})

        self.right = Button(self)
        self.right["text"] = "right",
        self.right["command"] = self.say_hi
        self.right.pack({"side": "right"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()

root.destroy()