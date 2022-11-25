from tkinter import *
 
root = Tk()
 
def afficher():
    print(my_entry.get())
 
bouton=Button(root, text="Afficher", command=afficher)
bouton.pack(side=TOP, padx=50, pady=10)
 
my_entry = Entry(root)
my_entry.pack()
 
root.mainloop()