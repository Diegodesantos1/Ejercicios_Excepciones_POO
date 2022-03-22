from datetime import datetime
import time
import re
class Correo_electronico:
    def __init__(self, hora_actual):
        self.hora_actual = hora_actual
    def comprobar_hora():
        hora_actual=str(datetime.now().time())
        if hora_actual > "08:00:00.000000" and hora_actual < "12:00:00.000000":
            print("Buenos días:\n")
            time.sleep(1)
        elif hora_actual > "12:00:00.000000" and hora_actual < "21:00:00.000000":
            print("Buenas tardes:\n")
            time.sleep(1)
        else:
            print("Buenas noches:\n")
            time.sleep(1)
    def usuario():
        correo_electronico = str(input("Introduzca su correo electrónico:\n"))
        comprobacion=re.search("@......", correo_electronico)
        if comprobacion == None:
            print("Correo no válido, mantenga el formato xxx@xxx.xx\n")
            Correo_electronico.usuario()
        else:
            usuario = re.sub("@gmail.com.es.orgyahoohotmail!","",correo_electronico)
            print(f"Bienvenido {usuario}")


Correo_electronico.comprobar_hora()
Correo_electronico.usuario()