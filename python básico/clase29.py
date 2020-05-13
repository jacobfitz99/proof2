####################
#Funciones
####################

def hola_mundo(nombre):
	print("Hola mundo de %s"%nombre)
	return

hola_mundo("Jacob")


####
def holamundo(nombre):
	saludo = "Hola mundo de :" + nombre
	return saludo

saludo_regresado = hola_mundo("Jacob")


####
def holamundo(nombre):
	"""
	Función que saluda a una persona
	:param nombre Nombre de quien se va a saludar    
	return saludo El saludo que se va a mandar
	"""
	saludo = "Hola mundo de: " + nombre
	return saludo

print(saludo_regresado)

print(hola_mundo.__doc__)

###########################################
def sumatoria(x,y):
	return x+y

def resta(x,y):
	return x-y

def multiplicación(x,y):
	return x*y

def división(x,y):
	return x/y

def modulo(x,y):
	return %x,%y 
	
