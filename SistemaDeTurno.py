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
    
def numeroDeTurnoExiste(numeroTurno):

    if not os.path.exists("turnos.txt"):
        return False

    with open("turnos.txt","r",encoding="utf-8") as archivo:

        for linea in archivo:
            partes = linea.strip().split("|")
            if partes[0] == numeroTurno:
                return True    
    
    return False

def turnoFechayHoraExiste(fecha,hora):

    if not os.path.exists("turnos.txt"):
        return False
    
    with open("turnos.txt","r",encoding="utf-8") as archivo:

        for linea in archivo:
            partes = linea.strip().split("|")
            if partes[3] == fecha and partes[4] == hora:
                return True

    return False        


def AltaTurno():

    while True:

        limpiarPantalla()

        nombre = input("Ingrese su nombre: ")    
        apellido = input("Ingrese su apellido: ")

        fecha = pedirFecha()
        hora = pedirHora()

        while turnoFechayHoraExiste(fecha,hora):
            print("Ya existe un turno a esa hora y fecha")

            fecha = pedirFecha()
            hora = pedirHora()

        motivo = input("Ingrese el motivo del turno: ")

        numeroTurno = random.randrange(1000,9999)

        while numeroDeTurnoExiste(str(numeroTurno)):
            numeroTurno = random.randrange(1000,9999)

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

            archivo.write(f"{numeroTurno}|{nombre}|{apellido}|{fecha}|{hora}|{motivo}\n")
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

        if not os.path.exists("turnos.txt"):
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

def EliminarTurno():

    limpiarPantalla()

    if not os.path.exists("turnos.txt"):
        print("No hay turnos cargados.")
        input("ENTER para continuar...")
        return

    numero = input("Ingrese el número de turno a eliminar: ")

    turnos = []
    eliminado = False

    with open("turnos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("|")
            if partes[0] == numero:
                eliminado = True
            else:
                turnos.append(linea)

    if not eliminado:
        print("El número de turno no existe.")
        input("ENTER para continuar...")
        return

    with open("turnos.txt", "w", encoding="utf-8") as archivo:
        for t in turnos:
            archivo.write(t)

    print("Turno eliminado correctamente.")
    input("ENTER para continuar...")



def ListarTurnos():
   
        limpiarPantalla()

        if not os.path.exists("turnos.txt"):
            print("No hay turnos cargados.")
            input("ENTER para continuar...")
            return

        print("====== LISTADO DE TURNOS ======\n")

        with open("turnos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split("|")
                print(f"N° Turno: {partes[0]}")
                print(f"Nombre: {partes[1]} {partes[2]}")
                print(f"Fecha: {partes[3]}  Hora: {partes[4]}")
                print(f"Motivo: {partes[5]}")
                print("------------------------------")

        input("\nENTER para continuar...")

def ModificarTurno():

    limpiarPantalla()

    if not os.path.exists("turnos.txt"):
        print("No hay turnos cargados.")
        input("ENTER para continuar...")
        return

    numero = input("Ingrese el número de turno a editar: ")

    turnos = []
    encontrado = False

    with open("turnos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("|")

            if partes[0] == numero:
                encontrado = True

                print("\nTurno encontrado:")
                print(f"Nombre: {partes[1]} {partes[2]}")
                print(f"Fecha actual: {partes[3]}")
                print(f"Hora actual: {partes[4]}")
                print(f"Motivo actual: {partes[5]}")

                nueva_fecha = pedirFecha()
                nueva_hora = pedirHora()

                while turnoFechayHoraExiste(nueva_fecha, nueva_hora):
                    print("Ya existe un turno en esa fecha y hora.")
                    nueva_fecha = pedirFecha()
                    nueva_hora = pedirHora()

                nuevo_motivo = input("Ingrese el nuevo motivo: ")

                nueva_linea = f"{numero}|{partes[1]}|{partes[2]}|{nueva_fecha}|{nueva_hora}|{nuevo_motivo}\n"
                turnos.append(nueva_linea)

            else:
                turnos.append(linea)

    if not encontrado:
        print("El número de turno no existe.")
        input("ENTER para continuar...")
        return

    with open("turnos.txt", "w", encoding="utf-8") as archivo:
        for t in turnos:
            archivo.write(t)

    print("Turno editado correctamente.")
    input("ENTER para continuar...")


def Salir():

    limpiarPantalla()
    print("Cerrando el sistema.")
    sys.exit()


def MenuPrincipal():

    while True:

        limpiarPantalla()

        print(" -------- SISTEMAS DE TURNOS -------- \n")

        print(" 1 > Alta Turno ")

        print(" 2 > Buscar Turno por su número")

        print(" 3 > Eliminar Turno")

        print(" 4 > Listar Turno")

        print(" 5 > Modificar Turno")

        print(" 0 > Salir")

        print("----------------------------------------")

        opcion = (input(f"Ingrese la opción seleccionada: "))

        if not opcion.isdigit():

            print("ERROR: LA OPCIÓN DEBE SER UN NÚMERO VÁLIDO.\n")
            input("Presione ENTER para continuar...")
            continue

        opcion = int(opcion)

        if opcion == 1:
            AltaTurno()
        elif opcion == 2:
            BuscarTurnoPorNumero()
        elif opcion == 3:
            EliminarTurno()
        elif opcion == 4:
            ListarTurnos()
        elif opcion == 5:
            ModificarTurno()
        elif opcion == 0:
            Salir()
        else:
            print("LA OPCIÓN INGRESADA ES INCORRECTA. INTENTE DE NUEVO.")   
            input("Presione ENTER para continuar....")


MenuPrincipal()         