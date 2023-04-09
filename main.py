import Controller.Controller as cc
import multiprocessing as mp
import os

if __name__ == "__main__":
    """
        Permet de lancer le jeu via le Controller
    """
    NB_CPU= mp.cpu_count()//2
    
    if NB_CPU==0:
        raise ValueError("The number of CPU's is too low for this game to work")


    global CT
    pool = mp.Pool(NB_CPU)
    CT = cc.Controller(pool, NB_CPU)

    os._exit(1)


