from Game import Game
from tkinter import PhotoImage
import tkinter as tk
import Elements.PiecesListGUI as PG
from PIL import ImageTk
from GridInterface import GridInterface
class Abandon(tk.Frame):
    def __init__(self,image,parent,game):
        super(Abandon,self).__init__(parent)
        self.parent = parent
        self.bout = self.parent.create_image(
            (1440//2)-(image.width()//2), 
            120, 
            image=image,
            anchor=tk.NW
        )
        self.parent.tag_bind(self.bout, "<Button-1>",lambda *_: self.test())

    def test(self):
        if game.currentPlayer not in game.joueursAbandon:
            game.joueursAbandon.append(game.currentPlayer)

def task(board,game : Game):

    joueurs = game.getPlayers()
    plateau = game.getBoard()
    for joueur in joueurs:
        if joueur not in game.joueursAbandon:
            game.currentPlayer = joueur
            board.refreshPlayer(joueur.getColor())
            print("c'est a : ",joueur.getName())
            ajout = False
            pieceid = 1
            fini = False
            while not fini:
                if joueur not in game.joueursAbandon:
                    pieceid = input("Choisir pièce : ")
                    piece = joueur.getPiece(pieceid)
                    x = input("x = ")
                    y = input("y = ")
                    if joueur in game.joueursAbandon:
                        fini = True
                    if piece:
                        if joueur in game.joueursAbandon:
                            fini = True
                        if joueur not in game.joueursAbandon:
                            ajout = (plateau.ajouterPiece(piece,int(x),int(y),joueur,1,1))
                        if ajout:
                            fini = True
                else:
                    fini = True
            if joueur not in game.joueursAbandon:
                if ajout:
                    joueur.ajoutTour()
                    joueur.removePiece(str(pieceid))
                board.refreshBoard()
    window.update()


game = Game(None,None,20)

window = tk.Tk()
images = []

images.append(ImageTk.PhotoImage(file="build/assets/frame0/empty_list.png"))
images.append(PhotoImage(file="build/assets/frame0/player_yellow.png"))
images.append(PhotoImage(file="build/assets/frame0/player_green.png"))
images.append(PhotoImage(file="build/assets/frame0/player_blue.png"))
images.append(PhotoImage(file="build/assets/frame0/player_red.png"))
images.append(PhotoImage(file="build/assets/frame0/AppBorder.png"))
images.append(PhotoImage(file="build/assets/frame0/board.png"))#270x270
images.append(PhotoImage(file="build/assets/frame0/button_give_up.png"))

window.geometry("1440x1024")

border = tk.Canvas()
border.config(bg="white")
border.create_image(
        0,
        0,
        image=images[5],
        anchor=tk.NW
    )


border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
board = GridInterface(border,game.getBoard(),images)
board.move(x=720-270,y=512-270)

List1 = PG.PiecesListGUI(border,images,"Joueur 1",1)
List1.move(x=70,y=80)

List2 = PG.PiecesListGUI(border,images,"Joueur 2",2)
List2.move(x=1047,y=80)

List3 = PG.PiecesListGUI(border,images,"Joueur 3",3)
List3.move(x=1047,y=524)

List4 = PG.PiecesListGUI(border,images,"Joueur 4",4)
List4.move(x=70,y=524)

aba = Abandon(images[-1],border,game)


while 1:
    task(board,game)