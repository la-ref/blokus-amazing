import tkinter as tk

class Block(tk.Frame):
    
    
    
    #   Créé l'élément de gui pour la liste des pieces
    #
    #
    def __init__(self, parent : tk.Canvas, image, nb_player : int, base_x : int, base_y : int, piece):
        super(Block,self).__init__(parent)
        self.parent = parent
        self.nb_player = nb_player
        ## emplacement initiale 
        self.base_x = base_x
        self.base_y = base_y

        self.piece = piece



        
        self.base_xoff = base_x
        self.base_yoff = base_y

        self.base_xoff2 = base_x
        self.base_yoff2 = base_y

        self.base_xoff3 = base_x
        self.base_yoff3 = base_y
        ## sert à garder la position relative avec la souris lors du déplacement
        self.delta_x = 100
        self.delta_y = 100
        # self.decalage_x = decal_x
        # self.decalage_y = decal_y
        ## sert à savoir si elle est en mvt
        self.state = 0
        
        
        self.bl = self.parent.create_image(
            base_x,
            base_y,
            image=image,
            anchor=tk.NW
        )
        # self.parent.moveto(self.base_x,self.base_y)
        
    def move(self, x : int, y : int):
        self.parent.move(self.bl,x,y)
    
    # def move_init(self, x : int, y : int):
    #     print("avant", self.base_x,self.base_y)
    #     self.base_x+=x
    #     self.base_y+=y
    #     self.parent.moveto(self.bl,self.base_x,self.base_y)
    #     print("move", self.base_x,self.base_y)
    
    def on_click(self,event):
        '''
        Fonction interne pour permettre le deplacement des blocks au clique
        '''
        ## si pas en mvt, enregistre la position relative avec la souris
        if not self.state:
            x,y=self.parent.coords(self.bl)
            self.delta_x,self.delta_y=event.x-x,event.y-y
        ## si en dehors de la grille, tp le block à la position initiale
        else:
            self.parent.moveto(self.bl,self.base_x,self.base_y)
            # self.parent.move(self.bl,self.delta_x,self.delta_y)
            print("test")         

        self.state = (self.state+1)%2
            
        
    def on_drag(self, event):
        '''
        Fonction interne pour permettre le deplacement des blocks au mvt de la souris
        '''
        x,y=self.parent.coords(self.bl)
        self.parent.move(self.bl,event.x-self.delta_x,event.y-self.delta_y)
        
    
    def bind(self,event_tag,call):
        '''
        Fonction interne pour permettre la gestion des event des blocks
        '''
        self.parent.tag_bind(self.bl,event_tag,call)
        
    def delete(self):
        '''
        Fonction interne pour détruire l'instance de block 
        '''
        self.parent.delete(self.bl)
        self.destroy()

if __name__=="__main__":
    from tkinter import PhotoImage

            
    window = tk.Tk()

    window.geometry("1440x1024")
    border = tk.Canvas()
    border.config(bg="white")
    border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
    
    images = []
    images.append(PhotoImage(file="build/assets/frame0/empty_list.png"))
    images.append(PhotoImage(file="build/assets/frame0/blue_1.png"))
    
    accueil=Block(border,images,1,0,0)
    import MouvementManager as Mv
    Mv.MouvementManager(accueil)


    window.mainloop()