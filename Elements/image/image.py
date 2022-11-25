from tkinter import PhotoImage


class image():
    def load():
        image = []
        image.append(PhotoImage(file="Accueil/assets/frame0/image_1.png")) #0
        image.append(PhotoImage(file="Accueil/assets/frame0/button_2.png")) #1
        image.append(PhotoImage(file="Accueil/assets/frame0/button_3.png")) #2
        image.append(PhotoImage(file="Accueil/assets/frame0/button_4.png")) #3
        image.append(PhotoImage(file="Accueil/assets/frame0/button_5.png")) #4
        image.append(PhotoImage(file="Accueil/assets/frame0/button_1.png")) #5
        image.append(PhotoImage(file="Plateau/assets/frame0/button_give_up.png")) #6
        image.append(PhotoImage(file="Plateau/assets/frame0/button_quit.png")) #7
        image.append(PhotoImage(file="Plateau/assets/frame0/game_board.png")) #8
        image.append(PhotoImage(file="Plateau/assets/frame0/empty_list.png")) #9
        image.append(PhotoImage(file="Plateau/assets/frame0/player_blue.png")) #10
        image.append(PhotoImage(file="Plateau/assets/frame0/player_green.png")) #11
        image.append(PhotoImage(file="Plateau/assets/frame0/player_red.png")) #12
        image.append(PhotoImage(file="Plateau/assets/frame0/player_yellow.png")) #13
        return image

    # def getImage(self, index: int):
    #     return image[index]