import threading

class MiHilo(threading.Thread):
	def __init__(self,num):
		threading.Thread.__init__(self)
		self.num = num

	def run(self):
		#Todo el codigo que quiero que se ejecute como hilo
		#start()
		print("Soy el hilo: ",self.num)
#Este es el hilo principal
def main():

	for i in range(10):
		hilo = MiHilo(i)
		hilo.start()               #start la forma de ejecutar la funcion con los hilos 
		hilo.join()

	print("Soy el hilo principal")		

main()		 	
