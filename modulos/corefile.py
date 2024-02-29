import json 
import os
BASE="data/"
def checkFile(archivo:str,data):
    if(os.path.isfile(BASE+ archivo)):
        with open(BASE + archivo ,"r") as bw:
            data = json.load(bw)
            return data
    else:
        with open(BASE+archivo ,"w") as bw:
            json.dump(data,bw,indent=4)
            return data

        
def UpdateFile(archivo,data):
    with open(BASE+ archivo,'r+') as fw:
        json.dump(data,fw,indent=4)
        fw.truncate()
        
        
def delOp(dataInventario,opcion):
    if dataInventario[opcion]:
        os.system('cls')
        if opcion == 'activo':
            delVal = input("Ingrese el Codigo de campus del Activo que quiere borrar <-> ")
        elif opcion == 'personal':
            delVal = input("Ingrese el Nro de Identificacion de la Persona que quiere borrar <-> ")
        elif opcion == 'zonas':
            delVal = input("Ingrese el Nro de Identificacion de la Zona que quiere borrar <-> ")

        if delVal not in dataInventario[opcion].items():
            print('El codigo ingresado no esta registrado...')
            os.system('pause')
            delOp()
        dataInventario[opcion].pop(delVal)
        UpdateFile('inventario.json',dataInventario)
        print('Ha sido eliminado correctamente')
        os.system('pause')
    else:
        print(f'No has ingresado algun {opcion}...')
        os.system('pause')
    

def Search(inventario: dict, opcion: str): 
    if inventario[opcion]:
        isValueTrue = True
        while isValueTrue:
            codCampus = str(input(')_'))
            for idx, (key, value) in enumerate(inventario[opcion].items()): #Itera sobre el diccionario seleccionado y idx imprime un mensaje de error
                if opcion == 'activos':
                    if value['CodCampus'] == codCampus:
                        return key
                    elif len(inventario[opcion])-1 == idx:
                        print('nombre no encontrado, ingreselo de nuevo')
                        os.system('pause')
                elif opcion == 'Peronas':
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
                    if value['NroAsig'] == codCampus:
                        return key
                    elif len(inventario[opcion])-1 == idx:
                        print('Nro de Asignacion no encontrado, ingreselo de nuevo')
                        os.system('pause')
    else:
        print('no has ingresado ningun activo')
        os.system('pause')
        return