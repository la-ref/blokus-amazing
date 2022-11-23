from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import sys
from Elements.bouton.button import *
from PIL import Image, ImageTk


class Accueil(Frame):
    def __init__(self,image_list):
        super()
        # OUTPUT_PATH = Path(__file__).parent
        # ASSETS_PATH = OUTPUT_PATH / Path(r"Accueil/assets/frame0")


        # def relative_to_assets(path: str) -> Path:
        #     return ASSETS_PATH / Path(path)

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
        image_image_1 = PhotoImage(
            file=image_list[0])
        image_1 = canvas.create_image(
            720.0,
            512.0,
            image=image_image_1
        )
        def quitGame(event):
            window.destroy()

        # button_load = RoundedButton(window, text="Hors ligne", radius=100, hauteur=128, largueur=500, fontsize=32, btnbackground="#0078ff", btnforeground="#ffffff", clicked=func)


        quitImage = ImageTk.PhotoImage(Image.open("Accueil/assets/frame0/button_1.png"))
        quitButton = canvas.create_image(470, 324, image=quitImage, anchor=tk.NW)
        canvas.tag_bind(quitButton, "<Button-1>", quitGame)


        button_image_2 = PhotoImage(
            file=image_list[1])
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=470.0,
            y=488.0,
            width=500.0,
            height=128.0
        )

        button_image_3 = PhotoImage(
            file=image_list[3])
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=470.0,
            y=652.0,
            width=500.0,
            height=128.0
        )

        button_image_4 = PhotoImage(
            file=image_list[4])
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=1032.0,
            y=821.0,
            width=80.0,
            height=80.0
        )

        button_image_5 = PhotoImage(
            file=image_list[5])
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=334.0,
            y=821.0,
            width=80.0,
            height=80.0
        )


if __name__ == "__main__":

    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")


    image = []
    image.append(ImageTk.PhotoImage(Image.open("Accueil/assets/frame0/image_1.png")))
    image.append(ImageTk.PhotoImage(Image.open("Accueil/assets/frame0/button_2.png")))
    image.append(ImageTk.PhotoImage(Image.open("Accueil/assets/frame0/button_3.png")))
    image.append(ImageTk.PhotoImage(Image.open("Accueil/assets/frame0/button_4.png")))
    image.append(ImageTk.PhotoImage(Image.open("Accueil/assets/frame0/button_5.png")))

    MonAccueil = Accueil(image)
    MonAccueil.pack()

    window.mainloop()
