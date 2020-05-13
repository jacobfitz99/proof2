###############
##POO - Clases - Métodos
################

class Persona:
	nombre = "Jorge"
	genero = "Masculino"
	edad = 23

	def dejar_tarea(self):
		print("10 Scripts para el jueves")
	def comer(self):
		print("Me gusta las papas")

jorge = Persona()

jorge.dejar_tarea()
jorge.comer()

#Constructor

class People:
	def __init__(self,nombre,genero)
		self.nombre = "nombre"
		self.genero = "genero"
people1 = People("Luis","Masculino")
people2 = People("Gerardo","Femenino")

people1.nombre
people2.genero

#La poo tiene 4 pilares: abstracción, herencia, polimorfismo, Encapsulamiento 

###Métodos magicos 
class Perro:
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad 
	def __add__(self,otro_perro):
		return self.edad + otro_perro.edad

sol = Perro("SOl",3)
bola = Perro("Bola",1)

print("Suma de edades: ",sol+bola)

#herencia 
class Animal:
	def respirar(self):
		print("Estoy respirando")
	def alimentarse(self):
		prine("Me estoy alimentando")

class Gato(Animal):
	def maullar(self):
		print("MiuauMiau")

gato1 = Gato()
print(gato1.respirar())
print(gato1.alimentarse())
print(gato1.maullar())








