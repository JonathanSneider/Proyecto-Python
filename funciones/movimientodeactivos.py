import os
import modulos.corefile as cf

def retornodeactivos(inventario):
    os.system('cls')
    print('Ingrese el codigo de campus del activo que sea retornar')
    codCampus = cf.Search(inventario, 'Activos')
    atajo = inventario['Activos'][codCampus]
    if atajo['estado'] == "Asignado" or atajo['estado'] == "No Asignado" or atajo['estado'] == "Dado de Baja":
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
    atajo['estado']= "No asignado"
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
    atajo['estado']= "Dado de Baja"
    cf.UpdateFile('data.json',inventario)
    
def garantiact(inventario:dict):
    os.system('cls')
    print('Ingrese el codigo de campus del activo que desea dar en garantia')
    codCampus = cf.Search(inventario, 'Activos')
    atajo = inventario['Activos'][codCampus]
    if atajo['estado'] == "Dado de Baja":
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
    atajo['estado']= "En Garantia"
    cf.UpdateFile('data.json',inventario)
    
def cambiarasignacion(inventario:dict):
    print('Ingrese el codigo de campus del activo el cual desea reasignar')
    valor = cf.Search(inventario, 'Activos')
    valors = []
    valors.append(valor)
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
    tipoMov = "ReAsigancion"
    isrunis = True
    while isrunis:
        idperasig = input('Ingrese el id de la persona la cual esta realizando la asignacion : ')
        if idperasig not in inventario['Personas']:
            print('Ingerse un id valido')
            os.system('pause')
            continue
        else:
            isrunis = False
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
    AsigandoA = input(f'Ingrese el id de la {TipoAsignacion} a la cual le asiganara el activo : ')
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
    asignacion = {
        "NroAsignacion":NroAsignacion,
        "FechaAsignacion":fecha,
        "TipoAsignacion":TipoAsignacion,
        "AsignadoA":AsigandoA,
        "Activos":valors
        
    }
    nrohistorial = str(len(inventario['Activos'][valor]['historialActivo'])+1).zfill(3)
    historialactivos = {
        "NroID":nrohistorial,
        "Fecha":fecha,
        "tipoMov":tipoMov,
        "idRespMov":idperasig
    }
    valorr = 0
    for key,value in inventario['Asignacion'].items():
        if valor in value['Activos']:
            for keyy,value in enumerate(value['Activos']):
                if valor == value:
                    valorr = keyy
            try:
                del inventario['Asignacion'][key]['Activos'][valorr]
            except TypeError:
                print(f'No se puede asiganar este activo a la {TipoAsignacion}')
                os.system('pause')
                return
            break
        else:
            pass
    inventario['Activos'][valor]['historialActivo'].update({nrohistorial:historialactivos})
    inventario['Activos'][valor]['estado'] = "Asigando"
    inventario['Asignacion'].update({NroAsignacion:asignacion})
    cf.UpdateFile('data.json',inventario)
    
    
