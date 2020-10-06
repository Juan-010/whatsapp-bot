import os
import sys
from time import sleep
from openwa import WhatsAPIDriver
version = '1.0.1'
driver = WhatsAPIDriver(client='chrome')
#urls
iso = "https://us04web.zoom.us/j/74583065356?pwd=d2NCWTlCUWkwd0lESkNQb21OUmxxdz09"
sdr = "https://us04web.zoom.us/j/9384918712?pwd=YkJ5RGpqdkVrSGwzaUZ1a3VLSE1kZz09"
fisica_p = "https://utn.zoom.us/j/98019977484?pwd=a2JPeXE3QkJOeERWTTBwWitoTzBtUT09"
fisica_t = "https://us04web.zoom.us/j/8839114678?pwd=YUo3a0QzbnVod1Blb1JBMHg5Zk5Gdz09"
info_p = "https://us04web.zoom.us/j/76339887291?pwd=aGVHenBBRjQxbFl0bWRlbThNdGthQT09"
info_t = "https://meet.google.com/sau-znja-qzh"
am_p = "https://utn.zoom.us/j/96969003891?pwd=aW1FNGR6Yk1mVHBHNyswY3JnN1BIdz09"
am_t = "https://utn.zoom.us/j/92043173427?pwd=Zk1VeVQrOTV2UEVmVERjOHV1L0tHdz09"

def run():
    print("Tienes 15 segundos para escanear el codigo QR!")
    sleep(15)
    print("Bot iniciado!")
    driver.subscribe_new_messages(NewMessageObserver())
    while True:
        sleep(60)


class NewMessageObserver:

    def on_message_received(self, new_messages):
        for message in new_messages:
            if message.type == 'chat':
                msg = message.content.lower()
                if msg[0] == '/':
                    chat = driver.get_chat_from_id(message.chat_id)
                    if msg[1:] == 'version':
                        chat.send_message("Version: {}".format(version))

                    elif msg[1:] == 'help' or msg[1:] == 'h' or msg[1:] == '?':
                        chat.send_message("Hola! Por el momento solo estan los links de las clases de cada materia")
                    elif msg[1:] == 'sistemas' or msg[1:] == 'sdr':
                        chat.send_message("Sistemas de Representacion:")
                        chat.send_message("Zoom: " + sdr)
                        chat.send_message("Profesor: Jorge Mercado")
                        chat.send_message("Horario: Miercoles de 15:30 a 18:00, o 17:30, 0 17:00, depende del humor del profe")

                    elif msg[1:] == 'iso':
                        chat.send_message("Ingeniería y Sociedad:")
                        chat.send_message("Zoom: " + iso)
                        chat.send_message("Profesor: Renee Isabel Mengo")
                        chat.send_message("Horario: Martes de 11:30 a 12:30")


                    elif msg[1:] == 'am2' or msg[1:] == 'analisis': 
                        chat.send_message("Análisis Matemático 2 (Teórico):")
                        chat.send_message("Zoom: " + am_t)
                        chat.send_message("Profesor: Leonardo Giordano")
                        chat.send_message("Horario: Miercoles de 8:30 a 11:30")
                        chat.send_message("Análisis Matemático 2 (Práctico):")
                        chat.send_message("Zoom: " + am_p)
                        chat.send_message("Profesor: Luis Carlos Mazzucchelli")
                        chat.send_message("Horario: Viernes de 8 a 12:50. La mas larga")


                    elif msg[1:] == 'fisica' or msg[1:] == 'fisica1' :
                        chat.send_message("Física 1 (Teórico):")
                        chat.send_message("Zoom: " + fisica_t)
                        chat.send_message("Profesor: Julio César Catán (you know who)")
                        chat.send_message("Horario: Lunes de 9:40 a 12:50\n Jueves de 8 a 9:30")
                        chat.send_message("Análisis Matemático 2 (Práctico):")
                        chat.send_message("Zoom: " + fisica_p)
                        chat.send_message("Profesor: Gabriel Eduardo González")
                        chat.send_message("Horario: Martes de 8:15 a (supuestamente) 11. Termina 9:30/10 casi siempre")

                    elif msg[1:] == 'info' or msg[1:] == 'informatica' or  msg[1:] == 'info1' :
                        chat.send_message("Informática 1 (Teórico):")
                        chat.send_message("Meet: " + info_t)
                        chat.send_message("Profesor: Claudio J. Paz")
                        chat.send_message("Horario: Lunes de 8 a 9:30")
                        chat.send_message("Informática 1 (Práctico):")
                        chat.send_message("Zoom: " + info_p)
                        chat.send_message("Profesor: Norma Luz Mascietti")
                        chat.send_message("Horario: A esta altura, quien sabe. Sabados o Jueves de 11:00 a 12:30")

                    else:
                        chat.send_message("No conozco ese comando pa, pone /help para ver los comandos")

run()
