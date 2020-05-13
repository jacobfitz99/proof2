from tkinter import *

raiz = Tk()    #Raiz es el objeto que es la ventana

widget = Label(raiz, text="Mi primer GUI!")    #para ingresar un texto a la ventana raiz 
widget.pack()    #esta le inserta el texto a la ventana
raiz.mainloop()     #mandar a ejecutar la funcion con mainloop