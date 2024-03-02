import os
import modulos.corefile as ccf
from tabulate import tabulate

def agregarzonas(inventario:dict):
    os.system('cls')
    try:
        NroZona = int(input('Ingrese el numero de identificacion de la zona : '))
    except ValueError:
        print('Ingrese un numero de ifentificacion valido')
        os.system('pause')
        return
    else:
        if (NroZona < 0):
            print('Ingrese un numero de identificacion valido')
            os.system('pause')
            return
        else:
            pass
    if NroZona in inventario['Zonas']:
        print('El numero de identificacion de la zona que ingresaste ya esta registrado')
        os.system('pause')
        return
    else:
        pass
    NroZona = str(NroZona)
    NombreZona = input('Ingrese el nombre de la zona : ')
    try:
        totalcapacidad = int(input('Ingrese la capacidad total : '))
    except ValueError:
        print('Ingresaste un valor invalido')
        os.system('pause')
        return
    else:
        if (totalcapacidad < 0):
            print('Ingrese un valor valido')
            os.system('pause')
            return
        pass
    zonaa = {
        "NroZona":NroZona,
        "NombreZona":NombreZona,
        "TotalCapacidad":totalcapacidad
    }
    inventario['Zonas'].update({NroZona:zonaa})
    ccf.UpdateFile('data.json',inventario)
    
def actualizarzonas(invetario:dict):
    os.system('cls')
    print('Ingrese el numero de zona que desee actualizar')
    codCampus = ccf.Search(invetario, 'Zonas')
    atajo = invetario['Zonas'][codCampus]
    opciones = ['1','2']
    print('1. Nombre de la zona\n2. Total Capacidad')
    op = input('Seleccione una opcion : ')
    if op not in opciones:
        print('Ingresaste una opcion no valida')
        os.system('pause')
        return
    else:
        pass
    if op == '1':
        valorN = input('Ingrese el nuevo nombre de la zona : ')
        atajo['NombreZona']=valorN
        ccf.UpdateFile('data.json', invetario)
    if op == '2':
        try:
            valorN = int(input('Ingrese el nuevo valor : '))
        except ValueError:
            print('Ingrese un valor valido')
            os.system('pause')
            return
        else:
            if (valorN < 0):
                print('Ingrese un valor valido')
                os.system('pause')
                return
            else:
                pass
        atajo['TotalCapacidad'] = valorN
        ccf.UpdateFile('data.json', invetario)
        
def eliminarzona(inventario:dict):
    ccf.delOp(inventario, 'Zonas')
    
def buscarzona(inventario:dict):
    os.system('cls')
    
    print('Ingrese el Numero  de la zona que desea buscar')
    resultado = ccf.Search(inventario, 'Zonas')
    diccionario = inventario['Zonas'][resultado]
    lista = [(key, value)for key, value in diccionario.items()]
    print(tabulate(lista, tablefmt="grid"))
    os.system('pause')
    