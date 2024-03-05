import os
import modulos.corefile as cf
from tabulate import tabulate
def añadirasignacion(inventario):
    contador = 0
    activoss = []
    os.system('cls')
    try:
        NroAsignacion = int(input('Ingrese el numero de asignacion : '))
    except ValueError:
        print('Ingrese un valor valido')
        os.system('pause')
        return
    else:
        NroAsignacion = str(NroAsignacion)
        if NroAsignacion in inventario['Asignacion']:
            print('El numero de asignacion ya se encuentra registrado')
            os.system('pause')
            return
    try:
        dia = int(input('ingrese el dia de asignacion : '))
    except ValueError:
        print('Ingrese un dia valido')
        os.system('pause')
        return
    else:
        if((dia > 31) or (dia < 0)):
            print('Ingrese un dia valido')
            os.system('pause')
            return
        pass
    try:
        mes = int(input('Ingrese el mes de asignacion : '))
    except ValueError:
        print('Ingrese un mes valido')
        os.system('pause')
        return
    else:
        if((mes > 12) or (mes < 0)):
            print('Ingrese un mes valido')
            os.system('pause')
            return
        pass
    try:
        año = int(input('Ingrese el año de asignacion : '))
    except ValueError:
        print('Ingrese un año valido')
        os.system('pause')
        return
    else:
        if((año > 2100) or (año < 2000)):
            print('Ingrese un año valido')
            os.system('pause')
            return
        pass
    fecha = (f"{dia}/{mes}/{año}")
    opciones = ['1','2']
    print('1. Personal\n2. Zona')
    op = input('Seleccione el tipo de asignacion : ')
    if op not in opciones:
        print('Ingrese una opciones valida')
        os.system('pause')
        return
    elif op == '1':
        TipoAsignacion = "Persona"
    elif op == '2':
        TipoAsignacion = "Zona" 
        
    AsigandoA = input(f'Ingrese el id de la {TipoAsignacion} que desee asignarle activos : ')
    if TipoAsignacion == "Persona":
        if AsigandoA not in inventario['Personas']:
            print('Ingrese un id valido')
            os.system('pause')
            return
        else:
            pass
    elif TipoAsignacion == "Zona":
        if AsigandoA not in inventario['Zonas']:
            print('Ingrese un id valido')
            os.system('pause')
            return
        else:
            pass
    for key, value in inventario['Asignacion'].items():
        if value["AsignadoA"] == AsigandoA:
            for values in enumerate(value['Activos']):
                contador += 1
        else:
            pass
                
    isrunasg = True
    while isrunasg:
        Activos = input('Ingrese el codigo de campus del activo el cual deseas asignar : ')
        
        if Activos not in inventario['Activos']:
            print('El codigo de campus que ingresaste no se encuentra registrado en activos')
            os.system('pause')
            continue
        
        elif (inventario['Activos'][Activos]['estado'] == "No Asignado"):
            activoss.append(Activos)
            contador += 1
            if TipoAsignacion == "Persona":
                pass
            elif contador == inventario['Zonas'][AsigandoA]['TotalCapacidad']:
                print('Se a superado la capicidad de la zona')
                os.system('pause')
                isrunasg = False
            rta12 = 'x'
            while (rta12 not in ['S','s','']):
                rta12 = input('Desea asiganar otro activo Si(S/s) Enter(No) :')
                isrunasg = bool(rta12)
        else:
            print('No se puede asignar este activo')
            os.system('pause')
            return
        
    
    isrunis = True
    while isrunis:
        idperasig = input('Ingrese el id de la persona la cual esta realizando la asignacion : ')
        if idperasig not in inventario['Personas']:
            print('Ingerse un id valido')
            os.system('pause')
            continue
        else:
            isrunis = False
    asignacion = {
        "NroAsignacion":NroAsignacion,
        "FechaAsignacion":fecha,
        "TipoAsignacion":TipoAsignacion,
        "AsignadoA":AsigandoA,
        "Activos":activoss
        
    }
    for value in activoss:
        nrohistorial = str(len(inventario['Activos'][value]['historialActivo'])+1).zfill(3)
        historialactivos = {
            "NroID":nrohistorial,
            "Fecha":fecha,
            "tipoMov":"Asignacion",
            "idRespMov":idperasig
        }
        inventario['Activos'][value]['historialActivo'].update({nrohistorial:historialactivos})
        inventario['Activos'][value]['estado'] = "Asignado"
        cf.UpdateFile('data.json',inventario)
    inventario['Asignacion'].update({NroAsignacion:asignacion})
    cf.UpdateFile('data.json',inventario)
            
        
    
    
    
def buscarasignacion(inventario):
    os.system('cls')
    print('Ingrese el numero de asignacion del cual desea ver')
    resultado = cf.Search(inventario, 'Asignacion')
    diccionario = inventario['Asignacion'][resultado]
    lista = [(key, value)for key,value in diccionario.items()]
    print(tabulate(lista, tablefmt="grid"))    
    os.system('pause')
    