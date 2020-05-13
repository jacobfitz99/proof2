#Hilos       #Tambien se conocen como procesos ligeros, un proceso se puede partir en varios hilos
#UN proceso ocupa mucha memoria mientras que los hilos muy poca

#Concurrencia vs paralelismo
#Concurrencia = varios procesos ejecutandose con un mismo nucleo
#Paralelismo = Los procesos se ejecutan al mismo tiempo, un proceso para cada nucleo

#Cluster = Varios elementos que trabajan de una manera colaborativa(no necesariamente deben ser computadoras)

#########################
#Programacion concurrente
#########################

import threading

def contar():
	contar = 0

	while contar < 10:
		contar += 1
		print("Hilo: ",threading.current_thread().getName(),"ID: ",threading.current_thread().ident,"Contador: ",contar)
		"""
hilo = threading.Thread(target=contar)
hilo1 = threading.Thread(target=contar)

#Ahora utilizamos el método "start" para ejecutar

hilo.start()
hilo1.start()"""

#hilos = []
def main():
	for i in range(100):
		hilos.append(threading.Thread(target=contar))
		hilos[i].start()

	for i in range(100):
		hilos[i].join() # Le dice al hilo principal que lo espere, porque cuando el hilo principal se apaga todo lo demas se muere

main()		
