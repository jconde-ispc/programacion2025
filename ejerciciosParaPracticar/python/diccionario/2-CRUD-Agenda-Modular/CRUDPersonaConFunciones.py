agenda = {}

def mostrar_menu():
    print("Bienvenido a la agenda telefónica (Diccionario y Funciones)")
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar toda la agenda, elemento a elemento")
    print("5. Mostrar toda la agenda (diccionario completo)")
    print("6. Salir")

def agregar_persona():
    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")
    dni = input("Ingrese el DNI: ")
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el número de teléfono: ")
    
    persona = {
        "apellido": apellido,
        "nombre": nombre,
        "dni": dni,
        "email": email,
        "telefono": telefono
    }
    
    agenda[dni] = persona
    print("Persona agregada exitosamente.")

def modificar_persona():
    dni = input("Ingrese el DNI de la persona que desea modificar: ")
    
    if dni in agenda:
        persona = agenda[dni]
        print("Datos actuales de la persona:")
        print(persona)
        
        opcion = input("¿Desea cambiar los demás campos de la persona? (s/n): ")
        
        if opcion.lower() == "s":
            apellido = input("Ingrese el nuevo apellido: ")
            nombre = input("Ingrese el nuevo nombre: ")
            email = input("Ingrese el nuevo email: ")
            telefono = input("Ingrese el nuevo número de teléfono: ")
            
            persona["apellido"] = apellido
            persona["nombre"] = nombre
            persona["email"] = email
            persona["telefono"] = telefono
            
            print("Persona modificada exitosamente.")
        else:
            print("No se realizaron cambios.")
    else:
        print("No se encontró ninguna persona con ese DNI.")

def eliminar_persona():
    dni = input("Ingrese el DNI de la persona que desea eliminar: ")
    
    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada exitosamente.")
    else:
        print("No se encontró ninguna persona con ese DNI.")

def mostrar_agenda():
    if agenda:
        print("Agenda:")
        for dni, persona in agenda.items():
            print(f"DNI: {dni}")
            print(f"Apellido: {persona['apellido']}")
            print(f"Nombre: {persona['nombre']}")
            print(f"Email: {persona['email']}")
            print(f"Teléfono: {persona['telefono']}")
            print("--------------------")
    else:
        print("La agenda está vacía.")

