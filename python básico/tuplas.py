#############
##Tuplas
#############


tupla = (1,"hola","adios",True)
tupla2 = 1,2,3,4,5,7,6  #empaquetamiento

print(tupla[1])     #indexación 

print(tupla2)

a,b,c,d,e,f,g = tupla2

print(d)

############ Se puede modificar una lista dentro de una tupla pero no toda la lista 

tuplachida = (("a","b","c"),[1,2,3])

tuplachida[1][0] = "hola"

print(tuplachida)

########################### Convertir una lista en tupla

listagay = [1,2,4,5]
print(type(listagay))

tuplacloset = tuple(listagay)

print(type(tuplacloset))

