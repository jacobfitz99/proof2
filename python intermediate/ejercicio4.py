########ejercicio de una agenda

print("Bienvenido a la agenda electronica")
print("¿Qué accion desea realizar?")

def menu():
	print("1.- Agregar contacto\n2.- Modificar contacto\n3.- Ver lista de contactos\n4.-Eliminar contactos\n5.-Salir")

menu()
eleccion = "0"
while eleccion != "5":
	eleccion=input()
	if eleccion == "1":
		with open("agenda.txt","a") as agenda: #renombra la variable 
			datos=["\nnombre"," ","numero\n"]
			datos[0]=input("Nombre del contacto: ")
			numero = input("Numero telefonico: ")
			datos[2] = numero+"\n"
			agenda.writelines(datos) #convierte en listas el archivo
			menu()
	elif eleccion == "2":
		modificando=input("¿A quien deseas modificar?\n")
		nuevoNombre=input("Ingresa nuevo nombre:  ")
		nuevoNumero=input("Ingresa nuevo numero:  ")
		agenda = open("agenda.txt","r")
		listasAuxiliares = agenda.readlines()
		agenda.close()
		agenda = open("agenda.txt","w")
		for line in listasAuxiliares:
			a=linea.split()
			if a [0] == modificando: 
				agenda.write(nuevoNombre + "" + nuevoNumero+"\n")
			else:
				agenda.write(linea)
		agenda.close()
		menu()
	elif eleccion == "3":
		print("Tus contactos son: \n")
		with open("agenda.txt","r") as agenda:
			for i in agenda:
				print(i)
		menu()
	elif eleccion == "4":
		eliminando=input("A quien deseas eliminar?\n")
		agenda = open("agenda.txt","r")
		listasAuxiliares = agenda.readlines()	
		agenda.close()

		agenda = open("agenda.txt","w")
		for linea in listasAuxiliares:
			a = linea.split()
			if a[0] == eliminando:
				pass
			else:
				agenda.write(linea)
		agenda.close()
		menu()			

#tarea pasar todo a mayusculas 	 					

