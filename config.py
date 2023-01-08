from __future__ import annotations
from tkinter import PhotoImage
import tkinter
# from Controller import Controller


class config():
    Config : config
    
    def __init__(self, controller):
        
        self.largueur : int = 1440
        self.hauteur : int = 1024
        self.image : list[PhotoImage] = []
        self.imagepiece : dict = {}
        self.controller=controller
        
        import platform
        if platform.system() == "Darwin":
            self.taillePolice=[40,32,30]
        elif platform.system() == "Windows" or platform.system() == "Linux":
            self.taillePolice=[30,25,22]


        
        self.image.append(PhotoImage(file="Accueil/assets/frame0/image_1.png")) #0
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_2.png")) #1
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_3.png")) #2
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_4.png")) #3
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_5.png")) #4
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_1.png")) #5

        # Plateau
        self.image.append(PhotoImage(file="Plateau/assets/frame0/button_give_up.png")) #6
        self.image.append(PhotoImage(file="Plateau/assets/frame0/button_quit.png")) #7
        self.image.append(PhotoImage(file="Plateau/assets/frame0/game_board.png")) #8
        self.image.append(PhotoImage(file="Plateau/assets/frame0/empty_list.png")) #9
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_yellow.png")) #10
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_green.png")) #11
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_red.png")) #12
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_blue.png")) #13

        # Lobby local
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/arriere_plan.png")) #14
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_bleu.png")) #15
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_jaune.png")) #16
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_jouer.png")) #17
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_noir_ia.png")) #18
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_quitter.png")) #19
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_robot_gris.png")) #20
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_robot_noir.png")) #21
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_rouge.png")) #22
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_user_gris.png")) #23
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_user_noir.png")) #24
        self.image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_vert.png")) #25

        #Plateau 
        self.image.append(PhotoImage(file="build/assets/frame0/AppBorder.png")) # 26
        self.image.append(PhotoImage(file="build/assets/frame0/surrenderhover.png")) # 27
        self.image.append(PhotoImage(file="build/assets/frame0/quitterhover.png")) # 28

        #Hover accueil
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_1_hover.png")) #29
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_2_hover.png")) #30
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_3_hover.png")) #31
        
        #Plateau
        self.image.append(PhotoImage(file="build/assets/frame0/player_surrender.png")) # 32

        #Hover accueil
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_4_hover.png")) #33
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_5_hover.png")) #34
    
        #Piece
        self.imagepiece = { 11:(PhotoImage(file="build/assets/piece/yellow.png")),
                    12:(PhotoImage(file="build/assets/piece/green.png")),
                    13:(PhotoImage(file="build/assets/piece/red.png")),
                    14:(PhotoImage(file="build/assets/piece/blue.png"))} 
        
        

        
    @staticmethod
    def initialisation(controller):
        '''
        Initialisation de la configuration. L'accès à la configuration ce fait via config.Config 
        '''
        config.Config = config(controller)
    

    def tableauImage(self):
        return self.image
    
    def hauteurFenetre(self):
        return self.hauteur
    
    def largueurFenetre(self):
        return self.largueur
    

    def __repr__(self) -> str:
        if not self.Config:
            return "Configuration pas initialisée !!!"
        else:
            return "\n| Configuration:\n| - Hauteur : {}\n| - Largeur : {}\n".format(self.hauteur,self.largueur)

