#################
#Condicionales
#################

calculo = int(input("¿Cuánto sacaste en calculo?\n"))
algebra = int(input("¿Cuánto sacaste en algebra?\n"))
ecuaciones_diferenciales = int(input("¿Cuánto sacaste en ecuaciones diferenciales\n"))
termodinámica = int(input("¿Cuánto sacaste en termodinámica?\n"))
química = int(input("¿Cuánto sacaste en química?\n"))

resultado = (calculo + algebra + ecuaciones_diferenciales + termodinámica + química)/5

if resultado >= 7:
	print("Estas chido, aprobaste!")
else: 
	print("Estas chavo, te veo el otro semestre!")

###############
#Condicional anidado
###############
peso = float(input("Ingresa tu peso:  \n"))
altura = float(input("Ingresa tu estatura  \n"))

imc = peso/altura**2

if imc>18.5 and imc<24.5:
	print("Estas normal, no te preocupes IMC = %d" %imc)
elif imc>25 and imc<29.9:
	print("Estas en sobrepeso bajale a los tacosIMC = %d" %imc)
elif imc>30 and imc<34.4:
	print("prohibido los tacosIMC = %d" %imc)
else: 
	print("Estas a un taco de morirIMC = %d" %imc)
