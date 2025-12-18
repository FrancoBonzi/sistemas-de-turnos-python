# 📅 Sistema de Turnos en Python

Mini aplicación de consola desarrollada en **Python**, que permite la gestión básica de turnos mediante archivos de texto.  

## 🧩 Funcionalidades

El sistema permite:

- ✅ **Dar de alta turnos**
- 🔍 **Buscar turnos por número**
- 📋 **Listar todos los turnos registrados**
- ✏️ **Modificar un turno existente**
- 🗑️ **Eliminar un turno**
- 🚫 **Evitar turnos duplicados** (misma fecha y hora)
- 🔢 **Evitar números de turno repetidos**

Toda la información se almacena en un archivo de texto (`turnos.txt`).

## 🧑‍💻 Datos solicitados por teclado

Al generar un turno, el sistema solicita:

- Nombre
- Apellido
- Fecha del turno (DD/MM/AAAA)
- Hora del turno (HH:MM)
- Motivo del turno

El **número de turno** se genera automáticamente de forma aleatoria y única.

Cada turno se guarda en una línea con el siguiente formato:

