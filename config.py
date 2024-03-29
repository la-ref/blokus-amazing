from __future__ import annotations
from tkinter import PhotoImage
import random

class config():
    """ Classe de configuration de l'application
    """
    Config : config
    
    def __init__(self, controller, NB_CPU):
        """ Constructeur qui permet d'initialiser les émléments principaux du jeu

        Args:
            Controller: Controller qui gère le jeu
        """
        random.seed()
        self.NB_CPU= NB_CPU
        self.largueur : int = 1440
        self.hauteur : int = 1024
        self.image : list[PhotoImage] = []
        self.imagepiece : dict = {}
        self.controller = controller
        
        import platform
        if platform.system() == "Darwin":
            self.taillePolice=[40,32,30,22]
            self.jsonPath = "/HighScore/highscore.json"
        elif platform.system() == "Windows":
            self.taillePolice=[30,25,22,15]
            self.jsonPath = "\\HighScore\\highscore.json"
        elif platform.system() == "Linux":
            self.taillePolice=[30,25,22,15]
            self.jsonPath = "/HighScore/highscore.json"


        # vérifie si la police est installée
        import tkinter as tk, tkinter.font as tk_font
        if 'Lilita One' not in tk_font.families():
            # sinon
            if platform.system() == "Windows":
                # si sous windows, auto installation
                print("Font installation : start")
                print("Font installation : 0%")
                import win32api
                import win32con
                import ctypes
                print("Font installation : 35%") # =)
                gdi32 = ctypes.WinDLL('gdi32'); 
                result = gdi32.AddFontResourceW(u"./Elements/bouton/police.ttf")
                win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_FONTCHANGE)
                print("Font installation : 100%")
                print("Font installation : complete")
            
            else:
                # si autre, previens et quitte
                print("Police non installée ! Veillez l'installer (voir manuel utilisateur)")
                exit(-5)
        
        self.image.append(PhotoImage(file="Images/Accueil/image_1.png")) #0
        self.image.append(PhotoImage(file="Images/Accueil/button_2.png")) #1
        self.image.append(PhotoImage(file="Images/Accueil/button_3.png")) #2
        self.image.append(PhotoImage(file="Images/Accueil/button_4.png")) #3
        self.image.append(PhotoImage(file="Images/Accueil/button_5.png")) #4
        self.image.append(PhotoImage(file="Images/Accueil/button_1.png")) #5

        # Plateau
        self.image.append(PhotoImage(file="Images/Plateau/button_give_up.png")) #6
        self.image.append(PhotoImage(file="Images/Plateau/button_quit.png")) #7
        self.image.append(PhotoImage(file="Images/Plateau/board.png")) #8
        self.image.append(PhotoImage(file="Images/Plateau/empty_list.png")) #9
        self.image.append(PhotoImage(file="Images/Plateau/player_yellow.png")) #10
        self.image.append(PhotoImage(file="Images/Plateau/player_green.png")) #11
        self.image.append(PhotoImage(file="Images/Plateau/player_blue.png")) #12
        self.image.append(PhotoImage(file="Images/Plateau/player_red.png")) #13

        # Lobby local
        self.image.append(PhotoImage(file="Images/LobbyLocal/arriere_plan.png")) #14
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_bleu.png")) #15
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_jaune.png")) #16
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_jouer.png")) #17
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_noir_ia.png")) #18
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_quitter.png")) #19
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_robot_gris.png")) #20
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_robot_noir.png")) #21
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_rouge.png")) #22
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_user_gris.png")) #23
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_user_noir.png")) #24
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_vert.png")) #25

        #Plateau 
        self.image.append(PhotoImage(file="Images/Plateau/AppBorder.png")) # 26
        self.image.append(PhotoImage(file="Images/Plateau/surrenderhover.png")) # 27
        self.image.append(PhotoImage(file="Images/Plateau/quitterhover.png")) # 28

        #Hover accueil
        self.image.append(PhotoImage(file="Images/Accueil/button_1_hover.png")) #29
        self.image.append(PhotoImage(file="Images/Accueil/button_2_hover.png")) #30
        self.image.append(PhotoImage(file="Images/Accueil/button_3_hover.png")) #31
        
        #Plateau
        self.image.append(PhotoImage(file="Images/Plateau/player_surrender.png")) # 32

        #Hover accueil
        self.image.append(PhotoImage(file="Images/Accueil/button_4_hover.png")) #33
        self.image.append(PhotoImage(file="Images/Accueil/button_5_hover.png")) #34

        #Hover lobby
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_jaune_hover.png")) #35
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_vert_hover.png")) #36
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_rouge_hover.png")) #37
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_bleu_hover.png")) #38
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_jouer_hover.png")) #39
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_quitter_hover.png")) #40
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_noir_ia_hover.png")) #41
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_robot_gris_hover.png")) #42
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_robot_noir_hover.png")) #43
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_user_gris_hover.png")) #44
        self.image.append(PhotoImage(file="Images/LobbyLocal/bouton_user_noir_hover.png")) #45

        #Lobby winner
        self.image.append(PhotoImage(file="Images/Plateau/image_winner.png")) #46
        
        #Icone
        self.image.append(PhotoImage(file="Images/logo.png")) #47
    
        #Piece
        self.image.append(PhotoImage(file="Images/Plateau/yellow.png")) #48
        self.image.append(PhotoImage(file="Images/Plateau/green.png")) #49
        self.image.append(PhotoImage(file="Images/Plateau/blue.png")) # 50
        self.image.append(PhotoImage(file="Images/Plateau/red.png")) # 51


        #Accueil
        self.image.append(PhotoImage(file="Images/Accueil/regle_fond.png")) # 52
        self.image.append(PhotoImage(file="Images/Accueil/regle_text.png")) # 53
        self.image.append(PhotoImage(file="Images/Accueil/voile.png")) # 54

        #Plateau hover
        self.image.append(PhotoImage(file="Images/LobbyLocal/info_hover.png")) # 55

        # Modal
        self.image.append(PhotoImage(file="Images/modal/no_valid.png")) # 56
        self.image.append(PhotoImage(file="Images/modal/valid.png")) # 57

        # Game hover
        self.image.append(PhotoImage(file="Images/Plateau/button_info_hover.png")) # 58
        self.image.append(PhotoImage(file="Images/Plateau/button_info.png")) # 59

        # Connexion
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/adresse_ip.png")) # 60
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/entrer_pseudo.png")) # 61
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/port.png")) # 62
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/se_connecter.png")) # 63
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/param_avance.png")) # 64
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/param_simplifie.png")) # 65
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/adresse_ip_hover.png")) # 66
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/entrer_pseudo_hover.png")) # 67
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/port_hover.png")) # 68
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/se_connecter_hover.png")) # 69
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/param_avance_hover.png")) # 70
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/param_simplifie_hover.png")) # 71
        self.image.append(PhotoImage(file="Images/LobbyEnLigne/quitter_hover.png")) # 72
        
        # Accueil erreur
        self.image.append(PhotoImage(file="Images/Accueil/error.png")) # 73

        # Scoreboard
        self.image.append(PhotoImage(file="Images/Leaderboard/button.png")) # 74
        self.image.append(PhotoImage(file="Images/Leaderboard/fleche_droite.png")) #75
        self.image.append(PhotoImage(file="Images/Leaderboard/fleche_gauche.png")) # 76
        self.image.append(PhotoImage(file="Images/Leaderboard/button_blanc.png")) # 77

        self.image.append(PhotoImage(file="Images/Leaderboard/fleche_droite_hover.png")) # 78
        self.image.append(PhotoImage(file="Images/Leaderboard/fleche_gauche_hover.png")) # 79
        


        
    @staticmethod
    def initialisation(controller, NB_CPU):
        """
        Initialisation de la configuration. L'accès à la configuration ce fait via config.Config 
        """
        config.Config = config(controller, NB_CPU)
    

    def tableauImage(self):
        """ Fonction qui permet de retourner le dictionnaire image

        Return:
            self.image: Tableau d'images
        """
        return self.image
    
    def hauteurFenetre(self):
        """ Fonction qui permet de retourner la hauteur de la fenêtre

        Return:
            self.hauteur (int): Valeur de la hauteur de la fenêtre
        """
        return self.hauteur
    
    def largueurFenetre(self):
        """ Fonction qui permet de retourner la largueur de la fenêtre

        Return:
            self.largueur (int): Valeur de la largueur de la fenêtre
        """
        return self.largueur
    

    def __repr__(self) -> str:
        if not self.Config:
            return "Configuration pas initialisée !!!"
        else:
            return "\n| Configuration:\n| - Hauteur : {}\n| - Largeur : {}\n".format(self.hauteur,self.largueur)

