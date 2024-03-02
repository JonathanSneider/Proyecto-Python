import os
import modulos.corefile as cf

def añadirasignacion(inventario):
    os.system('cls')
    try:
        NroAsignacion = int(input('Ingrese el numero de asignacion : '))
    except ValueError:
        print('Ingrese un valor valido')
        os.system('pause')
        return
    else:
        if NroAsignacion in inventario['Asignaciones']:
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
        if((NroAsignacion > 31) or (NroAsignacion < 0)):
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
    print('1. Personal\n3. Zona')
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
    isrunasg = True
    while isrunasg:
        Activos = input('Ingrese el codigo de campus del activo el cual deseas asignar : ')
        if Activos not in inventario['Activos']:
            print('El codigo de campus que ingresaste no se encuentra registrado en activos')
            os.system('pause')
            continue
        
        #INCOMPLETOOOOOOOO
        
        elif inventario['Activos'][Activos]['Estado'] == "":
            pass
    
    
    
    