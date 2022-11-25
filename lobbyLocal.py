from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import tkinter
import sys
from config import *

class lobbyLocal(Frame):
    def __init__(self,window,image_list):
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
        Arriere_plan = canvas.create_image(
            720.0,
            512.0,
            image=image_list[14]
        )

        Bouton_Rouge = canvas.create_image(
            279.0,
            883.0,
            image=image_list[22]
        )

        canvas.create_text(
            157.639892578125,
            840.0,
            anchor="nw",
            text="PERSONNE 3",
            fill="#FFFFFF",
            font=("LilitaOne", 48 * -1)
        )

        Bouton_Jouer = canvas.create_image(
            719.0,
            464.0,
            image=image_list[17]
        )

        Bouton_Quitter = canvas.create_image(
            717.0,
            577.0,
            image=image_list[19]
        )


        Bouton_Bleu = canvas.create_image(
            1156.0,
            883.0,
            image=image_list[15]
        )

        canvas.create_text(
            1034.639892578125,
            840.0,
            anchor="nw",
            text="PERSONNE 4",
            fill="#FFFFFF",
            font=("LilitaOne", 48 * -1)
        )


        Noir_IA_Bleu_1 = canvas.create_image(
            1266.0,
            683.04345703125,
            image=image_list[18]
        )

        canvas.create_text(
            1194.0,
            657.04345703125,
            anchor="nw",
            text="FACILE",
            fill="#FFFFFF",
            font=("LilitaOne", 32 * -1)
        )

        Noir_IA_Bleu_2 = canvas.create_image(
            1266.91796875,
            622.521728515625,
            image=image_list[18]
        )

        canvas.create_text(
            1194.91796875,
            596.521728515625,
            anchor="nw",
            text="MOYEN",
            fill="#FFFFFF",
            font=("LilitaOne", 32 * -1)
        )

        Noir_IA_Bleu_3 = canvas.create_image(
            1266.0,
            562.0,
            image=image_list[18]
        )

        canvas.create_text(
            1194.0,
            536.0,
            anchor="nw",
            text="EXPERT",
            fill="#FFFFFF",
            font=("LilitaOne", 32 * -1)
        )

        Bouton_Vert = canvas.create_image(
            1156.0,
            147.0,
            image=image_list[25]
        )

        canvas.create_text(
            1034.639892578125,
            104.0,
            anchor="nw",
            text="PERSONNE 2",
            fill="#FFFFFF",
            font=("LilitaOne", 48 * -1)
        )

        Bouton_Jaune = canvas.create_image(
            279.0,
            147.0,
            image=image_list[16]
        )

        canvas.create_text(
            157.639892578125,
            104.0,
            anchor="nw",
            text="PERSONNE 1",
            fill="#FFFFFF",
            font=("LilitaOne", 48 * -1)
        )

        Bouton_Robot_gris_X = canvas.create_image(
            139.0,
            256.0,
            image=image_list[20]
        )

        image_12 = canvas.create_image(
            1295.0,
            256.0,
            image=image_list[20]
        )

        image_image_13 = PhotoImage(
            file=relative_to_assets("image_13.png"))
        image_13 = canvas.create_image(
            1185.0,
            775.0,
            image=image_image_13
        )

        image_image_14 = PhotoImage(
            file=relative_to_assets("image_14.png"))
        image_14 = canvas.create_image(
            1185.0,
            256.0,
            image=image_image_14
        )

        image_image_15 = PhotoImage(
            file=relative_to_assets("image_15.png"))
        image_15 = canvas.create_image(
            249.0,
            256.0,
            image=image_image_15
        )

        image_image_16 = PhotoImage(
            file=relative_to_assets("image_16.png"))
        image_16 = canvas.create_image(
            249.0,
            775.0,
            image=image_image_16
        )

        image_image_17 = PhotoImage(
            file=relative_to_assets("image_17.png"))
        image_17 = canvas.create_image(
            139.0,
            775.0,
            image=image_image_17
        )

        image_image_18 = PhotoImage(
            file=relative_to_assets("image_18.png"))
        image_18 = canvas.create_image(
            1295.0,
            775.0,
            image=image_image_18
        )






if __name__ == "__main__":
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")

    image = config.tableauImage()

    MonAccueil = lobbyLocal(window,image)
    # MonAccueil.pack()
    window.resizable(False, False)
    window.mainloop()
