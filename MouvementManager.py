import tkinter as tk
import time

class MouvementManager():
    ## Permet le click and drop du widget passé en paramètre

    def __init__(self,widget):
        self.widget = widget
        self.widget.bind("<ButtonPress-1>", self.on_click)
        self.widget.bind("<Motion>", self.on_drag)
        self.widget.parent.bind("<Motion>", self.on_drag)
        self.widget.configure(cursor="hand1")
        self.timer=time.perf_counter()


    def on_click(self, event):
        self.widget.on_click(event)
        

    def on_drag(self, event):
        if self.widget.state:
            ## limite le frame rate pour empêcher des bizareries
            if (time.perf_counter()-self.timer>0.02):
                self.widget.on_drag(event)
                self.timer=time.perf_counter()
