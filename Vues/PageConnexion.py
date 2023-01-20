from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *
from Vues.ScrollableFrame import ScrollableFrame

class PageConnexion(Frame):
    """ Classe étant une frame réprésentant la page d'acceuil
    """
    def __init__(self,window):
        super(PageConnexion, self).__init__()
        self.window = window
        self.hidden = True
        self.scrollable_frame = None
        self.windowRegle = None

    def initialize(self):
        """ Fonction qui initialise la page d'accueil
        """
        for widgets in self.winfo_children():
            widgets.destroy()
        
        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        background = self.canvas.create_image(
            720.0,
            512.0,
            image=config.Config.image[0]
        )
        
        

if __name__ == "__main__":
    from config import config
    from Controller.Controller import Controller
    window = Tk(className='Accueil')

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    config.initialisation(None)
    image = config.Config.image

    MonAccueil = Accueil(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()