###############
#Cadenas
###############
cadena = "¿Acaso hubo búhos acá?"

#Indexación

print(cadena[12:17])

#Subcadenas

print(cadena[12:17],"y aguilas")

#Concatenación

Saludoespañol = "Hola amigo"
Saludofrances = "Bonjour mon amie"
despedidaespañol = "Hasta luego" 
despedidafrances = "  Á plus tard"
frases = Saludofrances + despedidafrances
print(frases)

#Cadena cruda

print("La UNAM es la mejor universidad de \nMéxico")
print(r"La UNAM es la mejor universidad de \nMéxico")

#Placeholders

k = 5
h = 7 
print("Mi número favorito es %d y el %d " % (k,h))



###############
#Listas
###############

materias = ["Taller","Econometría","Industrial","Francés","INAE","Ecopol","Python","Macroeconomía","Historia"]

#Ordenamiento

materias.sort()
print(materias)

#Indexación 

print("Mis materias más faciles son:",materias[8],",",materias[1],"e",materias[3])
materias[2] = "Estadística"
print(materias)
materias.pop()
print(materias)
materias.remove("Estadística")
print(materias)
print(materias*10)

#################
#Tuplas
#################

tuna = ("autor",31,55,"est","best",88,"física",True,55,"física","Dostoievski","pithon")

#Indexación

print(tuna[10],tuna[3],tuna[1],tuna[4],tuna[0])

#Empaquetamiento 

tuna2 = 1,2,3,4,5,6,7,8,9,10,11,12,13
print(tuna2)

#Desempaquetamiento

c,o,r,e,a,d,e,l,n,o,r,t,e = tuna2
print(l)

#Replace 

tunasfrescas = (("h","i"),["Hello","my","dear"])
tunasfrescas[1][2] = "friend"
print(tunasfrescas)

#De lista a tupla 

listade_tunas = ["tunas de Jalisco","Tunas de Hidalgo","Tunas de Guerrero"]
print(type(listade_tunas))
procedencia_detunas = tuple(listade_tunas)
print(type(procedencia_detunas))

################
#Diccionarios
################
tarjetas = {"bbva":45,"scotiabank":91,"santander":38}
print(tarjetas)

#Buscar por valores 
print(tarjetas["santander"])
print("El pin de la tarjeta de crédito bbva es %d"  % tarjetas["bbva"])

#Actualizar y añadir un elemento

tarjetas.update({"scotiabank":38})

tarjetas.update({"hsbc":55})

print("El pin de la tarjeta de credito scotiabank es: ",tarjetas["scotiabank"])
print(tarjetas)

#imprimir llaves,valores y ambos 

print(list(tarjetas.keys()))
print(list(tarjetas.values()))
print(list(tarjetas.items()))






