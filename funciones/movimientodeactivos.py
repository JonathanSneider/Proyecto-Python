import os
import modulos.corefile as cf

def retornodeactivos(inventario):
    os.system('cls')
    print('Ingrese el codigo de campus del activo que sea retornar')
    codCampus = cf.Search(inventario, 'Activos')
    atajo = inventario['Activos'][codCampus]
    if atajo['Estado'] == "Asignado" or atajo['Estado'] == "No Asignado" or atajo['Estado'] == "Dado de Baja":
        print('Este activo no se puede retornar')
        os.system('pause')
        return
    else:
        pass
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
    tipoMov = "Retorno Activo"
    isrunis = True
    while isrunis:
        idperasig = input('Ingrese el id de la persona la cual esta realizando la asignacion : ')
        if idperasig not in inventario['Personas']:
            print('Ingerse un id valido')
            os.system('pause')
            continue
        else:
            isrunis = False
    
    nrohistorial = str(len(inventario['Activos'][codCampus]['historialActivo'])+1).zfill(3)
    historialactivos = {
        "NroID":nrohistorial,
        "Fecha":fecha,
        "tipoMov":tipoMov,
        "idRespMov":idperasig
    }
    inventario['Activos'][codCampus]['historialActivo'].update({nrohistorial:historialactivos})
    comparacion = int(len(atajo['historialActivo']))
    if comparacion < 0:        
        atajo['Estado']= "No asignado"
    else:
        atajo['Estado']= "Asigando"
    
    cf.UpdateFile('data.json',inventario)

def dardebajAc(inventario:dict):
    os.system('cls')
    print('Ingrese el codigo de campus del activo que desea dar de baja')
    codCampus = cf.Search(inventario, 'Activos')
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
    tipoMov = "Dado de Baja"
    isrunis = True
    while isrunis:
        idperasig = input('Ingrese el id de la persona la cual esta realizando la asignacion : ')
        if idperasig not in inventario['Personas']:
            print('Ingerse un id valido')
            os.system('pause')
            continue
        else:
            isrunis = False
    
    nrohistorial = str(len(inventario['Activos'][codCampus]['historialActivo'])+1).zfill(3)
    historialactivos = {
        "NroID":nrohistorial,
        "Fecha":fecha,
        "tipoMov":tipoMov,
        "idRespMov":idperasig
    }
    inventario['Activos'][codCampus]['historialActivo'].update({nrohistorial:historialactivos})
    atajo = inventario['Activos'][codCampus]
    atajo['Estado']= "Dado de Baja"
    cf.UpdateFile('data.json',inventario)
    
def garantiact(inventario:dict):
    os.system('cls')
    print('Ingrese el codigo de campus del activo que desea dar en garantia')
    codCampus = cf.Search(inventario, 'Activos')
    atajo = inventario['Activos'][codCampus]
    if atajo['Estado'] == "Dado de Baja":
        print('no se puede dar en garantia este activo')
        os.system('pause')
        return
    else:
        pass
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
    tipoMov = "Garantia"
    isrunis = True
    while isrunis:
        idperasig = input('Ingrese el id de la persona la cual esta realizando la asignacion : ')
        if idperasig not in inventario['Personas']:
            print('Ingerse un id valido')
            os.system('pause')
            continue
        else:
            isrunis = False
    
    Nrohistorial = str(len(inventario['Activos'][codCampus]['historialActivo'])+1).zfill(3)
    historialactivos = {
        "NroID":Nrohistorial,
        "Fecha":fecha,
        "tipoMov":tipoMov,
        "idRespMov":idperasig
    }
    inventario['Activos'][codCampus]['historialActivo'].update({Nrohistorial:historialactivos})
    atajo['Estado']= "En Garantia"
    cf.UpdateFile('data.json',inventario)
    
