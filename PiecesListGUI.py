import tkinter as tk



class PiecesListGUI(tk.Frame):
    
    def __init__(self, parent : tk.Misc):
        tk.Frame.__init__(self, parent)
        
        
        List = tk.Frame(self)
        List.config(width=250,height=450 , bg="purple")
        List.pack()
        self.grid(row = 0, column = 0, pady = 2, padx=2)


if __name__=="__main__":


    window = tk.Tk()
    window.geometry("1440x1024")
    
    accueil=PiecesListGUI(window) 
    accueil.pack(expand=True)


    window.mainloop()