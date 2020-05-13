from tkinter import *
from webbrowser import *
from tkinter import messagebox 
def fun_saludar():
	print("Hola mundo")

def fun_despedir():
	print("Adios mundo")

def buscar_google():
	open_new('www.google.com')		

def lanzar_alerta():
	messagebox.showinfo('Alerta!!!!')

raiz = Tk()                           #Con raiz como objeto podemos ponerle titulo y ponerle demas funciones
raiz.title('Botones')               #Para darle un titulo 		
raiz.geometry('400x200')            #Espicifa el tamaño de la ventana

label = Label(raiz, text='Cuatro botones')
boton1 = Button(raiz, text='Saludar', command=fun_saludar, bg="#A9CCE3", bd=23)                               #Botton viene en la paqueteria y command es lo que pasa cuando clickeamos el boton
boton2 = Button(raiz, text='Despedir', command=fun_despedir, bg="#765F93")                               #Botton viene en la paqueteria y command es lo que pasa cuando clickeamos el boton
boton3 = Button(raiz, text='Google', command=buscar_google, bg="#186A3B")                               #Botton viene en la paqueteria y command es lo que pasa cuando clickeamos el boton
boton4 = Button(raiz, text='Alerta', command=lanzar_alerta, bg="#A9CCE3")                               #Botton viene en la paqueteria y command es lo que pasa cuando clickeamos el boton


label.pack(side=TOP)
boton1.pack(side=LEFT, fill=BOTH, expand=YES)
boton2.pack(side=RIGHT, fill=BOTH, expand=YES)

boton3.pack(side=TOP)
boton4.pack(side=BOTTOM)

raiz.mainloop()

