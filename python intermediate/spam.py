import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

print('*********** Enviar correos desde gmail************')

#Datos de quien va a enviar el correo
user = input ("Cuenta de gmail")
password = getpass.getpass("Contraseña: ")    #Se utiliza para tapar la contraseña que inserta el usuario

#Definimos las cabeceras del Email

remitente = user
destinatario = input('Para ejemplo: amigo@gmail.com')
asunto = input('asunto')
mensaje = input('mensaje')

#host y puerto SMTP Gmail

gmail = smtplib.SMTP('smtp.gmail.com','587')

#Aqui comienza la transferencia 
gmail.starttls()

gmail.login(user, password)

gmail.set_debuglevel(1)

header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente 
header['To'] = destinatario

#convertir a html
mensaje = MIMEText(mensaje, 'html')
header.attach(mensaje)

gmail.sendmail(remitente, destinatario, header.as_tring())

gmail.quit()
