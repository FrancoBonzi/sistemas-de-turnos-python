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
        #AltaTurno()
    elif opcion == 2:
        #BuscarTurnoPorNumero
    elif opcion == 3:
        Salir()
        break
    else:
        print("LA OPCIÓN INGRESADA ES INCORRECTA. INTENTE DE NUEVO.")   
        input("Presione ENTER para continuar....")


MenuPrincipal()         