from tkinter import *

contador = 0
def aumentar():
	global contador
	contador +=1
	label.config(text=contador)

def disminuir():
	global contador
	contador -=1
	label.config(text=contador)      #Config es para configurar la etiqueta

raiz=Tk()
raiz.title('Contador')

label = Label(raiz, text = contador, bg='blue')

boton1 = Button(raiz, text = 'Aumentar', command=aumentar)		
boton2 = Button(raiz, text = 'Disminuir', command=disminuir)

label.pack(fill=BOTH, expand=YES, side=TOP)


boton1.pack(fill=BOTH, expand=YES, side=RIGHT)		
boton2.pack(fill=BOTH, expand=YES, side=LEFT)	
raiz.mainloop()	