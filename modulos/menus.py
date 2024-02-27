import os
from tabulate import tabulate
def menuPrincipal():
    opciones = ["1","2","3","4","5","6","7"]
    menu =[["1.", "ACTIVOS"], ["2.", "PERSONAL"], ["3.", "ZONAS"], ["4.", "ASIGNACION DE ACTIVOS"], ["5.", "REPORTES"], ["7.", "MOVIMIENTO DE ACTIVOS"], ["4.", "SALIR"]]
    print(tabulate(menu, tablefmt="grid"))
    opcion = input("Seleccione una opcion : ")
    if opcion not in opciones:
        print('Ingresaste una opciones invalida')
        os.system('pause')
        menuPrincipal()
    else:
        return opcion
    
