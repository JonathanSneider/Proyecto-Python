import json 
import os
BASE="data/"

#verifica si el json data existe y si no lo crea
def checkFile(archivo:str,data):
    if(os.path.isfile(BASE+ archivo)):
        with open(BASE + archivo ,"r") as bw:
            data = json.load(bw)
            return data
    else:
        with open(BASE+archivo ,"w") as bw:
            json.dump(data,bw,indent=4)
            return data


#Actualizar cualquier informacion      
def UpdateFile(archivo,data):
    with open(BASE+ archivo,'r+') as fw:
        json.dump(data,fw,indent=4)
        fw.truncate()
        

#eliminando algun valor
def delOp(dataInventario,opcion):
    os.system('cls')
    if opcion == 'Activos':
        delVal = input("Ingrese el Codigo de campus del Activo que quiere eliminar : ")
    elif opcion == 'Personas':
        delVal = input("Ingrese el Nro de Identificacion de la Persona que quiere eliminar : ")
    elif opcion == 'Zonas':
        delVal = input("Ingrese el Nro de Identificacion de la Zona que quiere eliminar : ")

    if delVal not in dataInventario[opcion].keys():
        print('El codigo ingresado no esta registrado')
        os.system('pause')
        return
    if opcion == "Activos":
        if dataInventario[opcion][delVal]['estado'] == "Asignado":
            print('El activo ingresado no se puede eliminar')
            os.system('pause')
            return
        else:
            pass
    else:
        pass
    if opcion == "Personas":
        for key,value in dataInventario['Asignacion'].items():
            if dataInventario['Asignacion'][key]['AsignadoA'] == delVal:
                print("No se puede eliminar esta persona")
                os.system('pause')
                return
    else:
        pass
    dataInventario[opcion].pop(delVal)
    UpdateFile('data.json',dataInventario)
    os.system('pause')
    

def Search(inventario: dict, opcion: str): 
    if inventario[opcion]:
        isValueTrue = True
        while isValueTrue:
            codCampus = str(input(')_ : '))
            for idx, (key, value) in enumerate(inventario[opcion].items()):
                if opcion == 'Activos':
                    if value['codCampus'] == codCampus:
                        return key
                    elif len(inventario[opcion])-1 == idx:
                        print('id no encontrado, ingreselo de nuevo')
                        os.system('pause')
                elif opcion == 'Personas':
                    if value['id'] == codCampus:
                        return key
                    elif len(inventario[opcion])-1 == idx:
                        print('Id no encontrado, ingreselo de nuevo')
                        os.system('pause')
                elif opcion == 'Zonas':
                    if value['NroZona'] == codCampus:
                        return key
                    elif len(inventario[opcion])-1 == idx:
                        print('Nro de Zona no encontrado, ingreselo de nuevo')
                        os.system('pause')
                elif opcion == 'Asignacion':
                    if value['NroAsignacion'] == codCampus:
                        return key
                    elif len(inventario[opcion])-1 == idx:
                        print('Nro de Asignacion no encontrado, ingreselo de nuevo')
                        os.system('pause')
    else:
        print('no has ingresado ningun activo')
        os.system('pause')
        return
    
    
