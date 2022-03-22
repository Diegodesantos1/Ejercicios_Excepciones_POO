from datetime import datetime
import time
import re
import colorama
from colorama import Fore
class Correo_electronico:
    def __init__(self, hora_actual):
        self.hora_actual = hora_actual
    def comprobar_hora():
        hora_actual=str(datetime.now().time())
        if hora_actual > "08:00:00.000000" and hora_actual < "12:00:00.000000":
            print("¡Buenos días!\nCargando página web...")
            time.sleep(1)
        elif hora_actual > "12:00:00.000000" and hora_actual < "21:00:00.000000":
            print("¡Buenas tardes!\nCargando página web...")
            time.sleep(1)
        else:
            print("¡Buenas noches!\nCargando página web...")
            time.sleep(1)
    def usuario(contador):
        if contador < 2:
            correo_electronico = str(input("Introduzca su correo electrónico:\n"))
            comprobacion=re.search("@......", correo_electronico)
            if comprobacion == None:
                print("Correo no válido, mantenga el formato xxx@xxx.xx\n")
                Correo_electronico.usuario(contador + 1)
            else:
                lista = correo_electronico.split("@")
                usuario = lista.pop(0)
                print(f"¡Bienvenido {usuario}!")
        else:
            print(Fore.RED + "Cuenta bloqueada a causa de un ataque\n")
            exit


Correo_electronico.comprobar_hora()
Correo_electronico.usuario(0)