# Importar módulos
import time
import requests
import csv
import os
import subprocess
import gi
from bs4 import BeautifulSoup
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def progama ():

# Dirección de la página web
   url = "https://packetstormsecurity.com/news/"

# Ejecutar GET-Request
   response = requests.get(url)

# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
   html = BeautifulSoup(response.text, 'html.parser')

#   etq1= "dl"
#   CLASS="news"

# Extraer todas las NOTICIAS TITULARES y LINK Y FILTRAR
#   quotes_html = html.find_all('dl', class_="news")
# USANDO VARIABLES EN TAGS
   quotes_html = html.find_all(etq1, class_=CLASS)

# Crear una lista de las NOTICIAS
   quotes = list()
   for quote in quotes_html:
       quotes.append(quote.text)


# Guardar las NOTICIAS EN FICHERO CSV
# Abrir el archivo con Excel / LibreOffice, etc.
   with open('./packetstorm.csv', 'w', newline='') as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerows(zip(quotes))


#   LEO archivo NOTICIAS.CSV  y lo visualizo en notify
   with open('./packetstorm.csv', newline='') as csvfile:
       spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
       os.system ("clear")

       for row in spamreader:
            os.system ("clear")
            Notify.init("NOTICIAS:")
            Hello = Notify.Notification.new (', '.join(row) + "fuente:PacketStorm") 
            Hello.show()
            time.sleep(5)

# PROGRAMA MAIN PRINCIPAL QUE LLAMA A LA FUNCION
# Se llamara a si misma Buscara noticias visualizara todas las noticias
# La funcion reconectara de nuevo pasadas 15min

x = 1
while (x >= 1):
   Notify.init("NOTICIAS:")
   Hello = Notify.Notification.new ("Reconectando a Noticias....")
   Hello.show()

   etq1= "dl"
   CLASS="news"
   progama ()
   time.sleep(900)
   
