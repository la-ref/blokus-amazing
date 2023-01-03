from tkinter import PhotoImage


class config():
    def __init__(self):
        self.largueur = 1440
        self.hauteur = 1024
        self.image = []
    def tableauImage():
        image = []
        # Accueil
        image.append(PhotoImage(file="Accueil/assets/frame0/image_1.png")) #0
        image.append(PhotoImage(file="Accueil/assets/frame0/button_2.png")) #1
        image.append(PhotoImage(file="Accueil/assets/frame0/button_3.png")) #2
        image.append(PhotoImage(file="Accueil/assets/frame0/button_4.png")) #3
        image.append(PhotoImage(file="Accueil/assets/frame0/button_5.png")) #4
        image.append(PhotoImage(file="Accueil/assets/frame0/button_1.png")) #5

        # Plateau
        image.append(PhotoImage(file="Plateau/assets/frame0/button_give_up.png")) #6
        image.append(PhotoImage(file="Plateau/assets/frame0/button_quit.png")) #7
        image.append(PhotoImage(file="Plateau/assets/frame0/game_board.png")) #8
        image.append(PhotoImage(file="Plateau/assets/frame0/empty_list.png")) #9
        image.append(PhotoImage(file="Plateau/assets/frame0/player_blue.png")) #10
        image.append(PhotoImage(file="Plateau/assets/frame0/player_green.png")) #11
        image.append(PhotoImage(file="Plateau/assets/frame0/player_red.png")) #12
        image.append(PhotoImage(file="Plateau/assets/frame0/player_yellow.png")) #13

        # Lobby local
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/arriere_plan.png")) #14
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_bleu.png")) #15
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_jaune.png")) #16
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_jouer.png")) #17
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_noir_ia.png")) #18
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_quitter.png")) #19
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_robot_gris.png")) #20
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_robot_noir.png")) #21
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_rouge.png")) #22
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_user_gris.png")) #23
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_user_noir.png")) #24
        image.append(PhotoImage(file="LobbyLocal/assets/frame0/bouton_vert.png")) #25
        return image
    def hauteurFenetre():
        return 1024
    def largueurFenetre():
        return 1440

    # def getImage(self, index: int):
    #     return image[index]