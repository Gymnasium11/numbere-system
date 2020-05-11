# Importing the necessary libraries

import sys
from PIL import Image, ImageTk
from tkinter import *
from tkinter.ttk import Frame, Label
import sys


# the main class for displaying the about us window

class About(Frame):

  def __init__(self):
        super().__init__()

        self.loadImage()
        self.initUI()

  def loadImage(self):
      try:
          self.img = Image.open("star.ico")

      except IOError:
          print("Unable to load image")
          sys.exit(1)

  def initUI(self):
      self.master.title("About")

      star = ImageTk.PhotoImage(self.img)
      label = Label(self, image=star)

      # reference must be stored

      label.image = star

      label.pack()
      self.pack()

  def setGeometry(self):
        w, h = self.img.size
        self.master.geometry(("%dx%d+300+300") % (w, h))
