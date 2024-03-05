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
    if CodCampus in activosdata['Activos']:
        print('El codigo de campus que intentas registrar ya se encuentra registrado')
        os.system('pause')
        return
    else:
        pass
    marcaa = VRF(marca,"la","marca")
    categoriaa = VRF(categoria,"la","categoria")
    tipoo = VRF(tipo,"el","tipo")
    isrunVlr = True
    while isrunVlr:
        try:
            VlrUnitario = float(input('Ingrese el valor unitario : '))
        except ValueError:
            print('Ingrese un numero valido')
            os.system('pause')
        else:
            if (VlrUnitario < 0):
                print('Ingresa un numero valido')
                os.system('pause')
                continue
            else:
                pass
            isrunVlr = False

    Proveedor = input('Ingrese el proveedor del activo : ')
    NroSerial = input('Ingrese el codigo serial : ')
    Empresaresponsable = input('Ingrese la Empresa responsable del activo : ')
    Estado = 'No Asignado'
    Activo ={
        
        "codTransaccion":CodTransaccion,
        "nroFormulario":NroFormulario,
        "codCampus":CodCampus,
        "marca":marcaa,
        "categoria":categoriaa,
        "tipo":tipoo,
        "vlrUnitario":VlrUnitario,
        "proveedor":Proveedor,
        "nroSerial":NroSerial,
        "empresaresponsable":Empresaresponsable,
        "estado":Estado,
        "historialActivo":{}
    }
    activosdata['Activos'].update({CodCampus:Activo})
    cf.UpdateFile('data.json',activosdata)

def updateActivos(activosdata:dict):
    os.system('cls')
    print('Ingrese el Codigo de campus del activo que desea actualizar')
    codCampus = cf.Search(activosdata, 'Activos')
    atajo = activosdata['Activos'][codCampus]
    opciones = ['1','2','3','4','5','6','7','8','9']
    print('1. Codigo de Transaccion\n2. Numero de Formulario\n3. Marca\n4. Categoria\n5. Tipo\n6. Valor unitario\n7. Proveedor\n8. Numero de serial\n9. Empresa responsable')
    op = input('Seleccione una opciones : ')
    if op not in opciones:
        print('Ingresaste una opcion no valida')
        os.system('pause')
        return
    else:
        pass
    if op == '1':
        valorN = input('Ingrese el Nuevo codigo de transaccion : ')
        atajo['codTransaccion']= valorN
        cf.UpdateFile('data.json',activosdata)
    if op == '2':
        valorN = input('Ingrese el Nuevo Numero de formulario : ')
        atajo['nroFormulario']=valorN
        cf.UpdateFile('data.json',activosdata)
    if op == '3':
        valorN = VRF(marca,"la","marca")
        atajo['marca']=valorN
        cf.UpdateFile('data.json',activosdata)
    if op == '4':
        valorN = VRF(categoria,"la","categoria")
        atajo['categoria']=valorN
        cf.UpdateFile('data.json',activosdata)
    if op == '5':
        valorN = VRF(tipo,"el","tipo")
        atajo['tipo']=valorN
        cf.UpdateFile('data.json',activosdata)
    if op == '6':
        isrun6 = True
        while isrun6:
            try:
                valorN = int(input('Ingrese el nuevo valor unitario : '))
            except ValueError:
                print('Ingresaste un valor invalido')
                os.system('pause')
                continue
            else:
                if (valorN < 0):
                    print('Ingresa un numero valido')
                    os.system('pause')
                    continue
                else:
                    pass
                isrun6 = False
            
        atajo['vlrUnitario']=valorN
        cf.UpdateFile('data.json',activosdata)
    if op == '7':
        valorN = input('Ingrese el nuevo proveedor : ')
        atajo['proveedor']=valorN
        cf.UpdateFile('data.json',activosdata)
    if op == '8':
        valorN = input('Ingrese el nuevo numero serial : ')
        atajo['nroSerial']=valorN
        cf.UpdateFile('data.json',activosdata)
    if op == '9':
        valorN = input('Ingrese la nueva empresa responsable : ')
        atajo['empresaresponsable']=valorN
        cf.UpdateFile('data.json',activosdata)

def delActivos(inventario : dict):
    print('Ingrese el Codigo de campus del activo que desea eliminar')
    cf.delOp(inventario,'Activos')
    

def buscaractivos(inventario:dict):
    os.system('cls')
    print('Ingrese el codigo de campus del activo el cual desea buscar')
    resultado = cf.Search(inventario, 'Activos')
    diccionario = inventario['Activos'][resultado]
    del(diccionario['historialActivo'])
    lista = [(key,value)for key,value in diccionario.items()]
    print(tabulate(lista, tablefmt="grid"))
    os.system('pause')
    


    
    
        
    