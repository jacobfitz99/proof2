import csv

with open('users.csv') as file:
	reader = csv.DictReader(file, delimiter=',') #Dictreader convierte a diccionario

	print(reader)

	for row in reader:
		print(row['Nombre'], "->", row['Correo'])  #esto sirve para que solo nos arroje la info específica 