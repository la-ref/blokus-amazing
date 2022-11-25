from tkinter import PhotoImage


class button():
    def load(self):
        self.image = []
        self.image.append(PhotoImage(file="Accueil/assets/frame0/image_1.png")) #0
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_2.png")) #1
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_3.png")) #2
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_4.png")) #3
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_5.png")) #4
        self.image.append(PhotoImage(file="Accueil/assets/frame0/button_1.png")) #5
        self.image.append(PhotoImage(file="Plateau/assets/frame0/button_give_up.png")) #6
        self.image.append(PhotoImage(file="Plateau/assets/frame0/button_quit.png")) #7
        self.image.append(PhotoImage(file="Plateau/assets/frame0/game_board.png")) #8
        self.image.append(PhotoImage(file="Plateau/assets/frame0/empty_list.png")) #9
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_blue.png")) #10
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_green.png")) #11
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_red.png")) #12
        self.image.append(PhotoImage(file="Plateau/assets/frame0/player_yellow.png")) #13

    def getImage(self, index: int):
        return self.image[index]