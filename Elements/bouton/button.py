from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import pyglet as pg


class button():

    """
    Cette fonction permet de créer un rectangle avec des bords arrondis
    params :
        - X1, coordonnée haut gauche
        - Y1, coordonnée bas gauche
        - X2, coordonnée haut droit
        - Y2, coordonnée bas droit
    """
    def load(self):
        self.image = []
        self.image.append(PhotoImage(file="Accueil/assets/frame0/image_1.png")) #0
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_2.png")) #1
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_3.png")) #2
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_4.png")) #3
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_5.png")) #4
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_1.png")) #5


    def getImage(self, index: int):
        return self.image[index]


#---------------#
#    Exemple    #
#---------------#
# root = tk.Tk()
# btn = RoundedButton(text="Hors ligne", radius=100, hauteur=128, largueur=500, fontsize=32, btnbackground="#0078ff", btnforeground="#ffffff", clicked=func)
# btn.pack(expand=True, fill="both")
# root.mainloop()