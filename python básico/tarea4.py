###############
##Ejercicio 1 
###############






###############
##Ejercicio 2
###############

celcius = float(input("Ingresa los grados Celcius:\n"))
farenheit = float(input("Ingresa tus grados Farenheit\n"))
conversion1 = celcius*1.8 + 32
conversion2 = (farenheit - 32)/1.8
print("%d grados celcius equivalen a %d grados farenheit \n %d grados Farenheit equivalen a %d grados celsius"%(celcius,conversion1,farenheit,conversion2))

################
##Ejercicio 3
################

while True:
	numcorrecto = int(input("Adivina un número entre 1 y 9\n"))
	if numcorrecto == 1:
		print("Muy abajo")
	elif numcorrecto == 2:
		print("Sigues bajo prro")
	elif numcorrecto == 3:
		print("Deja de meter uno por uno")
	elif numcorrecto == 4:
		print("Todo meketrefe este no es")
	elif numcorrecto == 5:
		print("Todo manco")
	elif numcorrecto == 6:
		print("Dedicate a otra cosa")
	elif numcorrecto == 7:
		print("¿Todo mancazo")
	elif numcorrecto == 8:
		print("Echale más ganas")
	elif numcorrecto == 9:
		print("Por fin le atinaste prro")
		break
	else:
		print("¿Tus papás son primos? ese no es un número entre 1 y 9")


##################
##Ejercicio 4
##################




##################
##Ejercicio 5
##################

palabra = input("Inserta una palabra chistosa:\n")
print((palabra[::-1]))

##################
##Ejercicio 6
##################

num_pares = int(0)
num_impares = int(0)
num = [34,56,76,3,21,78,8,6,54,7,]
if num%2 == 0:
		num_pares = num_pares + 1
else:
		num_impares = num_impares + 1

print(num_impares,num_pares)			


