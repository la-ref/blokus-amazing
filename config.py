from tkinter import PhotoImage
import tkinter


class config():
    Config = None
    
    def __init__(self, controller):
        
        self.largueur : int = 1440
        self.hauteur : int = 1024
        self.image : list[PhotoImage] = []
        self.controller=controller
        
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
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_blue.png")) #10
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_green.png")) #11
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_red.png")) #12
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_yellow.png")) #13

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

