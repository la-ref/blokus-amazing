import tkinter as tk
import GridInterface as GI



class GameInterface(tk.Frame):
    
    def __init__(self, parent : tk.Misc):
        tk.Frame.__init__(self, parent)
        
        
    
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)
        
        List1 = tk.Frame(self)
        List1.config(width=250,height=450 , bg="yellow")
        List1.grid(row = 0, column = 0, pady = 2, padx=2)
        
        List2 = tk.Frame(self)
        List2.config(width=250,height=450 , bg="green")
        List2.grid(row = 0, column = 2, pady = 2, padx=2)
        
        List3 = tk.Frame(self)
        List3.config(width=250,height=450 , bg="blue")
        List3.grid(row = 1, column = 2, pady = 2, padx=2)
        
        List4 = tk.Frame(self)
        List4.config(width=250,height=450 , bg="red")
        List4.grid(row = 1, column = 0, pady = 2, padx=2)
        
        board = GI.GridInterface(self)
        board.grid(row = 0, rowspan=2 , column = 1, pady = 10, padx=50)


if __name__=="__main__":

    window = tk.Tk()
    window.geometry("1440x1024")
    
    accueil=GameInterface(window)
    accueil.pack(expand=True)


    window.mainloop()