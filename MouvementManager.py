import tkinter as tk

class MouvementManager():

    # si drag vaut True, widget peut être déplacé.
    # si drop vaut True, widget peut recevoir des widgets déplaçable.
    # 
    def __init__(self,widget,drag : bool,drop : bool):

        self.widget = widget
        self.drag = drag
        self.drop = drop
        if drag:
            self.add_dragable(self.widget)

    def add_dragable(self, widget):
        self.widget = widget
        self.widget.bind("<ButtonPress-1>", self.on_start)
        self.widget.bind("<B1-Motion>", self.on_drag)
        self.widget.bind("<ButtonRelease-1>", self.on_drop)
        self.widget.configure(cursor="hand1")

    def on_start(self, event):
        print("z")

    def on_drag(self, event):
        xd = event.x_root
        yd = event.y_root
        self.widget.move(x=xd,y=yd)

    def on_drop(self, event):
        # commencons par trouver le widget sous le curseur de la souris
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        try:
            pass
        except:
            pass
