#####################
# Foreach
#####################

lista = [1,2,3.14,"Hola",True,(2,3)]

for elemento in lista:
	print("[%d] elemento: %s" %(lista.index(elemento),elemento)) # El elemento 1 tiene el índice 0 al igual que el True porque es una referencia

dias =('Lunes',
	   'Martes',
	   'Miercoles',
	   'Jueves',
	   'Viernes',
	   'Sabado',
	   'Domingo'
	   )
for dia in dias:
	if dia == 'Viernes':
		print("Vamos por unas chelas")
	else:
		print("Hoy no toca, vamos al curso")

#Iteración para diccionarios

calificaciones = {'Jorge': 10,
				  'Cesar': 9,
				  'Jocelyn': 8,
				  'Jacob': 7}

#Los nombres de las personas son las llaves 

for alumno in calificaciones:
	print("%s sacó %d" %(alumno,calificaciones[alumno]))


#Iteración para desempaquetar (tuplas)

colores_favs = [("Jorge","Azul"),
				("Itzel","Verde"),
				("Enrique","Rojo"),
				("Jesús","Morado"),
				("Angel","Vino")]

for nombre,color in colores_favs:
	print("El color %s es el favorito de %s" %(color,nombre))


#Iteración sobre cadena

for letra in "Ya mañana es viernes!":
	print(letra+"-")

	


