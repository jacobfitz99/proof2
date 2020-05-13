import sqlite3
import os
conn = sqlite3.connect("cursosProteco.db")        #Primero hay que crear la conexion y crear la base de datos
cursor = conn.cursor()

print('\n\t\tBases de datos de los cursos de Proteco')
#Crear las tablas
try:
	cursor.execute('''
		CREATE TABLE alumno(
		folio INTEGER PRIMARY KEY,
		nombreAlu TEXT,
		apPat TEXT,
		apMAT TEXT) ''')
	cursor.execute('''
		CREATE TABLE curso(
		idCurso INTEGER PRIMARY KEY,
		nombreCurso TEXT,
		cupo INTEGER)''')
	cursor.execute('''
		CREATE TABLE alumno_curso(
		folio INTEGER,
		idCurso INTEGER,
		calificacion FLOAT,
		FOREIGN KEY(folio) REFERENCES alumno(folio)        #constrains no llevan virul 
		FOREIGN KEY(idCurso) REFERENCES curso(idCurso)
		PRIMARY KEY(folio, idCurso))''')	
except:
	print("Saltandose la creación de las tablas porque ya existen :D")

while True:
	opcion = input("""
						\n1.-Registrar alumno
						\n2.-Registrar curso
						\n3.-Ver cursos
						\n4.-Inscribir curso	
						\n5.-Inscribir curso
						\n6.-Eliminar curso
						\n7.-Eliminar alumno
						\n8.-Actualizar datos alumno
						\n9.-Actualizar datos curso
						\n10.-Asignar/Cambiar calificación
						\n11.-Salir \t\tIngresa la opción que deseas realizar: """)
	if opcion == "1":
		folio = int(input("Ingresa el folio del asistente: "))
		nombreAlu = input("Ingresa el nombre del alumno: ")
		apPat = input("Ingrese el apellido paterno: ")
		apMAT = input("Ingrese el apellido materno: ")
		cursor.execute('INSERT INTO alumno(folio,nombreAlu,apPat,apMAT) VALUES("%d","%s","%s","%s")'%(folio,nombreAlu,apPat,apMAT))
		conn.commit()
		print("Alumno agregado exitosamente")
	elif opcion == "2":
		idCurso = int(input("Ingrese el id del curso: "))
		nombreCurso = input("Ingresa el nombre del curso: ")
		cupo = int(input("Ingresa el cupo del curso: "))
		cursor.execute('INSERT INTO curso(idCurso,nombreCurso,cupo) VALUES("%d","%s","%d")'%(idCurso,nombreCurso,cupo))
		conn.commit()
		print("Curso agregado exitosamente")
	elif opcion == "3":
		for row in conn.execute('SELECT * FROM curso ORDER BY idCurso ASC'):    #ASC forma ascendente
			print("id curso: ",row[0],"Nombre curso: ",row[1],"Cupo: ",row[2])
	elif opcion == "4":
		for row in conn.execute('SELECT * FROM alumno ORDER BY folio DESC'):    #DESC forma descendente
			print("folio: ",row[0],"Nombre: ",row[1],row[2],row[3])
	elif opcion == "5":
		os.system("cls")	
		print("Cursos disponibles: \n")			
		for row in conn.execute('SELECT * FROM alumno ORDER BY folio DESC'):    
			print("id curso: ",row[0],"Nombre curso: ",row[1],"Cupo: ",row[2])		
		folio = int(input("Ingresa tu folio: "))
		idCurso = int(input("Ingresa el Id del cruso a inscribir: "))
		cursor.execute('INSERT INTO alumno_curso(folio,idCurso) VALUES("%d","%d")'%(folio.idCurso))
		conn.commit()
	elif opcion == "6":
		idCurso = int(input("Ingresa el id del curso a borrar: "))
		for row in conn.execute('SELECT * FROM curso ORDER BY idCurso ASC'):
			print("id curso: ",row[0],"Nombre curso: ",row[1],"Cupo: ",row[2])
		cursor.execute("DELETE FROM curso WHERE idCurso=%d"%idCurso)
		conn.commit()
		print("Curso eliminado correctamente")			
	elif opcion == "7":
		pass
	elif opcion == "8":
		for row in conn.execute('SELECT * FROM alumno ORDER BY folio DESC'):    
			print("folio: ",row[0],"Nombre: ",row[1],row[2],row[3])			
		folio = int(input("Ingresa el folio del que deseas actualizar: "))
		opcioncambio = int(input("Qué campo quieres cambiar?: \n1.-Folio\n2.-Nombre\n3.-ApellidoMaterno"))
		if opcioncambio == 1:
			nuevofolio = int(input("Ingresa el nuevo folio: "))
			cursor.execute("""
				UPDATE alumno SET folio = "%d" WHERE folio"=%d" """%(nuevofolio,folio))
			conn.commit()
			print("Usuario actualizado")		
	elif opcion	== "9":
		pass
	elif opcion == "10":
		pass
	elif opcion == "11":
		print("Gracias por utilizar la base de datos del curso de proteco")
		break

conn.close()

