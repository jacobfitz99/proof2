############
# Cadenas 2 
# cuestionario: bit.ly/2Mgiqar
############

#Características de las canedas 

#Indexación 
cad = "Hola"
print(cad[0])
print(cad[1])
print(cad[2])
print(cad[3])
# cad[1] = 'u' #no se puede porque es inmutable 

#subcadenas, slicing -> rebanada

print(cad[1:4], "ke ase?")
cad2 = '¿Como estan?'
print(cad2[5:10])
print(cad2[7:10])
print(cad2[6:11])

#concatenación

saludo = 'Qué onda!'
despedida = 'Adios!'

salusdespedida = saludo + despedida
print(salusdespedida)
print(saludo + despedida)

halago = 'El profe es el:'

bueno ='\nmejor'
malo = 'peor'

print(halago,bueno*100)
print(malo)

#cadena cruda
print('Python es \nlo máximo!!!')

print(r'Python es \nlo máximo!!!')

# Placeholders
a = 2
b = 3
print('El valor a es: %d y de b es %d' %(a,b))


