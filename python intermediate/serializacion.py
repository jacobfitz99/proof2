import pickle

poema = """Cuantas veces, amor sin reconocer tu mirada, sin mirarte, centaura, 
en regiones contrarias, en un mediodía quemante: 
eras sólo el aroma de los cereales que amo. 
Tal vez te vi, te supuse al pasar levantando una copa 
en Angola, a la luz de la luna de Junio, 
o eras tú la cintura de aquella guitarra 
que toqué en las tinieblas y sonó como el mar desmedido. 
Te amé sin que yo lo supiera, y busqué tu memoria. 
En las casas vacías entré con linterna a robar tu retrato. 
Pero yo ya sabía cómo era. De pronto 
mientras ibas conmigo te toqué y se detuvo mi vida: 
frente a mis ojos estabas, reinándome, y reinas. 
Como hoguera en los bosques el fuego es tu reino."""

#Creamos el archivo binario

fichero_binario = open('poema.txt','wb')

pickle.dump(poema, fichero_binario)  #lo convierte a binario

fichero_binario.close()

fichero = open('poema.txt','rb')
lista = pickle.load(fichero)   #lo convierte de binario a normal

#print(lista)

import marshal

#serializar datos

archivoDump = marshal.dumps(poema)
print(archivoDump)    

#descompirimir datos