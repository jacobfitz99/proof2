import re 

"""asistentes = ['Armando Arzola','Xochitl Arzola','Jacob Ornelas','Julio Martinez','Johnatan Popoca','Bryan Popoca']
for i in asistentes:
	if re.findall('(Arzola)$',i):
		print(i)
	else:
		print('No hubo coincidencias')	

def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))
patrones = ['ho{0,1}la','ho{1,2}']				
texto = 'Hla hola hoola hooola hooooooola'
buscar(patrones,texto)"""

######
######
######
"""
def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))
patrones = ['h[ou]la','h[aio]la','h[aeiou]la'] #ponemos entre parentesis los caracteres que queremos discriminar 
texto = 'hala hela hila hola hula'
buscar(patrones,texto)
"""
#####
####
#####3

def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))       #findall busca y te regresa como lista 
patrones = ["h[a-z]la","h[0-9]la","[A-z]{4}","[A-z][A-z0-9]{3}"]  #los numeros entre corchetes es la cantidade de letras que deben de tener las plabras que se buscan
texto = 'hols h0la Hola, mola m0la M0la Abcd acde' 
buscar(patrones,texto)            #se tiene que manda a llamar a la funcion para que regrese los valores 