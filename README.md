# 📅 Sistema de Turnos en Python

## 📌 Descripción del proyecto

Aplicación de consola desarrollada en Python, orientada a la gestión de turnos.
Permite realizar operaciones de alta, consulta, listado, modificación y eliminación de turnos, utilizando archivos de texto para el almacenamiento de la información.

## 🧩 Funcionalidades

El sistema permite:

- Dar de alta turnos
- Buscar turnos por número
- Listar todos los turnos registrados
- Modificar turnos existentes
- Eliminar turnos

## 🧑‍💻 Datos solicitados por teclado

Para la carga de un turno, el sistema solicita:

- Nombre
- Apellido
- Fecha del turno (DD/MM/AAAA)
- Hora del turno (HH:MM)
- Motivo del turno

El número de turno se genera automáticamente y sirve como identificador único.

## 🛡️ Validaciones implementadas

- Control de formato de fecha y hora
- Evita turnos duplicados en la misma fecha y hora
- Evita la repetición del número de turno
- Validación de opciones ingresadas en el menú
- Control de existencia del archivo de datos
