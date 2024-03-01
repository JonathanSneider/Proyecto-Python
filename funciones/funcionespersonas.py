import os
import modulos.corefile as cf
def addpersonas(personasdata):
    os.system('cls')
    try:
        Id = int(input('Ingrese el Numero de CC o NIT : '))
    except ValueError:
        print('Ingrese un numero de CC o NIT valido : ')
        os.system('pause')
        addpersonas(personasdata)
    else:
        pass
    idd = str(Id)
    if idd in personasdata['Personas']:
        print('El id que ingresaste ya se encuentra registrado')
        os.system('pause')
        return
    else:
        pass
    nombre = input('Ingrese el nombre : ')
    Email = input('Ingrese el email : ')
    isrunmovil = True
    while isrunmovil:
        try:
            Telefonomovil = int(input('Ingrese el telefono movil : '))
        except ValueError:
            print('ingrese un numero de telefono valido')
            os.system('pause')
            continue
        else:
            if (Telefonomovil < 0):
                print('Ingresa un numero valido')
                os.system('pause')
                continue
            else:
                pass
            isrunmovil = False
    isruncasa = True
    while isruncasa:
        try:
            telefonoCasa = int(input('Ingrese el numero de telefono de su casa '))
        except ValueError:
            print('Ingrese un numero de telefono valido')
            os.system('pause')
            continue
        else:
            if (telefonoCasa < 0):
                print('Ingresa un numero valido')
                os.system('pause')
                continue
            else:
                pass
            isruncasa = False
            
    isrunpersonal = True
    while isrunpersonal:
        try:
            telefonopersonal = int(input('Ingrese el numero de telefono personal '))
        except ValueError:
            print('Ingrese un numero de telefono valido')
            os.system('pause')
            continue
        else:
            if (telefonopersonal < 0):
                print('Ingresa un numero valido')
                os.system('pause')
                continue
            else:
                pass
            isrunpersonal = False
    isrunoficina = True
    while isrunoficina:
        try:
            telefonooficina= int(input('Ingrese el numero de telefono de la oficina '))
        except ValueError:
            print('Ingrese un numero de telefono valido')
            os.system('pause')
            continue
        else:
            if (telefonooficina < 0):
                print('Ingresa un numero valido')
                os.system('pause')
                continue
            else:
                pass
            isrunoficina = False
    personas = {
        
        "id":idd,
        "nombre":nombre,
        "Email":Email,
        "TelefonoMovil":Telefonomovil,
        "TelefonoCasa":telefonoCasa,
        "TelefonoPersonal":telefonopersonal,
        "telefonoficina":telefonooficina,
    
    }
    
    personasdata['Personas'].update({idd:personas})
    cf.UpdateFile('data.json',personasdata)
    
def ActualizarPersonas(inventario:dict):
    os.system('cls')
    print('Ingrese el id de la persona que desea actualizar')
    idPer = cf.Search(inventario, 'Personas')
    atajo = inventario['Personas'][idPer]
    opciones = ['1','2','3','4','5','6']    
    print('1. Nombre\n2. Email\n3. Telefono Movil\n4. Telefono de la Casa\n5. Telefono Personal\n6. Telefono oficina')
    op = input('Seleccione una opcion : ')
    if op not in opciones:
        print('Ingresaste una opciones no valida')
        os.system('pause')
        return
    else:
        pass
    if op == '1':
        valorN = input('Ingrese el nuevo nombre : ')
        atajo['nombre']=valorN
        cf.UpdateFile('data.json',inventario)
    if op == '2':
        valorN = input('Ingrese el nuevo email : ')
        atajo['Email']=valorN
        cf.UpdateFile('data.json',inventario)
    if op == '3':
        isrun3 = True
        while isrun3:
            try:
                valorN = int(input('Ingrese el nuevo numero de movil : '))
            except ValueError:
                print('Ingrese un numero valido')
                os.system('pause')
            else:
                if (valorN < 0):
                    print('Ingresa un numero valido')
                    os.system('pause')
                    continue
                else:
                    pass
                isrun3 = False
        atajo['TelefonoMovil']=valorN
        cf.UpdateFile('data.json',inventario)
    if op == '4':
        isrun4 = True
        while isrun4:
            try:
                valorN = int(input('Ingrese el nuevo numero telefonico de la casa : '))
            except ValueError:
                print('Ingrese un numero valido')
                os.system('pause')
            else:
                if (valorN < 0):
                    print('Ingresa un numero valido')
                    os.system('pause')
                    continue
                else:
                    pass
                isrun4 = False
        atajo['TelefonoCasa']=valorN
        cf.UpdateFile('data.json',inventario)
    if op == '5':
        isrun5 = True
        while isrun5:
            try:
                valorN = int(input('Ingrese el nuevo numero telefonico personal : '))
            except ValueError:
                print('Ingrese un numero valido')
                os.system('pause')
            else:
                if (valorN < 0):
                    print('Ingresa un numero valido')
                    os.system('pause')
                    continue
                else:
                    pass
                isrun5 = False
        atajo['TelefonoPersonal']=valorN
        cf.UpdateFile('data.json',inventario)
    if op == '6':
        isrun6 = True
        while isrun6:
            try:
                valorN = int(input('Ingrese el nuevo numero telefonico de la oficina : '))
            except ValueError:
                print('Ingrese un numero valido')
                os.system('pause')
            else:
                if (valorN < 0):
                    print('Ingresa un numero valido')
                    os.system('pause')
                    continue
                else:
                    pass
                isrun6 = False
        atajo['telefonoficina']=valorN
        cf.UpdateFile('data.json',inventario)
        
def eliminarpersonas(inventario):
    cf.delOp(inventario, 'Personas')
    
        
    