#Modulos que nos van a permitir enviar correos desde python 3
import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

print("*** Enviar correo desde Gmail ***")
#Datos quien va enviar enviar el correo
user = input("Cuenta gmail: ")
password = getpass.getpass("Contraseña: ")

#Definimos las cabeceras del emai
remitente = user
destinatario = input("Para, ejemplo <amigo@gmail.com>: ")
asunto = input("Asunto: ")
mensaje = input("Mensaje: ")
archivo = input("Adjuntar archivo: ")

#Host y puerto SMTP Gmail
gmail = smtplib.SMTP('smtp.gmail.com',587)

#Protocolo de cifrado que utiliza gmail
#Aqui comienza la transferencia
gmail.starttls()

#Credenciales del usuario
gmail.login(user,password)

# Establecer el nivel de salida de depuración. Un valor verdadero para el nivel da como resultado mensajes de depuración para la conexión y para todos los mensajes enviados y recibidos del servidor.
gmail.set_debuglevel(1)

# Indicamos que el header tendrá mpultiples valores
header = MIMEMultipart()
header['Subject']=asunto
header['From']= remitente
header['To']= destinatario

#Convertimos a html
mensaje = MIMEText(mensaje, 'html') #Contenido-tipo html
header.attach(mensaje)

"""
#Comprobando que el archivo exista
if (os.path.isfile(archivo)):
	adjunto = MIMEBase('application', 'octet-stream')
	adjunto.set_payload(open(archivo, "rb").read())#leemos el contenido del archivo
	encode_base64(adjunto)
	adjunto.add_header('Content-Disposition', 'attachment; filename="%s"'%os.path.basename(archivo))
	header.attach(adjunto)
"""

#Enviar email, adjuntandolo como una cadena
gmail.sendmail(remitente, destinatario, header.as_string())

#Cerrar la conexion SMTP
gmail.quit()