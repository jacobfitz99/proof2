from tkinter import *
from tkinter import messagebox

lista = []

def guardar():
	n = nombre.get()
	ap = app.get()
	c = correo.get()
	t = telefono.get()
	lista.append(n+"$"+ap+"$"+c+"$"+t)
	escribirContacto()
	messagebox.showinfo("Guardado","El contacto ha sido guardado en la agenda")
	nombre.set("")
	app.set("")
	correo.set("")
	telefono.set("")
	consultar()
def eliminar():
	eliminado = conteliminar.get()
	removido = False
	for elemento in lista:
		arreglo = elemento.split("$")
		if conteliminar.get() == arreglo[2]:
			lista.remove(elemento)
			removido = True
	escribirContacto()
	consultar()
	if removido:
		messagebox.showinfo("Eliminar","Elemento eliminado"+eliminado)		
def consultar():
	r = Text(ventana,width=80,height=15)
	lista.sort()
	valores = []
	r.insert(INSERT,"Nombre\t\tApellido P\t\tTelefono\t\tCorreo\n")
	for elemento in lista:
		arreglo = elemento.split("$")
		valores.append(arreglo[2])
		r.insert(INSERT,arreglo[0]+"\t\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\n")
	r.place(x=20,y=300)
	spinTelefono = Spinbox(ventana,value=(valores),textvariable=conteliminar).place(x=460,y=100)
	if lista==[]:
		spinTelefono = Spinbox(ventana,value=(valores)).place(x=460,y=100)
	r.config(state=DISABLED)	
def iniciarArchivo():
	archivo = open("ag.txt","a")
	archivo.close()
def cargar():
	archivo = open("ag.txt","r")
	linea = archivo.readline()
	if linea:
		while linea:
			if linea[-1] == '\n':
				linea = linea[:-1]
			lista.append(linea)
			linea = archivo.readline()
	archivo.close()
def escribirContacto():
	archivo = open("ag.txt","w")
	lista.sort()
	for elemento in lista:
		archivo.write(elemento+"\n")
	archivo.close()

ventana = Tk()
nombre = StringVar()
app = StringVar()
correo = StringVar()
telefono = StringVar()
conteliminar = StringVar()
colorFondo = "#344"
colorLetra = "#FFF"

iniciarArchivo()
cargar()
consultar()
ventana.title("Agenda")
ventana.geometry("600x600")
ventana.configure(background=colorFondo)

etiquetaTitulo = Label(ventana,text="Agenda con archivos",bg=colorFondo,fg=colorLetra,font=("Helvetica",18)).place(x=180,y=15)
etiquetaN = Label(ventana,text="Nombre: ",bg=colorFondo,fg=colorLetra).place(x=30,y=100)
cajaN = Entry(ventana,textvariable=nombre).place(x=140,y=100)
etiquetaApp = Label(ventana,text="Apellido Paterno: ",bg=colorFondo,fg=colorLetra).place(x=30,y=150)
cajaApp = Entry(ventana,textvariable=app).place(x=140,y=150)
etiquetaT = Label(ventana,text="Telefono: ",bg=colorFondo,fg=colorLetra).place(x=30,y=200)
cajaT = Entry(ventana,textvariable=telefono).place(x=140,y=200)
etiquetaC = Label(ventana,text="Email: ",bg=colorFondo,fg=colorLetra).place(x=30,y=250)
cajaC = Entry(ventana,textvariable=correo).place(x=140,y=250)
etiquetaEliminar = Label(ventana,text="Telefono: ",bg=colorFondo,fg=colorLetra).place(x=350,y=100)
spinTelefono = Spinbox(ventana,textvariable=conteliminar).place(x=460,y=100)
botonGuardar = Button(ventana,text="Guardar",command=guardar,bg="#345",fg="white").place(x=175,y=272)
botonEliminar = Button(ventana,text="Eliminar",command=eliminar,bg="#345",fg="white").place(x=500,y=150)

ventana.mainloop()