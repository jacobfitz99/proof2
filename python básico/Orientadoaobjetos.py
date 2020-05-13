class Coche:                      #Las clases siempre empiezan por mayúsculas
	def avanzar(self):            #Las clases de dos palabras se separan asi CocheViejo
		print("Ruummm")
	def sonar(self):               #Se utiliza el self porque son métodos
		print("Piiiip!")

#Poner los métodos 
coche1 = Coche()
coche2 = Coche()
coche1.avanzar()
coche2.sonar()

#Poner caracteristicas 

llantas = 4
peso = 800
Coche.llantas()
