import os
import modulos.corefile as cf
from tabulate import tabulate

def resportesactivos(inventario:dict):
    Activos = []
    borrandohistorial = {}
    for key, value in inventario['Activos'].items():
        borrandohistorial.update({key:value})
    for keys, values in borrandohistorial.items():
        try:
            del(borrandohistorial[keys]['historialActivo'])
        except KeyError:
            continue
        Activos.append(borrandohistorial)
    
    lines_per_page = 20
    for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
        subset_data = Activos[i:i + lines_per_page]
        totalPag = len(Activos)//lines_per_page
        os.system('cls')
        print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
        print(f'pagina {idx + 1} de {totalPag + 1}')
        os.system('cls')

    
    