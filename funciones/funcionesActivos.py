import os
import modulos.corefile as cf 
from tabulate import tabulate
dataactivos = {}
marca = ['LG','COMPUMAX','LOGITECH','BENQ','ASUS','LENOVO','HP']
categoria = ['EQUIPO DE COMPUTO','ELECTRODOMESTICO','JUEGO']
tipo = ['MONITOR','CPU','TECLADO','MOUSE','AIRE ACONDICIONADO','PORTATIL','IMPRESORA']
def VRF(valor,el : str,valorr : str):
    os.system('cls')
    runVRF = True
    while runVRF:
        os.system('cls')
        if valor == marca:
            menu =[["LG"], ["COMPUMAX"], ["LOGITECH"], ["BENQ"], ["ASUS"], ["LENOVO"], ["HP"]]
            print(tabulate(menu, tablefmt="grid"))
        elif valor == categoria:
            menu =[["Equipo de computo"], ["Electrodomestico"], ["Juego"]]
            print(tabulate(menu, tablefmt="grid"))
        elif valor == tipo:
            menu =[["MONITOR"], ["CPU"], ["TECLADO"], ["MOUSE"], ["AIRE ACONDICIONADO"], ["PORTATIL"], ["IMPRESORA"]]
            print(tabulate(menu, tablefmt="grid"))
        op = input(f'Ingrese {el} {valorr} del activo : ').upper()
        if op not in valor:
            print('Ingresaste un dato invalido')
            os.system('pause')
            continue
        else:
            return op
            
            
    
def Addactivos(activosdata: dict):
    os.system('cls')
    CodTransaccion = input('Ingrese el codigo de transaccion : ')
    NroFormulario = input('ingrese el numero de formulario : ')
    CodCampus = input('Ingrese el Codigo de campus : ')
    marcaa = VRF(marca,"la","marca")
    categoriaa = VRF(categoria,"la","categoria")
    if categoriaa == "JUEGO":
        tipoo = ""
    else:
        tipoo = VRF(tipo,"el","tipo")
    isrunVlr = True
    while isrunVlr:
        try:
            VlrUnitario = float(input('Ingrese el valor unitario : '))
        except ValueError:
            print('Ingrese un numero valido')
            os.system('pause')
        else:
            isrunVlr = False
    Proveedor = input('Ingrese el proveedor del activo : ')
    NroSerial = input('Ingrese el codigo serial : ')
    Empresaresponsable = input('Ingrese la Empresa responsable del activo : ')
    Estado = 'No Asignado'
    Activo ={
        
        "CodTransaccion":CodTransaccion,
        "NroFormulario":NroFormulario,
        "CodCampus":CodCampus,
        "Marca":marcaa,
        "Categoria":categoriaa,
        "Tipo":tipoo,
        "VlrUnitario":VlrUnitario,
        "Proveedor":Proveedor,
        "NroSerial":NroSerial,
        "Empresaresponsable":Empresaresponsable,
        "Estado":Estado,
        "HistorialActivo":{
            'Nrold':"",
            'Fecha':"",
            'tipoMov':"",
            'idRespMov':""
            
        }
    }
    activosdata['Activos'].update({CodCampus:Activo})
    cf.createData('data.json',activosdata)
    
def updateActivos(activosdata:dict):
    os.system('cls')
    Id = input('Ingrese el codigo del activo : ')
    for key in activosdata['Activos'].keys():
        if Id not in activosdata['Activos']:
            print('El codigo no se encuentra registrado')
            os.system('pause')
            break
    else:
        for key,value in activosdata['Activos'][Id].keys():
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                os.system('cls')
                activosdata['Activos'][key] = input(f'Ingrese el nuevo valor para {key} :')
                activosdata['Activos'][Id][key].update({activosdata['Activos'][Id][key]:activosdata['Activos'][Id]})
                cf.UpdateFile('inventario.json',activosdata)
        
    
        
    