from datetime import datetime
import time
import re
class Correo_electronico:
    def __init__(self, hora_actual):
        self.hora_actual = hora_actual
    def comprobar_hora():
        hora_actual=str(datetime.now().time())
        if hora_actual > "08:00:00.000000" and hora_actual < "12:00:00.000000":
            print("Buenos días:\n Introduzca un usuario y un correo eléctronico para acceder:")
            time.sleep(1)
        elif hora_actual > "12:00:00.000000" and hora_actual < "21:00:00.000000":
            print("Buenas tardes:\n Introduzca un usuario y un correo eléctronico para acceder:")
            time.sleep(1)
        else:
            print("Buenas noches:\nIntroduzca un usuario y un correo eléctronico para acceder:")
            time.sleep(1)
    def usuario():
        s=str(input("Usuario:\n"))
        comprobacion = re.search(". * @. * \ .. *", s)
        if comprobacion == True:
            print("¡Bienvenido {s}!")
        elif comprobacion == None:
            print("Lo sentimos, el correo electrónico es erróneo.")
            Correo_electronico.usuario()
        else:
            pass


Correo_electronico.comprobar_hora()
Correo_electronico.usuario()