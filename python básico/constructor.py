#Constructor

class People:
	def __init__(self,nombre,genero):
		self.nombre = "nombre"
		self.genero = "genero"
people1 = People("Luis","Masculino")
people2 = People("Gerardo","Femenino")

print(people1.nombre)
print(people2.genero)