class Deporte:
	def rapidez(self):
		print("Necesitas correr más rapido")

	def condición(self):
		print("Se ocupa mucha condición")

class Futbol(Deporte):
	def patear(self):
		print("Tiros libres")

class Basquetball(Deporte):
	def lanzar(self):
		print("Tiros libres Jordan")

jugador1 = Futbol()
print(jugador1.patear())
print(jugador1.rapidez())


