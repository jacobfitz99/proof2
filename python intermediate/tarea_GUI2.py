from tkinter import *
import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

def enviar():
	gmail = smtplib.SMTP('smtp.gmail.com',587)
	header = MIMEMultipart()
	header['Subject']=asunto.get()
	header['From']= remitente.get()
	header['To']= destinatario.get()
	gmail.starttls()
	gmail.login(user.get(),password.get())
	gmail.set_debuglevel(1)
	header.attach(mensaje.get())	
	gmail.sendmail(remitente, destinatario, header.as_string())
	gmail.quit()

ventana = Tk()
ventana.title("Enviar Emails")
ventana.geometry("600x400")

user = StringVar()
password = StringVar()
remitente = user
destinatario = StringVar()
asunto = StringVar()
mensaje = StringVar()
archivo = StringVar()

etiqueta1 = Label(ventana,text="Cuenta de gmail: ").place(x=10,y=10)
user_caja = Entry(ventana,textvariable=user).place(x=120,y=10)
etiqueta2 = Label(ventana,text="Contraseña: ").place(x=10,y=60)
password_caja = Entry(ventana,textvariable=password).place(x=120,y=60)
etiqueta3 = Label(ventana,text="Destinatario: ").place(x=10,y=110)
destinatario_caja = Entry(ventana,textvariable=destinatario).place(x=120,y=110)
etiqueta4 = Label(ventana,text="Asunto: ").place(x=10,y=160)
asunto_caja = Entry(ventana,textvariable=asunto).place(x=120,y=160)
etiqueta5 = Label(ventana,text="Mensaje: ").place(x=10,y=210)
mensaje_caja = Entry(ventana,textvariable=mensaje).place(x=120,y=210)
etiqueta6 = Label(ventana,text="Adjuntar archivo: ").place(x=10,y=260)
archivo_caja = Entry(ventana,textvariable=archivo).place(x=120,y=260)

boton = Button(ventana,text='Enviar',command=enviar).place(x=10,y=310)
mensaje = MIMEText(mensaje, 'html')

ventana.mainloop()			
