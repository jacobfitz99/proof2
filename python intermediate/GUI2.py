from tkinter import *

label1 = Label(text='Texto...')                  #Cuando no creamos una raiz(ventana) como en el ejemplo pasado se crea por default  
label2 = Label(text='Mas texto...', bg='cyan')   #bg es back ground para poner color

label1.pack(side = LEFT, fill=BOTH, expand=YES)    #expand es para expandir
label2.pack(side = RIGHT, fill=BOTH, expand=YES)     #fill es para llenar 

mainloop()