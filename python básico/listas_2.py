#########
# listas 
#########

mandado = ['jabon',
           'comida',
           'sopa',
           'agua',
           'pan',
           'leche',
           'cereal',
           'atun',
           'cafe']



print(mandado[1:])   
print('Me falta por comprar:', mandado[6:9])
print(mandado[5])

vocales = ['E','I','O']
vocales += ['A']

# Casteo o conversión a otro tipo de dato con función

vocales = list('U') + vocales 
print(vocales)

#Métodos internos de la clase List

vocales.sort()
print(vocales)
mandado.sort()
print(mandado)

numeros = [3,7,9,14,25,75,23,2]
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)

numeros[4] = 100 #Sí soporta asignación del item
print(numeros)

lista = [1,"hola",True,[1,2,3]]

print(lista[1][1:4])
print(lista*3)

print(lista[-4])

print(lista.index(1))
lista.insert(3,"A")
print(lista)

lista.pop() #.pop elimina el último elemento de la lista 
print(lista)

lista.remove("hola") #se usa para eliminar un dato en específico
print(lista)






