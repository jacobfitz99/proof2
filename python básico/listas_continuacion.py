#################
#Listas continuación
##################


lista = [2,3,6,4,6,1]

#los que acaban como .count, .reverse son métodos

print("La lista tiene %d elementos" % len(lista))   #len es una función que cuenta la cantidad de elementos en una lista 
print("El número %d se repite %d veces" %(lista[2],lista.count(lista[2])))  #Cuenta la cantidad de veces que se repite un elemento que le digamos 


#Incertar un elemento en una lista por posición 
lista.insert(0,7)  #Mete un 7 en la posición 0

print(lista)

#Eliminar elemento de una lista por posición 
del lista[1]
print(lista)

print("El número mayor de la lista es: %d " % max(lista) )
print("El número menor de la lista es: %d " % min(lista) )


######################### Paso por valor (Si modificas la segunda no se modifica la primera)

a = 4
b = a

print("a =",a)
print("b =",b)

b = 120

print("a =",a)
print("b =",b)

########################### Paso por referencia (si modificas la segunda tambien se modifica la primera)

l1 = ["a","b","c"]
l2 = l1

print("lista 1:",l1)
print("lista 2:",l2)

l2[0] = 1

print("lista 1:",l1)
print("lista 2:",l2)

######################### Copiar lista 

l3 = l1.copy()

print("Lista 2: ",l3," id",id(l3))

l3[1] = 2
print("lista 2: ",l3," id",id(l3))



