
def eleccion_ejercicio():
    variable = int(input("Seleccione que ejercicio desea ejecutar: \n -->1: Web"))
    if variable == 1:
        from Clases import Web
    else:
        eleccion_ejercicio()

eleccion_ejercicio()