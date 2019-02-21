from tkinter import *
from random import randrange
	

def avancer():
	global x0, y0, x1, y1
	x0, x1= x0+10, x1+10

	can1.move (rectangle, 10, 0)
Fenetre = Tk()
can1 = Canvas(Fenetre, width=500, height=500, bg="white", bd=8)
can1.pack()

x0, y0, x1, y1 = 100, 100, 300, 200
rectangle = can1.create_rectangle(x0, y0, x1, y1, fill='green')
avancer = Button(Fenetre, text='avancer', command=avancer)
quitter = Button(Fenetre, text='Quitter', command=Fenetre.quit)
quitter.pack(side=BOTTOM)
avancer.pack(side=RIGHT)
Fenetre.mainloop()
Fenetre.destroy()

