import json 
import os
BASE="data/"
def checkFile(archivo:str,data):
    if(not(os.path.isfile(BASE+ archivo))):
        with open(BASE + archivo ,"w") as bw:
            json.dump(data,bw,indent=4)

def readDataFile(archivo):
    with open(BASE+archivo,"r+") as rf:
       return json.load(rf)
   
def createData(archivo,data):
    with open(BASE+archivo,"w+") as rwf:
        json.dump(data,rwf,indent=4)
        
def updateActivos(dataa,srcData):
    if (len(dataa) <=0):
        print('No se encuentra registrada informacion la cual actualizar')
        os.system('pause')
    else:
        activoup = input('Ingrese el activo el cual desea actualizar : ') 
        
        srcData['proveedores'].update({dataa['nit']:dataa})
        UpdateFile('inventario.json',srcData)
    os.system('pause')
    
def UpdateFile(archivo,data):
    with open(BASE+ archivo,'w') as fw:
        json.dump(data,fw,indent=4)
        
        
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