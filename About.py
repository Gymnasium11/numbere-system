# Importing the necessary libraries

from tkinter import *
import tkinter.ttk as ttk

# the main class for displaying the about us window

class About:

  def __init__(self, master, *args):

    '''Initialize and create the main window with the main parameters'''

    master.title("About")

    master.geometry('350x600')
    master.maxsize(width=350, height=600)
    master.minsize(width=350, height=600)

  

