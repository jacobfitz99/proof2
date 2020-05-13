#contador de palabras 
archivo = open("Test.txt","w")
archivo.write("Este texto tiene cinco palabras")

archivo.close()

archivo = open("Test.txt","r")
for linea in archivo:
	print(linea)

archivo.seek(0) #Pone el puntero en la posicion inicial

listaArchivo=archivo.readlines()  #cuenta las lineas 
contadorPalabras=0

print(listaArchivo)

for elemento in listaArchivo:
	contadorPalabras+= len(elemento.split())

print("El archivo tiene",contadorPalabras,"palabras")	

archivo.close()	

#####################
cadena ="Hola me, llamo Julio, y me programar"