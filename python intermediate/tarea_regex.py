import re

texto = "Se insertara un correo electrónico común y válido por ejemplo juanrobles13@gmail.com con el fin de probar que se puede encontrar un correo dentro de un texto"
correo = "[\w\.-]+@[\w\.-]+"

print(re.search(correo,texto))

haymatch = re.search(correo,texto)

if haymatch is not None:
	print("Hay un correo en el texto")
	print("El correo es: ", haymatch.group(0))
else:
	print("No hay algun correo en el texto :( ")	