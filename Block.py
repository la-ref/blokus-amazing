import tkinter as tk





class Block(tk.Frame):
    
    
    
    #   Créé l'élément de gui pour la liste des pieces
    #
    #
    def __init__(self, parent : tk.Canvas, images : list, nb_player : int, base_x : int, base_y : int):
        super(Block,self).__init__(parent)
        self.parent = parent
        self.nb_player = nb_player
        ## emplacement initiale 
        self.base_x = base_x
        self.base_y = base_y
        ## sert à garder la position relative avec la souris lors du déplacement
        self.delta_x = 100
        self.delta_y = 100
        ## sert à savoir si elle est en mvt
        self.state = 0
        
        
        self.bl = self.parent.create_image(
            0,
            0,
            image=images[nb_player],
            anchor=tk.NW
        )
        self.parent.moveto(self.base_x,self.base_y)
        
         
    def on_click(self,event):
        '''
        Fonction interne pour permettre le deplacement des blocks au clique
        '''
        ## si pas en mvt, enregistre la position relative avec la souris
        if not self.state:
            x,y=self.parent.coords(self.bl)
            self.delta_x,self.delta_y=event.x-x,event.y-y
        ## si en dehors de la grille, tp le block à la position initiale
        elif self.state and (event.x<450 or event.x>990 or event.y<242 or event.y>782):
            self.parent.moveto(self.bl,self.base_x,self.base_y)
        self.state = (self.state+1)%2
            
        
    def on_drag(self, event):
        '''
        Fonction interne pour permettre le deplacement des blocks au mvt de la souris
        '''
        x,y=self.parent.coords(self.bl)
        self.parent.moveto(self.bl,event.x-self.delta_x,event.y-self.delta_y)
        
    
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