#codeshare.io/pythonProteco
#ruta absoluta y ruta relativa

archivo = open("./poema.txt","r") #r = read #un punto al inicio busca en la carpeta actual #dos puntos busca en la carpeta anterior
lineas = 0
for i in archivo:
	if i=="\n":
		pass
	else:
		lineas+=1	
#texto = archivo.read()

archivo.close() #CLose siempre cerrarlo
print("El documento tiene",lineas,"renglones para leer")
#print(texto)