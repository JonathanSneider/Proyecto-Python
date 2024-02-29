import os
import modulos.corefile as cf

def agregarzonas(inventario:dict):
    os.system('cls')
    NroZona = input('Ingrese el numero de la zona : ')
    NombreZona = input('Ingrese el nombre de la zona : ')
    try:
        totalcapacidad = int(input('Ingrese la capacidad total : '))
    except ValueError:
        print('Ingresaste un valor invalido')
        os.system('pause')
        return
    else:
        pass
    zonaa = {
        "NroZona":NroZona,
        "NombreZona":NombreZona,
        "TotalCapacidad":totalcapacidad
    }
    inventario['Zonas'].update({})