def recibiNumero(numero):
	try:
		num = float(numero)
		print('El numero elevado al cuadrado es: ',numero**2)
	except(ValueError, TypeError) as excepcion:  #TypeError: 5+'A'     ValueError: float() 	
		print('Las caracteristicas del error son: ',excepcion)
	except:
		print('Algo salió mal, contactate con el administrador')	

recibiNumero("google")