import os
import json
import modulos.menus as mn
import modulos.corefile as cf
import sys
import funciones.funcionesActivos as fa
import funciones.funcionespersonas as fp
import funciones.agregandoCVS as fcv
import funciones.funcioneszonas as fz
import funciones.asignaciones as asi
import funciones.reportes as rp
import funciones.movimientodeactivos as mva
dataa = {
    'Activos':{},
    'Personas':{},
    'Zonas':{},
    'Asignacion':{},
}

inventario = cf.checkFile("data.json",dataa)
# Se añadio el archivo csv a data.json
#fcv.añadiendoactivos(inventario)
#cf.UpdateFile('data.json', inventario)


#se empiezan a mostar los menus
if __name__ == "__main__":
    Runpro = True
    while Runpro:
        try:
            op = mn.menuPrincipal()
        except KeyboardInterrupt:
            print('No se vale CTRL + C')
            os.system('pause')
            continue
        else:
            pass
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
                            rta33 = input('Desea eliminar otro activo Si(S/s) Enter(No) :')
                            isruna3 = bool(rta33)
                if op1 == "4":
                    isrunA4 = True
                    while isrunA4:
                        fa.buscaractivos(inventario)
                        rtaa4 = 'x'
                        while (rtaa4 not in ['S','s','']):
                            rtaa4 = input('Desea buscar otro activo Si(S/s) Enter(No) :')
                            isrunA4 = bool(rtaa4)
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
                        rtap111 = 'x'
                        while (rtap111 not in ['S','s','']):
                            rtap111 = input('Desea Regresar agregar otra persona Si(S/s) Enter(No) :')
                            isrun22 = bool(rtap111)
                if op2 == "2":
                    isrunP12 = True
                    while isrunP12:
                        fp.ActualizarPersonas(inventario)
                        rtap12 = 'x'
                        while (rtap12 not in ['S','s','']):
                            rtap12 = input('Desea Regresar actualizar la informacion de otra persona Si(S/s) Enter(No) :')
                            isrunP12 = bool(rtap12)
                if op2 == "3":
                    isrunP33 = True
                    while isrunP33:
                        fp.eliminarpersonas(inventario)
                        rtap33 = 'x'
                        while (rtap33 not in ['S','s','']):
                            rtap33 = input('Desea eliminar otra persona Si(S/s) Enter(No) :')
                            isrunP33 = bool(rtap33)
                if op2 == "4":
                    isrunP44 = True
                    while isrunP44:
                        fp.buscarpersonas(inventario)
                        rtap4 = 'x'
                        while (rtap4 not in ['S','s','']):
                            rtap4 = input('Desea eliminar otra persona Si(S/s) Enter(No) :')
                            isrunP44 = bool(rtap4)
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
                            rtaz1 = input('Desea agregar otra zona Si(S/s) Enter(No) :')
                            isrunz1 = bool(rtaz1)
                if op3 == "2":
                    isrunZ22 = True
                    while isrunZ22:
                        fz.actualizarzonas(inventario)
                        rtaz2 = 'x'
                        while (rtaz2 not in ['S','s','']):
                            rtaz2 = input('Desea actualizar otra zona Si(S/s) Enter(No) :')
                            isrunZ22 = bool(rtaz2)
                if op3 == "3":
                    isrunz33 = True
                    while isrunz33:
                        fz.eliminarzona(inventario)
                        rtaz3 = 'x'
                        while (rtaz3 not in ['S','s','']):
                            rtaz3 = input('Desea  eliminar otra zona Si(S/s) Enter(No) :')
                            isrunz33 = bool(rtaz3)
                if op3 == "4":
                    isrunZ4 = True
                    while isrunZ4:
                        fz.buscarzona(inventario)
                        rtaz4 = 'x'
                        while (rtaz4 not in ['S','s','']):
                            rtaz4 = input('Desea buscar otra zona Si(S/s) Enter(No) :')
                            isrunZ4 = bool(rtaz4)
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
                    isrunAs1 = True
                    while isrunAs1:
                        asi.añadirasignacion(inventario)
                        rtas1 = 'x'
                        while (rtas1 not in ['S','s','']):
                            rtas1 = input('Desea añadir otra asigancion Si(s/S) Enter(no) Regresar :')
                            isrunAs1 = bool(rtas1)
                if op4 == "2":
                    isrunAs2 = True
                    while isrunAs2:
                        asi.buscarasignacion(inventario)
                        rtas12 = 'x'
                        while (rtas12 not in ['S','s','']):
                            rtas12 = input('Desea buscar otra asigancion Si(s/S) Enter(no) Regresar :')
                            isrunAs2 = bool(rtas12)
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
                    isrunRA = True
                    while isrunRA:
                        rp.resportesactivos(inventario)
                        rtar4 = 'x'
                        while (rtar4 not in ['N','n','']):
                            rtar4 = input('Desea Regresar al Menu de reportes No(n/N) Enter(si) Regresar :')
                            isrunRA = bool(rtar4)
                if op5 == "2":
                    isrunRE2 = True
                    while isrunRE2:
                        rp.ActivosCate(inventario)
                        rtar42 = 'x'
                        while (rtar42 not in ['N','n','']):
                            rtar42 = input('Desea Regresar al Menu de reportes No(n/N) Enter(si) Regresar :')
                            isrunRE2 = bool(rtar42)
                if op5 == "3":
                    isrunRE3 = True
                    while isrunRE3:
                        rp.activosdadobaja(inventario)
                        rtar42s = 'x'
                        while (rtar42s not in ['N','n','']):
                            rtar42s = input('Desea Regresar al Menu de reportes No(n/N) Enter(si) Regresar :')
                            isrunRE3 = bool(rtar42s)
                if op5 == "4":
                    isrunrp4 = True
                    while isrunrp4:
                        rp.activosyasignacion(inventario)
                        rtar42sxs = 'x'
                        while (rtar42sxs not in ['N','n','']):
                            rtar42sxs = input('Desea Regresar al Menu de reportes No(n/N) Enter(si) Regresar :')
                            isrunrp4 = bool(rtar42sxs)
                if op5 == "5":
                    isrunRE55 = True
                    while isrunRE55:
                        rp.historialamov(inventario)
                        rtar42ss = 'x'
                        while (rtar42ss not in ['N','n','']):
                            rtar42ss = input('Desea Regresar al Menu de reportes No(n/N) Enter(si) Regresar :')
                            isrunRE55 = bool(rtar42ss)
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
                    isrunDA11 = True
                    while isrunDA11:
                        mva.retornodeactivos(inventario)
                        rtaDaa = 'x'
                        while (rtaDaa not in ['S','s','']):
                            rtaDaa = input('Desea retornar otro activo Si(s/S) Enter(no) Regresar :')
                            isrunDA11 = bool(rtaDaa)
                if op6 == "2":
                    isruDA1 = True
                    while isruDA1:
                        mva.dardebajAc(inventario)
                        rtaDa = 'x'
                        while (rtaDa not in ['S','s','']):
                            rtaDa = input('Desea dar de baja otro activo Si(s/S) Enter(no) Regresar :')
                            isruDA1 = bool(rtaDa)
                if op6 == "3":
                    isrunDA33 = True
                    while isrunDA33:
                        mva.cambiarasignacion(inventario)
                        rtaDa213 = 'x'
                        while (rtaDa213 not in ['S','s','']):
                            rtaDa213 = input('Desea re asiganar otro activo Si(s/S) Enter(no) Regresar :')
                            isrunDA33 = bool(rtaDa213)
                if op6 == "4":
                    isruDA2 = True
                    while isruDA2:
                        mva.garantiact(inventario)
                        rtaDa2 = 'x'
                        while (rtaDa2 not in ['S','s','']):
                            rtaDa2 = input('Desea enviar a garantia otro activo Si(s/S) Enter(no) Regresar :')
                            isruDA2 = bool(rtaDa2)
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