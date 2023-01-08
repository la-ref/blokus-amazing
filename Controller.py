from __future__ import annotations
from Game import Game
from tkinter import PhotoImage
import tkinter as tk
import Elements.PiecesListGUI as PG
from PIL import ImageTk
from accueil import Accueil
from Player import Player
from config import config
from Pieces import Pieces
from lobbyLocal import lobbyLocal
from GameInterface import GameInterface
class Controller(tk.Tk):

    
    def __init__(self) -> None:
        tk.Tk.__init__(self)
        #self.window = tk.Tk()
        
        config.initialisation(self)
        
        self.frames = { "Acceuil" : Accueil(self), "lobbyLocal" : lobbyLocal(self), "GameInterface" : GameInterface(self)}

        self.game : Game = Game(None,None,20)
        self.geometry(str(config.Config.largueur)+"x"+str(config.Config.hauteur))
        # self.border = tk.Canvas()

        # self.border.create_image(
        #     0,
        #     0,
        #     image=PhotoImage(file="build/assets/frame0/AppBorder.png"),
        #     anchor=tk.NW
        # )
        # self.border.config(bg="white")
        # self.border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
        # self.vueJeu : GridInterface = GridInterface(self.border,self.game.getBoard())
        self.changePage('Acceuil')
        # self.vueJeu.move(x=720-270,y=512-270)
        # self.vueJeu.setController(self)
        self.mainloop()
        
    def changePage(self, nomFrame):
        self.vueJeu = self.frames[nomFrame]
        self.vueJeu.initialize()
        self.vueJeu.tkraise()
        


    # def updatePlayers(self,couleur : int):
    #     self.vueJeu.refreshPlayer(couleur)

    def updateBoard(self):
        self.vueJeu.refreshBoard(self.game.getBoard())

    def surrender(self : Controller):
        print("hihihieooozo")
        if not self.game.isPlayerSurrendered():
            self.game.addSurrenderedPlayer()
    
    def getBoard(self : Controller):
        return self.game.getBoard()

    def updateWindows(self) -> None:
        self.playing = False
        import accueil
        from config import config
        #self.window = accueil.Accueil(self.window)
        print("au revoir")
        # self.window = tk.Tk()
        # self.window.geometry("1440x1024")
        # self.window.tkraise(lobbyLocal.lobbyLocal(self.window, config.tableauImage()))

# class Abandon(tk.Frame):
#     def __init__(self,image,parent,game):
#         super(Abandon,self).__init__(parent)
#         self.parent = parent
#         self.bout = self.parent.create_image(
#             (1440//2)-(image.width()//2), 
#             120, 
#             image=image,
#             anchor=tk.NW
#         )
#         self.parent.tag_bind(self.bout, "<Button-1>",lambda *_: self.test())

#     def test(self):
#         if game.currentPlayer not in game.joueursAbandon:
#             game.joueursAbandon.append(game.currentPlayer)

# def task(board,game : Game):

#     joueurs = game.getPlayers()
#     plateau = game.getBoard()
#     for joueur in joueurs:
#         if joueur not in game.joueursAbandon:
#             game.currentPlayer = joueur
#             board.refreshPlayer(joueur.getColor())
#             print("c'est a : ",joueur.getName())
#             ajout = False
#             pieceid = 1
#             fini = False
#             while not fini:
#                 if joueur not in game.joueursAbandon:
#                     pieceid = input("Choisir pièce : ")
#                     piece = joueur.getPiece(pieceid)
#                     x = input("x = ")
#                     y = input("y = ")
#                     if joueur in game.joueursAbandon:
#                         fini = True
#                     if piece:
#                         if joueur in game.joueursAbandon:
#                             fini = True
#                         if joueur not in game.joueursAbandon:
#                             ajout = (plateau.ajouterPiece(piece,int(x),int(y),joueur,1,1))
#                         if ajout:
#                             fini = True
#                 else:
#                     fini = True
#             if joueur not in game.joueursAbandon:
#                 if ajout:
#                     joueur.ajoutTour()
#                     joueur.removePiece(str(pieceid))
#                 board.refreshBoard()
#     window.update()


# game = Game(None,None,20)

# window = tk.Tk()
# images = []

# images.append(ImageTk.PhotoImage(file="build/assets/frame0/empty_list.png"))
# images.append(PhotoImage(file="build/assets/frame0/player_yellow.png"))
# images.append(PhotoImage(file="build/assets/frame0/player_green.png"))
# images.append(PhotoImage(file="build/assets/frame0/player_blue.png"))
# images.append(PhotoImage(file="build/assets/frame0/player_red.png"))
# images.append(PhotoImage(file="build/assets/frame0/AppBorder.png"))
# images.append(PhotoImage(file="build/assets/frame0/board.png"))#270x270
# images.append(PhotoImage(file="build/assets/frame0/button_give_up.png"))

# window.geometry("1440x1024")

# border = tk.Canvas()
# border.config(bg="white")
# border.create_image(
#         0,
#         0,
#         image=images[5],
#         anchor=tk.NW
#     )


# border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
# board = GridInterface(border,game.getBoard(),images)
# board.move(x=720-270,y=512-270)

# List1 = PG.PiecesListGUI(border,images,"Joueur 1",1)
# List1.move(x=70,y=80)

# List2 = PG.PiecesListGUI(border,images,"Joueur 2",2)
# List2.move(x=1047,y=80)

# List3 = PG.PiecesListGUI(border,images,"Joueur 3",3)
# List3.move(x=1047,y=524)

# List4 = PG.PiecesListGUI(border,images,"Joueur 4",4)
# List4.move(x=70,y=524)

# aba = Abandon(images[-1],border,game)


# while 1:
#     task(board,game)


    def placePiece(self, piece : Pieces, colonne : int, ligne : int, dc : int, dl : int):
        '''Fonction de liaison entre le placement d'une piece graphique et moteur
        
        Args:
            - piece : Pieces -> pièce jouée
            - joueur : Player -> joueur de la pièce
            - colonne : int -> colonne du premier cube de la piece
            - ligne : int -> ligne du premier cube de la piece
            - dc : int -> décalage entre la colonne du premier cube de la piece et celle de l'origine de la piece.
            - dl : int -> décalage entre la ligne du premier cube de la piece et celle de l'origine de la piece.
        
        Returns: 
            - bool: vrai si la pièce est ajouter sur le plateau,sinon faux
        '''
        print("2",piece.getDelimitation())
        return self.game.playTurn(piece, colonne, ligne, dc, dl)

if __name__ == "__main__":
    global CT
    CT = Controller()