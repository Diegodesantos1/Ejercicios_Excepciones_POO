from datetime import datetime
import time
import re
class Correo_electronico:
    def __init__(self, hora_actual):
        self.hora_actual = hora_actual
    def comprobar_hora():
        hora_actual=str(datetime.now().time())
        if hora_actual > "08:00:00.000000" and hora_actual < "12:00:00.000000":
            print("Buenos días:\nIntroduzca un correo electrónico para acceder:")
            time.sleep(1)
        elif hora_actual > "12:00:00.000000" and hora_actual < "21:00:00.000000":
            print("Buenas tardes:\nIntroduzca un correo electrónico para acceder:")
            time.sleep(1)
        else:
            print("Buenas noches:\nIntroduzca un correo electrónico para acceder:")
            time.sleep(1)
    def usuario():
        s=str(input("Usuario:\n"))
        usuario = re.findall(r"^\w+",s)
        print(usuario)

Correo_electronico.comprobar_hora()
Correo_electronico.usuario()