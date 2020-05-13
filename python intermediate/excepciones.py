
while True:
	try:
	  #Toda aquella instrucción que pueda levantar una excepción 
	  x = int(input("Ingrese un número: "))   #12,A
	except ValueError:
		print('El caracter ingresado no es el requerido')
	else:
		print('Todo salio a la perfección')	
