#re.match  busca caracteres al principio del texto
#re.search   busca los caracteres en todo el texto 
#re.findall    

import re

print(re.match("hola","hola"))   #match busca patrones y despues te dice que fue lo que hizo
if re.match("hola","hola"):
	print("Hizo match")

if re.match(".ola","tola"):
	print("Hizo match")

if re.match("hola","hola"):
	print(re.match("python|jython|cython","cython"))  #te regresa el match y dónde se ubica dentro de la palabra
	print("Hizo match")

if re.match("(p|j|c)ython","python jython cython"):
	print(re.match("(p|j|c)ython","python jython cython"))
	print("Hizo match")

if re.match("[pjc]ython","cython"):
	print(re.match("[pjc]ython","cython"))
	print("Hizo match")

if re.match("niñ(a|o)s","niñas niños"):
	print(re.match("niñ(a|o)s","niñas niños"))
	print("Hizo match")

if re.match("cadena[0-9]","cadena1 cadena1"):
    print(re.match("cadena[0-9]","cadena cadena1"))
    print("Hizo match")

if re.match("python+","pytho pythonnnnnn"):    #+ comienza de 1 en adelante
	print(re.match("python+","pytho pythonnnnnn"))
	print("Hizo match")

if re.match("python*","pytho"):
	print(re.match("python*","pytho"))
	print("Hizo match")

if re.match("pytho?","pytho python"):        #signo de interrogacion es solo 0 o 1
	print(re.match("pytho?","pytho python"))
	print("Hizo match")

if re.match("^http","http://google.com"):    #^en los rangos sirve para negarlos, sólo es solamente al principio
	print(re.match("^http","http://google.com"))    #^en los rangos sirve para negarlos, sólo es solamente al principio
	print("Hizo match")





	