import tkinter as tk
from accueil import Accueil
from lobbyLocal import lobbyLocal
from GameInterface import GameInterface
class Control(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = Accueil(container,self)
        self.frames = {}

        for f in (lobbyLocal,GameInterface):
            self.frames[f] = f(container,self)
    
    def show_frame(self,name):
        frame = self.frames[name]
        frame.tkraise()
