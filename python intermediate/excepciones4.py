numero = input("Da un número")
def sacarRaiz(numero):
	ocurre_error = True 
	try:
		num = float(numero)
		if num < 0:
			raise TypeError #Forzamos la invocación de una excepción
		print('La raiz del número',num,'es',num**0.5)	 
	except TypeError:
	 	print('Ocurrio una excepcion, cuidado con los negativos')
	 	ocurre_error = True  #Es redundante ponerlo

	else:
	 	ocurre_error = False
	finally:
	 	if ocurre_error == True:
	 		print('Algo salió mal')
	 	else: 
	 		print('Perfecto correcto entiendo')

sacarRaiz(numero)	 		

