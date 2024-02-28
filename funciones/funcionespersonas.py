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
            isrunoficina = False
    
    personas = {
        
        "id":Id,
        "nombre":nombre,
        "Email":Email,
        "TelefonoMovil":Telefonomovil,
        "TelefonoCasa":telefonoCasa,
        "TelefonoPersonal":telefonopersonal,
        "telefonoficina":telefonooficina,
    
    }
    
    personasdata['Personas'].update({Id:personas})
    cf.createData('data.json',personasdata)
    
    
    
        
    