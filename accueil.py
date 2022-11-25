from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *

class Accueil(Frame):
    def __init__(self,window,image_list):
        super()
        # OUTPUT_PATH = Path(__file__).parent
        # ASSETS_PATH = OUTPUT_PATH / Path(r"Accueil/assets/frame0")


        # def relative_to_assets(path: str) -> Path:
        #     return ASSETS_PATH / Path(path)
        self.window = window
        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        background = canvas.create_image(
            720.0,
            512.0,
            image=image_list[0]
        )

        # button_load = RoundedButton(window, text="Hors ligne", radius=100, hauteur=128, largueur=500, fontsize=32, btnbackground="#0078ff", btnforeground="#ffffff", clicked=func)


        HorsLigneBouton = canvas.create_image(
            470, 
            324, 
            image=image_list[5],
            anchor=tkinter.NW
        )
        # canvas.tag_bind(HorsLigneBouton, "<Button-1>", self.HorsLigneBouton)


        EnLigneBouton = canvas.create_image(
            470, 
            488, 
            image=image_list[1],
            anchor=tkinter.NW
        )
        # canvas.tag_bind(EnLigneBouton, "<Button-1>", self.EnLigneBouton)



        QuitterBouton = canvas.create_image(
            470, 
            652, 
            image=image_list[2],
            anchor=tkinter.NW
        )
        canvas.tag_bind(QuitterBouton, "<Button-1>", self.QuitterBouton)

        


        BoutonScore = canvas.create_image(
            1032, 
            821, 
            image=image_list[3],
            anchor=tkinter.NW
        )
        # canvas.tag_bind(BoutonScore, "<Button-1>", self.BoutonScore)


        BoutonInfo = canvas.create_image(
            334, 
            821, 
            image=image_list[4],
            anchor=tkinter.NW
        )
        # canvas.tag_bind(BoutonInfo, "<Button-1>", self.BoutonInfo)

    def QuitterBouton(self,event):
        self.window.destroy()
    
    def BoutonInfo(self,event):
        self.window.destroy()
    
    def BoutonScore(self,event):
        self.window.destroy()
    
    def EnLigneBouton(self,event):
        self.window.destroy()
    
    def HorsLigneBouton(self,event):
        self.window.destroy()


if __name__ == "__main__":

    window = Tk(className='Accueil')

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    image = config.tableauImage()

    MonAccueil = Accueil(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()
