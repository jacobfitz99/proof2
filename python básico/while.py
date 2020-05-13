###############
#Ciclo while mientras 
###############

respuesta =""

while respuesta != "salir":
	respuesta = input('escribe')



numero = 0

while numero <10:
		numero += 1

		if numero == 5:
			continue 
		print("interacion: %d" % numero)
