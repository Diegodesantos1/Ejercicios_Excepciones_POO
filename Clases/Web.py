from datetime import datetime

class Correo_electronico:
    def __init__(self, hora_actual):
        self.hora_actual = hora_actual
    def comprobar_hora():
        hora_actual=str(datetime.now().time())
        if hora_actual > "08:00:00.000000" and hora_actual < "12:00:00.000000":
            print("Buenos días:\n Introduzca un usuario y un correo eléctronico para acceder:\n")
        elif hora_actual > "12:00:00.000000" and hora_actual < "21:00:00.000000":
            print("Buenas tardes:\n Introduzca un usuario y un correo eléctronico para acceder:\n")
        else:
            print("Buenas noches:\n Introduzca un usuario y un correo eléctronico para acceder:\n")
Correo_electronico.comprobar_hora()