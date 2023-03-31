from __future__ import annotations
from Elements.Pieces.Pieces import Pieces
from Elements.Player import Player
from Elements.Board import Board
from config import config
import threading

class Game:

    """Classe de gestion des parties de jeu blokus
    """
    def __init__(self : Game, joueurs : list[Player]|None,plateau : Board|None,taille : int,online : bool = False) -> None:
        """Constructeur créant une partie avec des joueurs et un plateau de taille n

        Args:
            self (Game): game
            joueurs (list[Player] | None): liste de joueurs ou rien
            plateau (Board | None): plateau de jeu ou rien
            taille (int): taille du plateau de jeu
        """
        self.__joueurs : list[Player] = joueurs or [Player(11,"matthieu"),Player(12,"aurelian"),Player(13,"gauthier"),Player(14,"inconnu")]
        self.__joueursAbandon : list[Player] = []
        self.__currentPlayerPos : int = 0
        self.__plateau : Board = plateau or Board(taille)
        self.__online : bool = online
        self.__enCours = True

        for pj in self.__joueurs:
            pj.resetPiece()
    
    def enCours(self) -> bool:
        return self.__enCours
        
    def start(self):
        threading.Timer(0.5,self.__nextPlayer).start()

    def getPlayers(self : Game) -> list[Player]:
        """Méthode getter permettant d'avoir la liste contenant les joueurs dans le jeu

        Args:
            self (Game): game

        Returns:
            list[Player]: liste contenant les joueurs de la partie
        """
        return self.__joueurs
    
    def setPlayers(self : Game, list : list[Player]):
        self.__joueurs : list[Player] = list

    def getCurrentPlayer(self : Game) -> Player:
        """Méthode getter permettant d'avoir la liste contenant les joueurs dans le jeu

        Args:
            self (Game): game

        Returns:
            list[Player]: liste contenant les joueurs de la partie
        """
        return self.__joueurs[self.__currentPlayerPos]
    
    def getBoard(self : Game) -> Board:
        """Méthode getter permettant d'obtenir le plateau du jeu

        Args:
            self (Game): game

        Returns:
            Board: plateau du jeu
        """
        return self.__plateau

    def getCurrentPlayerId(self : Game) -> int:
        """Méthode getter permettant d'obtenir l'id du joueur courant

        Args:
            self (Game): Game

        Returns:
            int: l'id du joueur courant
        """
        return self.__currentPlayerPos
    
    def getCurrentPlayers(self : Game) -> list[Player]:
        """Méthode getter petmettant d'obtenir la liste des joueurs
        encore actuellement dans la partie.

        Args:
            self (Game): Game

        Returns:
            list: La liste des joueurs encore dans la partie
        """
        tableau = []
        for joueur in self.getPlayers():
            if joueur not in self.__joueursAbandon:
                tableau.append(joueur)
        return tableau

    def addSurrenderedPlayer(self : Game) -> bool|list[Player]:
        """Méthode qui permet d'ajouter un joueur dans la liste des joueurs qui ont abandonné et de donne le status de la partie
        voir : getWinners()

        Args:
            self (Game): Game

        Returns:
            bool|list[Player]: false si il la game n'est pas terminée sinon retourne la liste des joueurs gagnant
        """
        self.__joueursAbandon.append(self.__joueurs[self.__currentPlayerPos])
        self.__nextPlayer()
        if not self.__online:
            config.Config.controller.updateBoard() #actualise le plateau avec le joueur courant
        if self.getWinners():
            if not self.__online:
                config.Config.controller.vueJeu.changeTextPartie(" ",0)
                config.Config.controller.vueJeu.partieTermine
        return self.getWinners()
    
    def addSurrenderedPlayerOnline(self: Game, player) -> bool|list[Player]:
        if not self.__online:
            return False
        if player not in self.__joueursAbandon:
            if self.getCurrentPlayer() == player:
                self.addSurrenderedPlayer()
            else:
                self.__joueursAbandon.append(player)
        return self.getWinners()
            

    def isPlayerSurrendered(self : Game) -> bool:
        """Méthode permettant de savoir si le joueur courant a abandonné

        Args:
            self (Game): Game

        Returns:
            bool: vrai s'il a abandonné sinon faux
        """
        return self.__joueurs[self.__currentPlayerPos] in self.__joueursAbandon
    
    def getSurrenderedPlayer(self):
        return self.__joueursAbandon

    def __nextPlayer(self : Game) :
        """Méthode qui permet de sélectionné le prochain joueur pour être le joueur courant

        Args:
            self (Game): Game
        """
        self.__currentPlayerPos = (self.__currentPlayerPos+1)%len(self.__joueurs)
        while self.__joueurs[self.__currentPlayerPos] in self.__joueursAbandon and len(self.__joueursAbandon) != len(self.__joueurs):
            self.__currentPlayerPos = (self.__currentPlayerPos+1)%len(self.__joueurs)
        if not self.__online:
            config.Config.controller.updateBoard() #actualise le plateau avec le joueur courant
        
        if not self.__online:
            if len(self.__joueursAbandon) != len(self.__joueurs):
                config.Config.controller.vueJeu.changeTextPartie("C'est à " + self.__joueurs[self.__currentPlayerPos].getName() + " de jouer",self.__currentPlayerPos)
                if self.getCurrentPlayer().getAI():
                    self.getCurrentPlayer().getAI().play()
                return True
            else:
                return False

