def LeerArchivos():
	leer = input("Ingresa el nombre del archivo: ")
	nombreArchivo = leer+".txt"

	try:
		archivo = open(nombreArchivo)
		cadena = archivo.readlines()
	except FileNotFoundError:
		print("El archivo no existe")
	else:
		print(cadena)
	finally:  #siempre se va a ejecutar finally
		print("Sismpre se ejecuta finally broo")



LeerArchivos()	