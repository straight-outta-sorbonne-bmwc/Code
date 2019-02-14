from tkinter import *
from random import randrange
	
Fenetre = Tk()
can1 = Canvas(Fenetre, width=500, height=500, bg="white", bd=8)
can1.pack()

can1.create_rectangle(100, 100, 300, 200)
quitter = Button(Fenetre, text='Quitter', command=Fenetre.quit)
quitter.pack(side=BOTTOM)
Fenetre.mainloop()
Fenetre.destroy()

