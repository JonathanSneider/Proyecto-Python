import os
import modulos.corefile as cf
from tabulate import tabulate

def resportesactivos(inventario:dict):
    Activos = []
    borrandohistorial = {}
    for key, value in inventario['Activos'].items():
        borrandohistorial[key] = value.copy()
    for key, value in borrandohistorial.items():
        try:
            del borrandohistorial[key]['historialActivo']
        except KeyError:
            continue
    for keys, values in borrandohistorial.items():
        Activos.append(values)
    lines_per_page = 20
    for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
        subset_data = Activos[i:i + lines_per_page]
        totalPag = len(Activos)//lines_per_page
        os.system('cls')
        print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
        print(f'pagina {idx + 1} de {totalPag + 1}')
        input("Presione Enter para continuar...")

def ActivosCate(inventario:dict):
    os.system('cls')
    opciones = ["1","2","3"]
    categoria = ['EQUIPO DE COMPUTO','ELECTRODOMESTICO','JUEGO']
    menu =[["1. Equipo de computo"], ["2. Electrodomestico"], ["3. Juego"]]
    print(tabulate(menu, tablefmt="grid"))
    op = input('Ingrea una categoria : ')
    if op not in opciones:
        print('Ingresaste una opcion no valida')
        input("Presione Enter para continuar...")
        return
    if op == "1":
        Activos = []
        borrandohistorial = {}
        for key, value in inventario['Activos'].items():
            if value['categoria'] == 'EQUIPO DE COMPUTO':
                borrandohistorial[key] = value.copy()
                try:
                    del borrandohistorial[key]['historialActivo']
                except KeyError:
                    continue
        for keys, values in borrandohistorial.items():
            Activos.append(values)
        lines_per_page = 15
        for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
            subset_data = Activos[i:i + lines_per_page]
            totalPag = len(Activos)//lines_per_page
            os.system('cls')
            print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
            print(f'pagina {idx + 1} de {totalPag + 1}')
            input("Presione Enter para continuar...")
    if op == "2":
        Activos = []
        borrandohistorial = {}
        for key, value in inventario['Activos'].items():
            if value['categoria'] == 'ELECTRODOMESTICO':
                borrandohistorial[key] = value.copy()
                try:
                    del(borrandohistorial[key]['historialActivo'])
                except KeyError:
                    continue
        for keys, values in borrandohistorial.items():
            Activos.append(values)
        lines_per_page = 20
        for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
            subset_data = Activos[i:i + lines_per_page]
            totalPag = len(Activos)//lines_per_page
            os.system('cls')
            print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
            print(f'pagina {idx + 1} de {totalPag + 1}')
            input("Presione Enter para continuar...")
    if op == "3":
        Activos = []
        borrandohistorial = {}
        for key, value in inventario['Activos'].items():
            if value['categoria'] == 'JUEGO':
                borrandohistorial[key] = value.copy()
                try:
                    del(borrandohistorial[key]['historialActivo'])
                except KeyError:
                    continue
        for keys, values in borrandohistorial.items():
            Activos.append(values)
        lines_per_page = 20
        for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
            subset_data = Activos[i:i + lines_per_page]
            totalPag = len(Activos)//lines_per_page
            os.system('cls')
            print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
            print(f'pagina {idx + 1} de {totalPag + 1}')
            input("Presione Enter para continuar...")
def activosdadobaja(inventario:dict):
    Activos = []
    borrandohistorial = {}
    for key, value in inventario['Activos'].items():
        if value['estado'] == 'Dado de Baja':
            borrandohistorial[key] = value.copy()
            try:
                del(borrandohistorial[key]['historialActivo'])
            except KeyError:
                continue
    for keys, values in borrandohistorial.items():
        Activos.append(values)
    lines_per_page = 20
    for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
        subset_data = Activos[i:i + lines_per_page]
        totalPag = len(Activos)//lines_per_page
        os.system('cls')
        print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
        print(f'pagina {idx + 1} de {totalPag + 1}')
        input("Presione Enter para continuar...")
    
def historialamov(inventario:dict):
    os.system('cls')
    print('Ingrese el codigo de campus del activo del cual quieres ver el historial de movimientos')
    activoss = cf.Search(inventario,'Activos')
    historials = []
    for keys, values in inventario['Activos'][activoss].items():
        if keys == "historialActivo":
            for value in inventario['Activos'][activoss][keys].items():
                historials.append(value)
    lines_per_page = 20
    for idx, i in enumerate(range(0, len(historials), lines_per_page)):
        subset_data = historials[i:i + lines_per_page]
        totalPag = len(historials)//lines_per_page
        os.system('cls')
        print(tabulate(subset_data, tablefmt="grid", floatfmt=(".0f")))
        print(f'pagina {idx + 1} de {totalPag + 1}')
        input("Presione Enter para continuar...")

def activosyasignacion(inventario:dict):
    Activos = []
    codcam = {}
    for key, value in inventario['Activos'].items():
        for keye,valuee in inventario['Asignacion'].items():
            if key in valuee['Activos']:
                TipoAsignacion = {
                    "Activo":key,
                    "AsignadoA":inventario["Asignacion"][keye]['AsignadoA'],
                    "TipoAsignacion":inventario["Asignacion"][keye]['TipoAsignacion']
                }
                codcam.update({key:TipoAsignacion})
    for keys, values in codcam.items():
        Activos.append(values)
    lines_per_page = 20
    for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
        subset_data = Activos[i:i + lines_per_page]
        totalPag = len(Activos)//lines_per_page
        os.system('cls')
        print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
        print(f'pagina {idx + 1} de {totalPag + 1}')
        input("Presione Enter para continuar...")
    