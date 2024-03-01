import os
import json
import modulos.menus as mn
import modulos.corefile as cf
import sys
import funciones.funcionesActivos as fa
import funciones.funcionespersonas as fp
import funciones.agregandoCVS as fcv
import funciones.funcioneszonas as fz
dataa = {
    'Activos':{},
    'Personas':{},
    'Zonas':{},
    'Asignacion':{},
}

inventario = cf.checkFile("data.json",dataa)
#fcv.añadiendoactivos(inventario)
#cf.UpdateFile('data.json', inventario)

if __name__ == "__main__":
   
    Runpro = True
    while Runpro:
        op = mn.menuPrincipal()
        if op == "1":
            Run1 = True
            while Run1:
                op1 = mn.menuAct()
                if op1 == "1":
                    isrun11 = True
                    while isrun11:
                        fa.Addactivos(inventario)
                        rta1 = 'x'
                        while (rta1 not in ['S','s','']):
                            rta1 = input('Desea Regresar agregar otro activo Si(S/s) Enter(No) :')
                            isrun11 = bool(rta1)
                if op1 == "2":
                    isrun112 = True
                    while isrun112:
                        fa.updateActivos(inventario)
                        rta12 = 'x'
                        while (rta12 not in ['S','s','']):
                            rta12 = input('Desea actualizar otro activo Si(S/s) Enter(No) :')
                            isrun112 = bool(rta12)
                if op1 == "3":
                    isruna3 = True
                    while isruna3:
                        fa.delActivos(inventario)
                        rta33 = 'x'
                        while (rta33 not in ['S','s','']):
                            rta33 = input('Desea actualizar otro activo Si(S/s) Enter(No) :')
                            isruna3 = bool(rta33)
                if op1 == "4":
                    pass
                if op1 == "5":
                    rta1 = 'x'
                    while (rta1 not in ['N','n','']):
                        rta1 = input('Desea Regresar al Menu principal No(n/N) Enter(si) Regresar :')
                        Run1 = bool(rta1)    
        if op == "2":
            Run2 = True
            while Run2:    
                op2 = mn.menuPer()
                if op2 == "1":
                    isrun22 = True
                    while isrun22:
                        fp.addpersonas(inventario)
                        rta1 = 'x'
                        while (rta1 not in ['S','s','']):
                            rta1 = input('Desea Regresar agregar otro activo Si(S/s) Enter(No) :')
                            isrun22 = bool(rta1)
                if op2 == "2":
                    pass
                if op2 == "3":
                    pass
                if op2 == "4":
                    pass
                if op2 == "5":
                    rta2 = 'x'
                    while (rta2 not in ['N','n','']):
                        rta2 = input('Desea Regresar al Menu principal No(n/N) Enter(si) Regresar :')
                        Run2 = bool(rta2)
        if op == "3":
            Run3 = True
            while Run3:  
                op3 = mn.menuZon()
                if op3 == "1":
                    isrunz1 = True
                    while isrunz1:
                        fz.agregarzonas(inventario)
                        rtaz1 = 'x'
                        while (rtaz1 not in ['S','s','']):
                            rtaz1 = input('Desea Regresar agregar otra zona Si(S/s) Enter(No) :')
                            isrunz1 = bool(rtaz1)
                if op3 == "2":
                    pass
                if op3 == "3":
                    pass
                if op3 == "4":
                    pass
                if op3 == "5":
                    rta3 = 'x'
                    while (rta3 not in ['N','n','']):
                        rta3 = input('Desea Regresar al Menu principal No(n/N) Enter(si) Regresar :')
                        Run3 = bool(rta3)
        if op == "4":
            Run4 = True
            while Run4:         
                op4 = mn.menuAsignacionA()
                if op4 == "1":
                    pass
                if op4 == "2":
                    pass
                if op4 == "3":
                    rta4 = 'x'
                    while (rta4 not in ['N','n','']):
                        rta4 = input('Desea Regresar al Menu principal No(n/N) Enter(si) Regresar :')
                        Run4 = bool(rta4)
        if op == "5":
            Run5 = True
            while Run5:
                op5 = mn.menuReportes()
                if op5 == "1":
                    pass
                if op5 == "2":
                    pass
                if op5 == "3":
                    pass
                if op5 == "4":
                    pass
                if op5 == "5":
                    pass
                if op5 == "6":
                    rta5 = 'x'
                    while (rta5 not in ['N','n','']):
                        rta5 = input('Desea Regresar al Menu principal No(n/N) Enter(si) Regresar :')
                        Run5 = bool(rta5)
        if op == "6":
            Run6 = True
            while Run6:
                op6 = mn.menuMAct()
                if op6 == "1":
                    pass
                if op6 == "2":
                    pass
                if op6 == "3":
                    pass
                if op6 == "4":
                    pass
                if op6 == "5":
                    rta6 = 'x'
                    while (rta6 not in ['N','n','']):
                        rta6 = input('Desea Regresar al Menu principal No(n/N) Enter(si) Regresar :')
                        Run6 = bool(rta6)
        if op == "7":
            rta = 'x'
            while (rta not in ['N','n','']):
                rta = input('Desea salir No(n/N) Enter(si) Salir :')
                Runpro = bool(rta)