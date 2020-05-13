#####################
#Diccionarios
#####################

#Estructuras que mapean un objeto llave-valor

diccionario = {"uno""Jorge","dos:""Daniel","tres:""Alma"} #La llave es inmutable, no puede ser una lista pero el valor sí puede ser lo que sea 

print(diccionario)

print(diccionario["uno"])   #Buscar por valor

calificaciones = {"Jorge": [1,2,3,4],"Bruno":8,"Oscar":1}

print("La calificación de Jorge es: %s"
	% calificaciones["Jorge"])

cals_jorge = calificaciones.get("Jorge")  #Obtiene el valor. Con get no marca error si no existe previamente el valor pero pero con los corchetes sí
print("Calificaciones Jorge: ", cals_jorge)
calificaciones.update({"Jorge:"10})
calificaciones.update({"Isa":10})

print("Califiaciones Jorge: ",calificaciones["Jorge"])
print(calificaciones)

#llaves 

print(list(calificaciones.keys()))

#Valores

print(list(calificaciones.values()))


#Llaves y valores 

print(calificaciones.items())

#Copia

calificaciones_copia = calificaciones.copy()


