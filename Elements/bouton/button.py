import tkinter as tk
import pyglet as pg


class RoundedButton(tk.Canvas):
    """
    Cette classe initialise le boucle, c'est elle qui va l'affiche.
    """
    def __init__(self, master=None, text:str="", hauteur=20, largueur=20, fontsize=20, radius=25, btnforeground="#000000", btnbackground="#ffffff", clicked=None, *args, **kwargs):
        super(RoundedButton, self).__init__(master, *args, **kwargs)
        self.config(bg=self.master["bg"])
        self.btnbackground = btnbackground
        self.clicked = clicked
        self.largueur = largueur
        self.radius = radius
        self.hauteur = hauteur
        self.fontsize = fontsize
        
        self.rect = self.round_rectangle(0, 0, 0, 0, tags="button", radius=radius, fill=btnbackground)
        pg.font.add_file('Elements/bouton/police.ttf')
        set_font=pg.font.load('Lilita One')
 
        print(set_font)
        self.text = self.create_text(0, 0, text=text, tags="button", fill=btnforeground, font=("Lilita One", self.fontsize), justify="center")

        self.tag_bind("button", "<ButtonPress>", self.border)
        self.tag_bind("button", "<ButtonRelease>", self.border)
        self.bind("<Configure>", self.resize)
        
        text_rect = self.bbox(self.text)
        self["width"] = self.largueur
        
        self["height"] = self.hauteur
    
    """
    Cette fonction permet de créer un rectangle avec des bords arrondis
    params :
        - X1, coordonnée haut gauche
        - Y1, coordonnée bas gauche
        - X2, coordonnée haut droit
        - Y2, coordonnée bas droit
    """
    def round_rectangle(self, x1, y1, x2, y2, radius=25, update=False, **kwargs):
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        if not update:
            return self.create_polygon(points, **kwargs, smooth=True)
        else:
            self.coords(self.rect, points)

    def resize(self, event):
        text_bbox = self.bbox(self.text)

        if self.radius > event.width or self.radius > event.height:
            radius = min((event.width, event.height))

        else:
            radius = self.radius

        width, height = event.width, event.height

        if event.width < text_bbox[2]-text_bbox[0]:
            width = text_bbox[2]-text_bbox[0] + 30
        
        if event.height < text_bbox[3]-text_bbox[1]:  
            height = text_bbox[3]-text_bbox[1] + 30
        
        self.round_rectangle(5, 5, width-5, height-5, radius, update=True)

        bbox = self.bbox(self.rect)

        x = ((bbox[2]-bbox[0])/2) - ((text_bbox[2]-text_bbox[0])/2)
        y = ((bbox[3]-bbox[1])/2) - ((text_bbox[3]-text_bbox[1])/2)

        self.moveto(self.text, x, y)

    """
        Cette fonction permet de créer des bordures de couleur à notre bouton
        params : 
            - event : Si évènement de clique alors on ajoute l'évènement
    """
    def border(self, event):
        if event.type == "4":
            self.itemconfig(self.rect, fill="#d2d6d3")
            if self.clicked is not None:
                self.clicked()

        else:
            self.itemconfig(self.rect, fill=self.btnbackground)

def func():
    print("Bouton cliqué")


#---------------#
#    Exemple    #
#---------------#
# root = tk.Tk()
# btn = RoundedButton(text="Hors ligne", radius=100, hauteur=128, largueur=500, fontsize=32, btnbackground="#0078ff", btnforeground="#ffffff", clicked=func)
# btn.pack(expand=True, fill="both")
# root.mainloop()