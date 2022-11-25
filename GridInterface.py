import tkinter as tk


class GridInterface(tk.Frame):
    
    def __init__(self, parent : tk.Misc, hThick : int = 2):
        tk.Frame.__init__(self, parent, highlightthickness=hThick)
        for i in range(10):
            for j in range(10):
                widget = tk.Frame(self,highlightthickness=2)
                widget.config(width=60,height=60 , bg="white",highlightbackground = "gray")
                widget.grid(row = i, column = j, padx=2, pady=2)
        self.config(highlightbackground = "gray")


if __name__=="__main__":


    window = tk.Tk()
    window.geometry("1440x1024")
    
    List1 = tk.Frame(window)
    
    # window.columnconfigure(0, weight=1)
    # window.columnconfigure(1, weight=1)
    # window.columnconfigure(2, weight=1)
    
    # List1.config(width=250,height=450 , bg="yellow")
    # List1.grid(row = 0, column = 0, pady = 2, padx=2)
    
    # List2 = tk.Frame(window)
    # List2.config(width=250,height=450 , bg="green")
    # List2.grid(row = 0, column = 2, pady = 2, padx=2)
    
    # List3 = tk.Frame(window)
    # List3.config(width=250,height=450 , bg="blue")
    # List3.grid(row = 1, column = 2, pady = 2, padx=2)
    
    # List4 = tk.Frame(window)
    # List4.config(width=250,height=450 , bg="red")
    # List4.grid(row = 1, column = 0, pady = 2, padx=2)
    


    board = GridInterface(window,7)
    board.place("1440x1024")

    window.mainloop()