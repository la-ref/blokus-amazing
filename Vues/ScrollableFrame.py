import tkinter as tk
from tkinter import ttk
from config import config


class ScrollableFrame(ttk.Frame):
    """ Classe permettant de créer une frame scrollable
    """
    def __init__(self, container,image = None):
        """ Méthode d'initialisation de la classe, elle permet de créer notre objet
        
        Args:
            container: le canvas où sera affiché notre objet
        """
        super().__init__(container)
        self.canvas = tk.Canvas(self,width=config.Config.image[53].width(),height=854)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        if image:
            img = self.canvas.create_image(
                0, 
                0, 
                image=image,
                anchor=tk.NW
            )

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        


    def destroye(self) -> None:
        """ Méthode qui permet de supprimer l'ensemble des éléments de la frame

        Args:
            self: l'ensemble de notre objet
        """
        self.scrollable_frame.destroy()
        self.scrollbar.destroy()
        self.canvas.destroy()
        self.destroy()