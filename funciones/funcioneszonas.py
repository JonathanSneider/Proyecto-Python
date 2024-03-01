import os
import modulos.corefile as ccf

def agregarzonas(inventario:dict):
    os.system('cls')
    NroZona = str(len(inventario['Zonas'])+1).zfill(2)
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
    inventario['Zonas'].update({NroZona:zonaa})
    ccf.UpdateFile('data.json',inventario)