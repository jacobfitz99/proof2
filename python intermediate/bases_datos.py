#####
#Bases de datos con sqlite
#####
#La estructura básica de una base de datos son las tablas 
#Siempre deben de llevar números
#3 etapas para crear una base de datos 1.-Diseño conceptual(Modelo entidad-relaciónentidad=tabla, atributo=columna)   2.-Diseño lógico (crow's foot, convertir a tabblas y columnas, SQL)  3.-Diseño físico

import sqlite3

conn = sqlite3.connect("alumnos.db")  # .db es la extension en sqlite, si no existe la base de datos la crea

cursor = conn.cursor()

print("\n\t\tBases de datos de los asistentes de python")

nombre = input("Ingresa el nombre del asistente")   #Esto de va a guardar en la base de datos
promedio = float(input("¿Qué promedio tiene el alumno?"))

######Crea Tablas      #DEspues de execute ya es lenguaje SQL y no python
try:
	cursor.execute('''
		CREATE TABLE alumnos(id integer primary Key, nombre text, promedio float)''')
except:
	print("Saltandose la creación de la tabla porque ya existe :D")	

cursor.execute('INSERT INTO alumnos(nombre,promedio) VALUES("%s","%f")'%(nombre,promedio))

conn.commit()   #Quita una variable el commit

#cursor.execute('DELETE FROM alumnos')        #Se esta borrando toda la tabla, alumnos es toda la columna 
#conn.commit

for row in conn.execute('SELECT * FROM alumnos ORDER BY promedio DESC'):
	print("Nombre: ",row[1],"Promedio: ",row[2])

conn.close()	