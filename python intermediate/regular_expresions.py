##########
#Expresiones regulares
##########

###Metacaracteres

import re 

texto = "La tarde de hoy en la clase de python aprendermos expresiones regulares en python, porque python es cool"

cadena = 'python'
print(re.findall(cadena,texto))    #Regresa una lista con las concordancias que encuentra
tamaño = len(re.findall(cadena,texto))
print(tamaño)


