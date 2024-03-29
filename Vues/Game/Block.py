import tkinter as tk

class Block(tk.Frame):
    #   Créé l'élément de gui pour la liste des pieces
    #
    #
    def __init__(self, parent : tk.Canvas, image, nb_player : int, base_x : int, base_y : int, piece):
        """Constructeur créant un bloc de la pièce

        Args:
            self (Game): game
            window: La fenêtre de jeu
            parent (tk.Canvas): La fauille de dessin de la pièce
            image: Le tableau d'image
            nb_player (int): Identifiant du joueur
            base_x (int): Coordonnée en X du point d'origine de la pièce
            base_y (int): Coordonnée en Y du point d'origine de la pièce
        """
        super(Block,self).__init__(parent)
        self.parent = parent
        self.nb_player = nb_player
        ## emplacement initiale 
        self.base_x = base_x
        self.base_y = base_y

        self.piece = piece

        self.base_xoff = base_x
        self.base_yoff = base_y

        self.base_xoff3 = base_x
        self.base_yoff3 = base_y
        self.save_x,self.save_y = 0,0
        ## sert à garder la position relative avec la souris lors du déplacement
        self.delta_x = 100
        self.delta_y = 100

        ## sert à savoir si elle est en mvt
        self.state = 0
        self.bl = self.parent.create_image(
            base_x,
            base_y,
            image=image,
            anchor=tk.NW
        )

        
    def move(self, x : int, y : int):
        """ Méthode permettant le mouvement du bloc à une coordonnée X et Y 
        """
        self.parent.move(self.bl,x,y)

    def on_click(self,event):
        """
        Fonction interne pour permettre le deplacement des blocks au clique
        """
        ## si pas en mvt, enregistre la position relative avec la souris
        if not self.state:
            self.save_x,self.save_y = self.parent.coords(self.bl)
            x,y=self.parent.coords(self.bl)
            self.delta_x,self.delta_y=event.x-x,event.y-y
        ## si en dehors de la grille, tp le block à la position initiale
        else:
            self.parent.moveto(self.bl,self.base_x,self.base_y)  

        self.state = (self.state+1)%2
            
        
    def on_drag(self, event):
        """
        Fonction interne pour permettre le deplacement des blocks au mvt de la souris
        """
        x,y=self.parent.coords(self.bl)
        self.parent.move(self.bl,event.x-self.delta_x,event.y-self.delta_y)
        
    def recreate(self,x,y,image):
        self.bl = self.parent.create_image(
            x,
            y,
            image=image,
            anchor=tk.NW
        )
    def bind(self,event_tag,call):
        """
        Fonction interne pour permettre la gestion des event des blocks
        """
        self.parent.tag_bind(self.bl,event_tag,call)
        
    def delete(self):
        """
        Fonction interne pour détruire l'instance de block 
        """
        self.parent.delete(self.bl)
        self.destroy()