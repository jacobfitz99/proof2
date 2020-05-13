#Cliente
##importamos el modulo para trabajar con sockets
import socket
##Definimos una vable para guardar la IP
recvIP=input("Ingresa la IP a la que te quieres conectar: ")
#Creamos un objeto socket para el servidor
s = socket.socket()
#Nos conectamos al servidor con el metodo connect. Tiene dos parametro
# el primer parametro es la IP del servidor
#el segundo parametro es el puerto de conexion
s.connect((recvIP,9000))

#Creams un bucle infinito para retener la conexion
while True:
	#para mandar el mensaje temos que instanciar una entrada de datos
	mensaje=input("Ingresa mensaje: ")
	#Para enviar el mensaje e tiene que instanciar del objeto del servidor (s) y con el metodo sent
	s.send(mensaje.encode())
	#Si por alguna razon si el mensaje es close cerramos la conexion
	if mensaje=="adios":
		break
	respuesta=s.recv(1024).decode()
	print("Respuesta del servidor: ", respuesta)
#Imprimimos cuando se cierra la conexion
print("Conexion finalizada :)")
#Cerramos la instancia del objeto servidor
s.close()