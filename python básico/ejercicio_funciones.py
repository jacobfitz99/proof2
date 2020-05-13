def dar_datos(nombre,telefono,cuenta):
	datos = []
	nombre = input("Ingresa tu nombre: ")
	datos.append(nombre)
	telefono = int(input("Ingresa tu telefono: "))
	datos.append(telefono)
	cuenta = int(input("Ingresa tu cuenta: "))
	datos.append(cuenta)
	return datos
print(dar_datos)


