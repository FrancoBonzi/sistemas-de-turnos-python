import os, sys, random

def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pedirFecha():
    while True:
        fecha = input("Ingrese la fecha del turno (DD/MM/AAAA): ")

        partes = fecha.split("/")

        if len(partes) != 3:
            print("Formato incorrecto.")
            input("ENTER para continuar...")
            continue

        if not (partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit()):
            print("La fecha debe contener solo números.")
            input("ENTER para continuar...")
            continue

        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])

        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 2024:
            print("Fecha inválida.")
            input("ENTER para continuar...")
            continue

        return fecha


def pedirHora():
    while True:
        hora = input("Ingrese la hora del turno (HH:MM): ")

        partes = hora.split(":")

        if len(partes) != 2:
            print("Formato incorrecto.")
            input("ENTER para continuar...")
            continue

        if not (partes[0].isdigit() and partes[1].isdigit()):
            print("La hora debe ser numérica.")
            input("ENTER para continuar...")
            continue

        h = int(partes[0])
        m = int(partes[1])

        if h < 0 or h > 23 or m < 0 or m > 59:
            print("Hora inválida.")
            input("ENTER para continuar...")
            continue

        return hora
    
def AltaTurno():

    while True:

        limpiarPantalla()

        nombre = input("Ingrese su nombre: ")    
        apellido = input("Ingrese su apellido: ")

        fecha = pedirFecha()
        hora = pedirHora()

        motivo = input("Ingrese el motivo del turno: ")

        numeroTurno = random.randrange(1,1000)

        limpiarPantalla()

        print("==== TURNO GENERADO ====\n")
        print(f"N° de Turno: {numeroTurno}")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"Fecha: {fecha}")
        print(f"Hora: {hora}")
        print(f"Motivo: {motivo}")
        print("==========================")

        with open("turnos.txt","a",encoding="utf-8") as archivo:
            archivo.write(f"{numeroTurno}|{nombre}|{apellido}|{fecha}|{hora}|{motivo}")

        respuesta = input("¿Desea agregar otro turno? (s/n): ").lower()

        while respuesta != 's' and respuesta != 'n':

            input("ERROR: DEBES INGRESAR 's' o 'n'.\n")
            respuesta = input("¿Desea agregar otro turno? (s/n): ").lower()

        if respuesta == 'n':
            return    

def BuscarTurnoPorNumero():

    while True:

        limpiarPantalla()

        numero_Turno = input("Ingrese el número del turno que está buscando: ")

        if os.path.exists("turnos.txt"):
            print("Aún no hay datos cargados... \n")
            input("Presione ENTER para continuar.")
            return

        fueEncontrado = False

        with open("turnos.txt","r",encoding="utf-8") as archivo:

            for linea in archivo:
                partes = linea.strip().split("|")

                if partes[0] == numero_Turno:

                    limpiarPantalla()

                    print("=== TURNO ENCONTRADO === \n")
                    print(f"Número del turno: {partes[0]}")
                    print(f"Nombre: {partes[1]}")
                    print(f"Apellido: {partes[2]}")
                    print(f"Fecha: {partes[3]}")
                    print(f"Hora: {partes[4]}")
                    print(f"Motivo: {partes[5]}")

                    print("=========================\n")

                    fueEncontrado = True
                    break
            
            if not fueEncontrado:
                print("El número de turno ingresado no fue encontrado.")

            respuesta = input("¿Desea buscar otro número de turno (s/n): ").lower()

            while respuesta != 's' and respuesta != 'n':
                print("Error: Debes ingresar 's' o 'n'. \n")

                respuesta = input("¿Desea ingresar 's' o 'n'. \n").lower()


            if respuesta == 'n':
                return    


def Salir():

    limpiarPantalla()
    print("Cerrando el sistema.")
    sys.exit()


def MenuPrincipal():

    print(" -------- SISTEMAS DE TURNOS -------- \n")

    print(" 1 > Alta Turno ")

    print(" 2 > Buscar Turno por su número")

    print(" 3 > Salir")

    print("----------------------------------------")

    opcion = input("Ingrese la opción seleccionada: ")

    if not opcion.isdigit():

        print("ERROR: LA OPCIÓN DEBE SER UN NÚMERO VÁLIDO.\n")

        opcion = input("Ingrese la opción seleccionada: ")

    opcion = int(opcion)

    if opcion == 1:
        AltaTurno()
    elif opcion == 2:
        BuscarTurnoPorNumero
    elif opcion == 3:
        Salir()
    else:
        print("LA OPCIÓN INGRESADA ES INCORRECTA. INTENTE DE NUEVO.")   
        input("Presione ENTER para continuar....")


MenuPrincipal()         