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
        
        
def delData(data):
    delVal = input("Ingrese el Nit del proveedor que desea borrar -> ")
    data['proveedores'].pop(delVal)
    UpdateFile('inventario.json',data)
    
def search(data):
    valor = input("Ingrese el Nit del proveedor a buscar -> ")
    result= data['proveedores'].get(valor)
    nit,nombrePro,tipo,direccion = result.values()
    ciudad,ubicacion,longitud,latitud = direccion.values()
    print(f'Nit {nit}:')
    os.system('pause')