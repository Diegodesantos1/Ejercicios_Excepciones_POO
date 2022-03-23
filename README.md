<h1 align="center">POO con archivos</h1>

*He usado la Programación Orientada a Objetos para resolver este ejercicio*

---

En este [repositorio](https://github.com/Diegodesantos1/Ejercicios_Excepciones_POO) queda resuelto el ejercicios de excepciones en Python. Para llevar a cabo el proyecto me hemos documentado a través de la teoría que se encuentra en el campus virtual y de otros medios.

***

## Índice
1. [Ejercicio 1: Excepciones correo  ](#id1)

***

## Ejercicio 1: Excepciones correo<a name="id1"></a>

Enunciado: escriba un programa que simule la conexión de un usuario a un sitio web para el que ya se ha registrado, solo con su dirección de correo electrónico (la gestión de una contraseña está fuera del alcance de esta sección). Este programa debe ofrecer la posibilidad al usuario de introducir una dirección de correo electrónico, y mostrará diferentes mensajes de error en función de la cadena introducida. El programa debe continuar si el correo electrónico indicado tiene un formato incorrecto y finalizar si no se reconoce el correo electrónico, ya que se podría tratar de un ciberataque. Importante: el método que analiza la cadena de caracteres no debe devolver ningún valor.

Requisitos previos:

Puede usar el módulo de expresiones regulares ofrecido por Python, para determinar si la cadena de caracteres tiene el formato correcto. Para hacerlo, importe el módulo "re" (import re) y utilice el método search() de la siguiente manera: re.search(". * @. * \ .. *", s). Esta línea devolverá None si la cadena s no tiene el formato de una dirección de correo electrónico.

El método input(’->’) le permite recopilar una cadena de caracteres escrita en la entrada estándar (la consola, en este caso).


```python
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
            comprobacion=(re.search(".*@.*\..*", correo_electronico))
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
```
Su UML es el siguiente:

![image](https://user-images.githubusercontent.com/91721855/159692536-197011bd-283b-4095-9e79-f33fcbb2f4ec.png)


En formato [XML](https://github.com/Diegodesantos1/Ejercicios_Excepciones_POO/blob/main/UML/Correo.drawio)