####################################################################################################################

    def isGameFinished(self : Game) -> bool:
        """Méthode getter qui indique si la partie est terminée ou non en regardant si tout les joueurs sont dans le tableau
        des joueurs qui ont abandonné

        Args:
            self (Game): Game

        Returns:
            bool: vrai si la partie est fini sinon faux
        """
        return len(self.__joueursAbandon) == len(self.__joueurs)    

    def countBlocks(self : Game,joueur : Player) -> int:
        """Méthode permettant d'obtenir le nombre de cubes posés sur la grille de jeu par un joueur

        Args:
            self (Game): Game
            joueur (Player): Joueur de la partie

        Returns:
            int: nombre de cubes posés par le joueur sur la grille de jeu
        """
        counter = 0
        for i in range(self.__plateau.getBoardSize()):
            for y in range(self.__plateau.getBoardSize()):
                if (joueur.getColor() == self.__plateau.getColorAt(i,y)):
                    counter+=1
        return counter

    def getWinners(self : Game) -> list[Player]:
        """Méthode permettant de savoir si la partie est fini ou non et d'obtenir les vainqueurs de la partie si fini

        Args:
            self (Game): _description_

        Returns:
            bool|list[Player]: false si il la game n'est pas terminée sinon retourne la liste des joueurs gagnant
        """
        if (len(self.__joueursAbandon) == len(self.__joueurs)):
            blockCount = []
            winners = []
            for joueur in self.__joueurs:
                blockCount.append(self.countBlocks(joueur))
            for i in range(len(blockCount)):
                if blockCount[i] == max(blockCount):
                    winners.append(self.__joueurs[i])
            return winners
        return []
    
    def getWinnersName(self : Game) -> list[str]:
        winners = self.getWinners()
        new = []
        if winners:
            for player in winners:
                new.append(player.getName())
            return new
        return False
                
    
    def playTurn(self : Game, piece : Pieces , colonne : int, ligne : int, dc : int, dl : int,rotation = None,flip = None) -> bool:
        """Méthode qui permet de jouer le tour du joueur courant
        
        Args:
            - piece : Pieces -> pièce jouée
            - joueur : Player -> joueur de la pièce
            - colonne : int -> colonne du premier cube de la piece
            - ligne : int -> ligne du premier cube de la piece
            - dc : int -> décalage entre la colonne du premier cube de la piece et celle de l'origine de la piece.
            - dl : int -> décalage entre la ligne du premier cube de la piece et celle de l'origine de la piece.
        
        Returns: 
            - bool: vrai si la pièce est ajouter sur le plateau,sinon faux
        """
        if len(self.__joueursAbandon) != len(self.__joueurs):
            if(rotation or flip):
                piece = piece.ajoutRotationFlip(rotation,flip)
            ajout= self.__plateau.ajouterPiece(piece,int(colonne),int(ligne),self.getCurrentPlayer(),int(dc),int(dl))
            if ajout: # si une pièce peut être ajouter
                self.getCurrentPlayer().removePiece(str(piece.getIdentifiant()))
                self.getCurrentPlayer().ajoutTour()


            
                if (len(self.getCurrentPlayer().getPieces()) == 0): # si un joueur a fini
                    self.addSurrenderedPlayer()
                else:
                    self.__nextPlayer()
                if not self.__online:
                    config.Config.controller.updateBoard()
                # prep tour suivant
                
                # config.Config.controller.updatePlayers(self.getCurrentPlayer())
                
                return True
            return False

        else:
            # call fonction winner
            return False
