
import csv

file = open('users.csv','r')  #base de datos de "randomusers" 
reader = csv.reader(file)

#for linea in reader:
#	print(linea)

filas = 0
for linea in reader:
	if filas == 0:
		header = linea
		print(header)
	else:
		columnas = 0
		for dato in linea:
			print("Fila %d, columna %d, Contenido: %s"%(filas, columnas+1, dato))
			columnas +=1
	filas +=1
	print()
file.close()	

#Crear copia csv

infile = open('users.csv')
outfile = open('copia.csv','w')

reader = csv.reader(infile)
writer = csv.writer(outfile, delimiter="|")

for linea in reader:
	writer.writerow(linea)

infile.close()
outfile.close()				
