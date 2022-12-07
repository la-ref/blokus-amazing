import tkinter as tk
import time

class MouvementManager():

    # si drag vaut True, widget peut être déplacé.
    # si drop vaut True, widget peut recevoir des widgets déplaçable.
    # 
    def __init__(self,widget,drag : bool,drop : bool):

        self.widget = widget
        self.drag = drag
        self.drop = drop
        self.state = 0
        if drag:
            self.add_dragable()

    def add_dragable(self):
        self.widget.bind("<ButtonPress-1>", self.on_start)
        self.widget.bind("<Motion>", self.on_drag)
        self.widget.parent.bind("<Motion>", self.on_drag)
        self.widget.bind("<ButtonRelease-1>", self.on_drop)
        self.widget.configure(cursor="hand1")
        self.timer=time.perf_counter()

    def on_start(self, event):
        self.state = (self.state+1)%2
        self.widget.on_click(event)

    def on_drag(self, event):
        if self.state:
            if (time.perf_counter()-self.timer>0.02):
                self.widget.on_drag(event)
                self.timer=time.perf_counter()

    def on_drop(self, event):
        # commencons par trouver le widget sous le curseur de la souris
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        # self.widget.bind("<Motion>", None)
        try:
            pass
        except:
            pass
