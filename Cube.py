import tkinter as tk





class Block(tk.Frame):
    
    
    
    #   Creer l'élément de gui pour la liste des pieces
    #
    #
    def __init__(self, parent : tk.Canvas, images : list, nb_player : int):
        super(Block,self).__init__(parent)
        self.parent = parent
        self.bl = self.parent.create_image(
            0,
            0,
            image=images[nb_player],
            anchor=tk.NW
        )
        
        
    # Fonction utiliser par Mouvement Manager (à supprimer plus tard)
    def move(self, x : int, y : int):
        self.parent.move(self.bl,x,y)
        
        
    def on_click(self,event):
        x,y=self.parent.coords(self.bl)
        self.delta=event.x-x,event.y-y
        
    def on_drag(self, event):
        x,y=self.parent.coords(self.bl)
        self.move(event.x-x-self.delta[0],event.y-y-self.delta[1])
        
    def bind(self,event_tag,call):
        self.parent.tag_bind(self.bl,event_tag,call)
        
    

if __name__=="__main__":
    from tkinter import PhotoImage

    
    # def on_configure(e):
    #     if e.widget == tk_root:
    #         sleep(0.015)
            
    window = tk.Tk()
    # window.bind("<Configure>", on_configure)
    window.geometry("1440x1024")
    border = tk.Canvas()
    border.config(bg="white")
    border.place(x=0,y=0,height=1024,width=1440,anchor=tk.NW)
    
    images = []
    images.append(PhotoImage(file="build/assets/frame0/empty_list.png"))
    images.append(PhotoImage(file="build/assets/frame0/blue_1.png"))
    
    accueil=Block(border,images,1)
    import MouvementManager as Mv
    Mv.MouvementManager(accueil,True,True)


    window.mainloop()