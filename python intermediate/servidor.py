#Servidor
#Importamos el modulo Socket
import socket
recvIp=input("Ingresa la Ip a la que quieres conectar: ")
#intanciar un objeto para trabajar con socket
ss=socket.socket()
#Con el metodo bind le indicamos que puerto debe escuchar
ss.bind((recvIp,9000))
#El numero de conexiones entrantes que vamos a aceptar
ss.listen(1)
#Intanciamos un objeto sc (socket client) para recibir datos, al recibir
# estos devolvera tambien un objeto que representa un tupla con los datos de conexion (IP, puerto)
conn,addr=ss.accept()
print("Iniciando el servidor!")
print("Cliente conectado desde: ",addr[0],": ",addr[1])

while True:
	#Recibimos el mensaje
	recibido=conn.recv(5000).decode()
	#Si el mensaje es adios se cierra la conexion
	if recibido=="adios":
		break
	#Si recibimos los datos nos muestra la IP y el mensaje recibido
	print("Cliente dice: ",recibido)
	#Devolvemos el mensaje al cliente
	conn.send(input("Ingresa tu mensaje: ").encode())
print("Se ha terminado la conexion :)")
ss.close()
