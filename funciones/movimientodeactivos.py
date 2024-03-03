import os
import modulos.corefile as cf

def retornodeactivos(inventario):
    pass

def dardebajAc(inventario:dict):
    os.system('cls')
    print('Ingrese el codigo de campus del activo que desea dar de baja')
    codCampus = cf.Search(inventario, 'Activos')
    atajo = inventario['Activos'][codCampus]
    atajo['Estado']= "Dado de Baja"
    cf.UpdateFile('data.json',inventario)
    
def garantiact(inventario:dict):
    os.system('cls')
    print('Ingrese el codigo de campus del activo que desea dar en garantia')
    codCampus = cf.Search(inventario, 'Activos')
    atajo = inventario['Activos'][codCampus]
    atajo['Estado']= "En Garantia"
    cf.UpdateFile('data.json',inventario)
    
