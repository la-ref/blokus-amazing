import Controller.Controller as cc
import multiprocessing as mp

if __name__ == "__main__":
    """
        Permet de lancer le jeu via le Controller
    """
    print(mp.cpu_count())
    mp.set_start_method('spawn')
    global CT
    CT = cc.Controller()
    
