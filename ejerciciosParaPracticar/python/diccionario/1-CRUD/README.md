

Este archivo contiene un programa en Python que implementa un **CRUD (Crear, Leer, Actualizar, Eliminar)** para gestionar una agenda telefónica. La agenda se almacena en un **diccionario**, donde cada entrada tiene como clave el **DNI** de una persona y como valor otro diccionario que contiene los datos de esa persona (apellido, nombre, email y teléfono).

### ¿Qué hace el programa?

1. **Crear (Agregar una persona):** Permite al usuario ingresar los datos de una persona (apellido, nombre, DNI, email y teléfono) y los almacena en el diccionario `agenda` usando el DNI como clave.
2. **Leer (Mostrar datos):**
   - Opción 4: Muestra los datos de cada persona en la agenda, uno por uno.
   - Opción 5: Muestra la agenda completa como un diccionario.
3. **Actualizar (Modificar una persona):** Permite modificar los datos de una persona existente en la agenda, identificándola por su DNI.
4. **Eliminar (Eliminar una persona):** Permite eliminar a una persona de la agenda usando su DNI.
5. **Salir:** Finaliza el programa.

### Estructura del diccionario

La agenda es un diccionario donde:

- La **clave** es el DNI de la persona (un identificador único).
- El **valor** es otro diccionario que contiene los datos de la persona.

Ejemplo de una agenda con 4 elementos:

```python
agenda = {
    "12345678": {
        "apellido": "Pérez",
        "nombre": "Juan",
        "dni": "12345678",
        "email": "juan.perez@example.com",
        "telefono": "123456789"
    },
    "87654321": {
        "apellido": "Gómez",
        "nombre": "Ana",
        "dni": "87654321",
        "email": "ana.gomez@example.com",
        "telefono": "987654321"
    },
    "11223344": {
        "apellido": "López",
        "nombre": "Carlos",
        "dni": "11223344",
        "email": "carlos.lopez@example.com",
        "telefono": "1122334455"
    },
    "55667788": {
        "apellido": "Martínez",
        "nombre": "Laura",
        "dni": "55667788",
        "email": "laura.martinez@example.com",
        "telefono": "5566778899"
    }
}
```

### Ejemplo de uso

1. **Agregar una persona:** El usuario ingresa los datos de una persona, y esta se agrega al diccionario `agenda`.
2. **Modificar una persona:** Si el usuario desea cambiar el teléfono de "Juan Pérez", puede buscarlo por su DNI (`12345678`) y actualizar el campo correspondiente.
3. **Eliminar una persona:** Si el usuario elimina a "Ana Gómez", su entrada se elimina del diccionario.
4. **Mostrar la agenda:** El programa puede mostrar todos los datos de las personas o la estructura completa del diccionario.

Este programa es una implementación básica que utiliza un bucle infinito para interactuar con el usuario hasta que elija salir. Es útil para practicar el manejo de diccionarios y operaciones CRUD en Python.
