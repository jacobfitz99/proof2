import re 

texto = "El día de hoy en la clase de python continuamos aprendiendo expresiones regulares en python 3, porque preogramar en python es cool "
cadena = "expresiones regulares"

print(re.search(cadena,texto))         #search te dice en qué parte del texto se encuentra el match 

isMatch = re.search(cadena,texto)

if isMatch is not None:
	print("Hizo match")
	print("El match inicia en: ",isMatch.start())
	print("El match termina en: ",isMatch.end())
	print("El match se hizo en: ",isMatch.span())        #span da la ubicacion de cual a cual numero de caracter
	print("El match fue: ",isMatch.group())            #nos dara el match completo
else:
	print("No hubo match")	
