import os
from tabulate import tabulate
def menuPrincipal():
    os.system('cls')
    titulo = """
    -----------------------------------------
    * SISTEMA G&C DE INVENTARIO CAMPUSLANDS *
    -----------------------------------------
    """
    print(titulo)
    opciones = ["1","2","3","4","5","6","7"]
    menu =[["1.", "ACTIVOS"], ["2.", "PERSONAL"], ["3.", "ZONAS"], ["4.", "ASIGNACION DE ACTIVOS"], ["5.", "REPORTES"], ["6.", "MOVIMIENTO DE ACTIVOS"], ["7.", "SALIR"]]
    print(tabulate(menu, tablefmt="grid"))
    opcion = input("Seleccione una opcion : ")
    if opcion not in opciones:
        print('Ingresaste una opciones invalida')
        os.system('pause')
        os.system('cls')
        menuPrincipal()
    else:
        return opcion
    
    
def menuAct():
    os.system('cls')
    titulo = """
        //////////////////
        -  MENU ACTIVOS  -
        //////////////////
        """
    print(titulo)
    opciones = ["1","2","3","4","5"]
    menu =[["1.", "AGREGAR ACTIVO"], ["2.", "EDITAR ACTIVO"], ["3.", "ELIMINAR ACTIVO"], ["4.", "BUSCAR ACTIVO"], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(menu, tablefmt="grid"))
    opcion = input("Seleccione una opcion : ")
    if opcion not in opciones:
        print('Ingresaste una opciones invalida')
        os.system('pause')
        menuAct()
    else:
        return opcion
def menuPer():
    os.system('cls')
    titulo2 = """
        //////////////////
        - MENU PERSONAL -
        //////////////////
    """
    print(titulo2)
    opciones = ["1","2","3","4","5"]
    menu =[["1.", "AGREGAR PERSONAL"], ["2.", "EDITAR PERSONAL"], ["3.", "ELIMINAR PERSONAL"], ["4.", "BUSCAR PERSONAL"], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(menu, tablefmt="grid"))
    opcion = input("Seleccione una opcion : ")
    if opcion not in opciones:
        print('Ingresaste una opciones invalida')
        os.system('pause')
        menuPer()
    else:
        return opcion
def menuZon():
    os.system('cls')
    titulo3 = """
        //////////////////
        -   MENU ZONAS   -
        //////////////////
        """
    print(titulo3)
    opciones = ["1","2","3","4","5"]
    menu =[["1.", "AGREGAR ZONA"], ["2.", "EDITAR ZONA"], ["3.", "ELIMINAR ZONA"], ["4.", "BUSCAR ZONA"], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(menu, tablefmt="grid"))
    opcion = input("Seleccione una opcion : ")
    if opcion not in opciones:
        print('Ingresaste una opciones invalida')
        os.system('pause')
        menuZon()
    else:
        return opcion
    
def menuAsignacionA():
    os.system('cls')
    titulo4 = """
        ++++++++++++++++++++++++++++++++
        -  MENU ASIGNACION DE ACTIVOS  -
        ++++++++++++++++++++++++++++++++
        """
    print(titulo4)
    opciones = ["1","2","3"]
    menu =[["1.", "CREAR ASIGNACION"], ["2.", "BUSCAR ASIGNACION"], ["3.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(menu, tablefmt="grid"))
    opcion = input("Seleccione una opcion : ")
    if opcion not in opciones:
        print('Ingresaste una opciones invalida')
        os.system('pause')
        os.system('cls')
        menuAsignacionA()
    else:
        return opcion
    
def menuReportes():
    os.system('cls')
    titulo4 = """
        *+++++++++++++++++*
        /  MENU REPORTES  /
        *+++++++++++++++++*
        """
    print(titulo4)
    opciones = ["1","2","3","4","5","6"]
    menu =[["1.", "LISTAR TODOS LOS ACTIVOS"], ["2.", "LISTAR ACTIVOS POR CATEGORIA"], ["3.", "LISTAR ACTIVOS DADOS DE BAJA POR DAÑO"], ["4.", "LISTAR ACTIVOS Y ASIGNACION"], ["5.", "LISTAR HISTORIAL DE MOV. DE ACTIVO"], ["6.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(menu, tablefmt="grid"))
    opcion = input("Seleccione una opcion : ")
    if opcion not in opciones:
        print('Ingresaste una opciones invalida')
        os.system('pause')
        os.system('cls')
        menuReportes()
    else:
        return opcion
    
    
    
def menuMAct():
    os.system('cls')
    titulo4 = """
        --------------------------------
        /  MENU MOVIMIENTO DE ACTIVOS  /
        --------------------------------
        """
    print(titulo4)
    opciones = ["1","2","3","4","5"]
    menu =[["1.", "RETORNO DE ACTIVO"], ["2.", "DAR DE BAJA ACTIVO"], ["3.", "CAMBIAR ASIGNACION DE ACTIVO"], ["4.", "ENVIAR A GARANTIA ACTIVO"], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
    print(tabulate(menu, tablefmt="grid"))
    opcion = input("Seleccione una opcion : ")
    if opcion not in opciones:
        print('Ingresaste una opciones invalida')
        os.system('pause')
        os.system('cls')
        menuMAct()
    else:
        return opcion