import math 

class NoPolinomioSegundoGrado(exception):
	pass
class RaicesImaginarias(exception):
	pass   #No hace nada 

def chicharronera(a,b,c):
	try:
		if a == 0:
			raise NoPolinomioSegundoGrado
		elif b**2 -4*a*c <0:
			raise RaicesImaginarias	
		else:
			print("x_1 = ",(-b+math.sqrt(b**2 -4*a*c) )/2*a)
			print("x_2 = ",(-b+math.sqrt(b**2 -4*a*c) )/2*a)	


	except NoPolinomioSegundoGrado:
		print('La ecuación no es un polinomio de segundo grado')
	except RaicesImaginarias:
		print('La ecuacion tiene raices complejas')	

chicharronera(1,0,11)		

