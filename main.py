#!/usr/bin/env python3
from tkinter import *
import time
from PIL import Image, ImageTk

class App(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image = Image.open("./assets/smiley.jpg")
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

root = Tk()
root.attributes("-fullscreen", True)
container = App(root)
container.pack(fill=BOTH, expand=YES)
container.configure(background="red")
root.mainloop()
