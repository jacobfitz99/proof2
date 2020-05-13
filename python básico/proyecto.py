################
#Juego del ahorcado
################

#Ornelas Fitz Jacob Neftali

import random

def lista_palabra():
	palabras = ['Python',
		'Jorge',
		'Universidad',
		'Canada',
		'Hermano',
		'Ajedrez',
		'Nemo',
		'Tenis',
		'Economia',
		'Frutas',
		'Joker',
		'Nantes',
		'Rumania',
		'Bucarest',
		'Frances',
		'Terricola',
		'Tenochtitlan',
		'Procrastinar']
	return random.choice(palabras).upper()

def revisa(palabra,pistas,encontrar):
	encontrar = encontrar.upper()
	resultado = ''
	j = 0
	aciertos = 0
	for letra in palabra:
		if letra in pistas:
			resultado += letra
		else:
			resultado += '*'

		if letra == encontrar:
			aciertos += 1
	if aciertos > 1:
		print('Siiiuuu, la palabra contiene',aciertos,'"' + encontrar + '"' + 's')
	elif aciertos == 1:
		print('Siiiuuu, la palabra contiene la letra"' + encontrar + '"')
	else:
		print('La palabra no contiene la letra"' + encontrar + '"')
	return resultado	


def inicio():
	palabra = lista_palabra()
	pistas = []
	adivinado = False 
	print('La palabra es de ',len(palabra),'letras.')
	while not adivinado:
		mensaje = 'Inserte una letra o una palabra de {} letras. '.format(len(palabra))
		encontrar = input(mensaje)
		encontrar = encontrar.upper()
		if encontrar in pistas:
			print('Encontraste "' + encontrar + '"')
		elif len(encontrar) == len(palabra):
			pistas.append(encontrar)
			if encontrar == palabra:
				adivinado = True
			else:
				print('Incorrecto, vuelve a intentarlo.')
		elif len(encontrar) == 1:
			pistas.append(encontrar)
			resultado = revisa(palabra,pistas,encontrar)
			if resultado == palabra:
				adivinado = True

			else:
				print(resultado)
		else:
			print('Cáracter invalido.')	
	print('Siiiuuu, adivinaste la palabra', palabra + ', crack! tan sólo en ', len(pistas), 'intentos.')
			
inicio()


	
		