from tkinter import *

raiz = Tk()

entrada = Entry(raiz)
boton = Button(raiz, text='Mandar')

var = StringVar()
entrada.config(textvariable=var)

def mandar():
	print('Recibido: ', var.get())

boton.config(command=mandar)
entrada.pack(side=LEFT, expand=YES, fill=X)       #fill X significa que se va a expandir pero sobre el eje de las X
boton.pack(side=RIGHT)
raiz.mainloop()	