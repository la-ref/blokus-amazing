import tkinter as tk
from PIL import ImageTk,Image
import Elements.Pieces.PiecesDeclaration as PD
from tkinter import PhotoImage
import Elements.Pieces.Pieces as p
import numpy as np
import Vues.Game.Block as b
from config import config
class Pieces_placement(tk.Frame):

    """Classe de gestion de la pièce
    """
    def __init__(self, window, parent : tk.Canvas, nb_player : int, la_piece: str):
        """Constructeur créant une pièce du joueur
        Args:
            self (Game): game
            window: La fenêtre de jeu
            parent (tk.Canvas): La fauille de dessin de la pièce
            nb_player (int): Identifiant du joueur
            la_piece (str) : Identifiant de la pièce
        """
        super(Pieces_placement,self).__init__(parent)


        # Variable global de la pièce
        self.window = window
        self.window.bind("<Motion>", self.on_drag, add='+')
        self.window.bind("<MouseWheel>", self.on_rotate, add='+')
        self.parent = parent
        self.nb_player = nb_player-11
        self.imagepiece = { 0:(PhotoImage(file="Images/Plateau/yellow.png")),
                            1:(PhotoImage(file="Images/Plateau/green.png")),
                            2:(PhotoImage(file="Images/Plateau/red.png")),
                            3:(PhotoImage(file="Images/Plateau/blue.png"))}
        self.x = 0
        self.y = 0
        self.la_piece = la_piece
        self.le_x = 0
        self.le_y = 0
        self.rotate = False
        self.souris_x = 0
        self.sourix_y = 0
        self.state = 0
        self.tableau_piece = [[]]
        self.tableau_piece_forme = []
        self.mon_state = 0

        # Initialisation de la pièce
        self.piece=PD.LISTEPIECES[la_piece]

        # Tableau des délimitations de la pièce
        self.tableau_piece=self.piece.getDelimitation()

        # Définition de l'image d'un bloc de la pièce
        self.image = self.imagepiece[self.nb_player]
        self.image = self.image.subsample(2)
        
        # Création de la pièce
        for i in range(len(self.tableau_piece[0])):
            self.y+=self.image.height()
            self.x=0
            for v in range(len(self.tableau_piece)):
                self.x+=self.image.width()
                if (self.tableau_piece[v][i] == 3):
                    test = b.Block(self.parent,self.image,self.nb_player,self.x,self.y,self)
                    self.parent.tag_bind(test.bl, "<ButtonPress-1>", self.on_click)
                    self.parent.tag_bind(test.bl, "<ButtonPress-3>", self.on_flip)
                    self.tableau_piece_forme.append(test)
                    
    def getPieceBoardCoord(self):
        """Fonction pour obtenir les coords du coin gauche de la piece sur le tableau 
        
        Returns:
            - int : colonne du premier cube de la piece
            - int : ligne du premier cube de la piece
            - int : décalage entre la colonne du premier cube de la piece et celle de l'origine de la piece.
            - int : décalage entre la ligne du premier cube de la piece et celle de l'origine de la piece.
        """
        x,y=self.parent.coords(self.tableau_piece_forme[0].bl)
        dy,dx=np.argwhere(self.tableau_piece==3)[0]
        x,y=x-27*(dx-1),y-27*(dy-1) # calcul les coordonnées du coin haut gauche
        return (x-450)//27+dx-1,(y-242)//27+dy-1,dx,dy

    def getPieceCoord(self):
        """
        Fonction pour obtenir les coords du coin gauche de la piece sur l'écran 
        """
        x,y=self.parent.coords(self.tableau_piece_forme[0].bl)
        dy,dx=np.argwhere(self.tableau_piece==3)[0]
        x,y=x-27*(dx-1),y-27*(dy-1) # calcul les coordonnées du coin haut gauche
        return [x,y]

    def on_flip(self,event):
        """Méthode qui permet de retourner la pièce (effet miroir)
        Args:
            event : évènement
        """
        # Si la pièce est sélectionnée
        if self.mon_state == True:
            self.x,self.y=self.getPieceCoord()
            self.ancienx,self.ancieny=self.getPieceCoord()

            # Suppression de la pièce
            for piece in self.tableau_piece_forme:
                objet = self.parent.find_withtag(piece.bl)
                ma_piece = objet[0]
                self.parent.delete(ma_piece)
            
            self.piece = PD.LISTEPIECES[self.la_piece]
            self.piece.flip()

            # Re-création de la pièce
            self.changement_piece(self.piece)

    def on_rotate(self,event):
        """Méthode qui permet de tourner à 90 degré la pièce
        Args:
            event : évènement
        """
        # Si la pièce est sélectionnée
        if self.mon_state == True:
            self.x,self.y=self.getPieceCoord()
            self.ancienx,self.ancieny=self.getPieceCoord()

            # Suppression de la pièce
            for piece in self.tableau_piece_forme:
                objet = self.parent.find_withtag(piece.bl)
                ma_piece = objet[0]
                self.parent.delete(ma_piece)

            self.piece = PD.LISTEPIECES[self.la_piece]
            self.piece.rotate90()

            # Re-création de la pièce
            self.changement_piece(self.piece)
    
    def changement_piece(self,piece):
        """Méthode qui permet de créer la pièce une fois quelle est supprimée
        Args:
            piece : la pièce
        """
        self.rotate = True

        self.tableau_piece = [[]]
        self.tableau_piece=piece.getDelimitation()
        
        self.tableau_piece_forme = []

        self.back_x = self.x
        self.back_y = self.y

        self.x=0
        self.y=0

        # Création de la pièce
        for i in range(len(self.tableau_piece)):
            self.x+=self.image.height()
            self.y = 0
            for v in range(len(self.tableau_piece[0])):
                self.y+=self.image.width()
                if (self.tableau_piece[i][v] == 3):
                    le_block = b.Block(self.parent,self.image,self.nb_player,0+self.y,0+self.x,self)
                    self.parent.tag_bind(le_block.bl, "<ButtonPress-1>", self.on_click)
                    self.parent.tag_bind(le_block.bl, "<ButtonPress-3>", self.on_flip)
                    self.tableau_piece_forme.append(le_block)
                    le_block.move(self.back_x-self.x,self.back_y-self.y)
                    le_block.state = 1
        
        # Téléportation de la pièce à l'endroit d'initialisation
        for piece in self.tableau_piece_forme:
            x2,y2=self.parent.coords(piece.bl)
            piece.move(piece.base_xoff,piece.base_yoff)
        
        # Sélection des coordonnées du premier bloc
        piece = self.tableau_piece_forme[0]
        self.oy2,self.ox2=self.parent.coords(piece.bl)
        differenceX = self.le_x+piece.base_xoff
        differenceY = self.le_y+piece.base_yoff
        self.le_x = self.le_x-differenceX
        self.le_y = self.le_y-differenceY

        # Téléportation de la pièce à la souris en fonction des coordonnées du premier bloc
        for piece in self.tableau_piece_forme:
            x2,y2=self.parent.coords(piece.bl)
            piece.move(self.souris_x-x2+piece.base_xoff+self.le_x,self.sourix_y-y2+piece.base_yoff+self.le_y)

    def getImage(self):
        """Fonction qui permet de savoir l'image 
        Returns:
            self.image: L'image
        """
        return self.image
    
    def getWidth(self):
        """Fonction qui permet de savoir la taille de la pièce
        Returns:
            len(self.tableau_piece): La largueur de la pièce
        """
        return len(self.tableau_piece)

    def getHeight(self):
        """Fonction qui permet de savoir la taille de la pièce
        Returns:
            len(self.tableau_piece[0]): La hauteur de la pièce
        """
        return len(self.tableau_piece[0])
    
    def getWidth_Petit(self):
        """Fonction qui permet de savoir la taille de la pièce moins la bordure
        Returns:
            len(self.tableau_piece)-2: La pièce moins la bordure
        """
        return len(self.tableau_piece)-2

    def getHeight_Petit(self):
        """Fonction qui permet de savoir la taille de la pièce moins la bordure
        Returns:
            len(self.tableau_piece[0])-2: La pièce moins la bordure
        """
        return len(self.tableau_piece[0])-2

    def move(self, x : int, y : int):
        """Méthode qui permet de modifier l'emplacement de chaque bloc
        Args:
            x : coordonnées en X
            y : coordonnées en Y
        """
        self.le_x+=x
        self.le_y+=y
        for piece in self.tableau_piece_forme:
            x2,y2=self.parent.coords(piece.bl)
            piece.move(x-x2-piece.base_x,y-y2-piece.base_y)
    
    def move_init(self, x : int, y : int):
        """Méthode qui permet la téléportation de la pièce à l'endroit d'initialisation
        Args:
            x : coordonnées en X
            y : coordonnées en Y
        """
        self.le_x+=x
        self.le_y+=y
        for piece in self.tableau_piece_forme:
            piece.move(x,y)
            piece.base_x += x
            piece.base_y += y
            piece.base_xoff2 = piece.base_x
            piece.base_yoff2 = piece.base_y
    
    def move_init2(self, x : int, y : int):
        """Méthode qui permet la téléportation de la pièce dans la liste du joueur
        Args:
            x : coordonnées en X
            y : coordonnées en Y
        """
        self.le_x+=x
        self.le_y+=y
        for piece in self.tableau_piece_forme:
            piece.move(x,y)
            piece.base_x += x
            piece.base_y += y
            self.base_xoff3 = self.le_x
            self.base_yoff3 = self.le_y


    def on_click(self,event):
        """ Fonction interne pour permettre le deplacement des blocks au clique
        Condition "si le bloc touche le plateau"
            Regare si le placement est bon
                Va supprimer la pièce et la mettre sur le plateau
            Si le placement n'est pas bon
                Va téléporter la pièce à l'endroit d'initialisation
        Deuxième condition "si le bloc ne touche pas le plateau"
            Va téléporter la pièce à l'endroit d'initialisation
        Args:
            event : l'évènement
        """

        ## reset la piece
        if (event.x<450 or event.x>990 or event.y<242 or event.y>782):
            self.image = self.imagepiece[self.nb_player]
            self.ok = 0
            for block in self.tableau_piece_forme:
                block.on_click(event)
                self.parent.itemconfigure(block.bl, image=self.image)

        
        self.le_x = self.base_xoff3
        self.le_y = self.base_yoff3

        # Condition si la pièce est sur le plateau
        if (event.x<450 or event.x>990 or event.y<242 or event.y>782):
            self.image = self.imagepiece[self.nb_player]

            # Changement de la taille de l'image
            for block in self.tableau_piece_forme:
                block.on_click(event)
                self.parent.itemconfigure(block.bl, image=self.image)
            
            # Si a pièce n'est pas motion (sélectionné et téléporté à la souris)
            if not self.mon_state:
                self.image = self.imagepiece[self.nb_player]
                self.saveliste = self.tableau_piece_forme

                # Change les coordonnés de téléportation au premier bloc de la pièce
                piece = self.tableau_piece_forme[0]
                self.oy2,self.ox2=self.parent.coords(piece.bl)
                differenceX = self.le_x+piece.base_xoff
                differenceY = self.le_y+piece.base_yoff
                self.le_x = self.le_x-differenceX
                self.le_y = self.le_y-differenceY
                    
                # Supprime tous les blocs
                for piece in self.tableau_piece_forme:
                    objet = self.parent.find_withtag(piece.bl)
                    ma_piece = objet[0]
                    self.parent.delete(ma_piece)
                
                self.tableau_piece_forme = []

                #Permet de recréer la pièce
                self.changement_piece(self.piece)
            else:
                # Supprime tous les blocs
                for piece in self.tableau_piece_forme:
                    objet = self.parent.find_withtag(piece.bl)
                    ma_piece = objet[0]
                    self.parent.delete(ma_piece)
                
                # Met le tableau sur la sauvegarde du tableau d'initialisation
                self.tableau_piece_forme = self.saveliste

                # Changement de la taille de l'image à une taille pour la liste
                self.image = self.imagepiece[self.nb_player]
                self.image = self.image.subsample(2)

                # Re-création de la pièce à l'endroit d'initialisation
                for block in self.tableau_piece_forme:
                    block.recreate(block.save_x,block.save_y,self.image)
                    self.parent.tag_bind(block.bl, "<ButtonPress-1>", self.on_click)
                    self.parent.tag_bind(block.bl, "<ButtonPress-3>", self.on_flip)
                    block.state = 0
        
        else:
            ## teste si peut placer
            col,lig,dc,dl = self.getPieceBoardCoord()
            if config.Config.controller.placePiece(self.piece,self.nb_player,col,lig,dc,dl):
                # supprime si oui
                for piece in self.tableau_piece_forme:
                    piece.delete()
                self.tableau_piece_forme = []
            else:
                # remet la piece à la position si non
                for piece in self.tableau_piece_forme:
                    objet = self.parent.find_withtag(piece.bl)
                    ma_piece = objet[0]
                    self.parent.delete(ma_piece)
                
                # Met le tableau sur la sauvegarde du tableau d'initialisation
                self.tableau_piece_forme = self.saveliste

                # Changement de la taille de l'image à une taille pour la liste
                self.image = self.imagepiece[self.nb_player]
                self.image = self.image.subsample(2)

                # Re-création de la pièce à l'endroit d'initialisation
                for block in self.tableau_piece_forme:
                    block.recreate(block.save_x,block.save_y,self.image)
                    self.parent.tag_bind(block.bl, "<ButtonPress-1>", self.on_click)
                    self.parent.tag_bind(block.bl, "<ButtonPress-2>", self.on_flip)
                    block.state = 0

        
        # Changement de l'état 0 ou 1
        self.mon_state=(self.mon_state+1)%2


    def on_drag(self, event):
        """
        Fonction interne pour permettre le deplacement des blocks au mvt de la souris
        Args:
            event : l'évènement
        """
        self.souris_x = event.x
        self.sourix_y = event.y
        self.premier2 = 0

        # Téléportation de la pièce à l'endroit de la souris
        if self.mon_state == True:
            for piece in self.tableau_piece_forme:
                x2,y2=self.parent.coords(piece.bl)
                piece.move(event.x-x2+piece.base_xoff+self.le_x,event.y-y2+piece.base_yoff+self.le_y) 
        self.premier2 = 0
        

if __name__=="__main__":
    from tkinter import PhotoImage
    window = tk.Tk()
    window.geometry("1440x1024")
    
    border = tk.Canvas()
    border.config(bg="white")
    border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
    
    images = []
    images.append(Image.open("build/assets/frame0/empty_list.png"))
    images.append(Image.open("build/assets/frame0/player_blue.png"))
    Photo_images = []
    Photo_images.append(ImageTk.PhotoImage(images[0]))
    Photo_images.append(ImageTk.PhotoImage(images[1].rotate(angle=00, expand=True)))
    
    accueil=Pieces_placement(window,border,11,"21")
    accueil.move(300,300)  
    window.mainloop()