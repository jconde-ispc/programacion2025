def mostrar_menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Opciones de usuario")
    print("2. Información")
    print("0. Salir")

def mostrar_submenu_usuario():
    print("\n--- SUBMENÚ: OPCIONES DE USUARIO ---")
    print("1. Crear usuario")
    print("2. Eliminar usuario")
    print("0. Volver al menú principal")

# Inicio del programa
opcion_principal = "-1"

while opcion_principal != "0":
    mostrar_menu_principal()
    opcion_principal = input("Seleccioná una opción: ")

    if opcion_principal == "1":
        opcion_submenu = -1
        while opcion_submenu != "0":
            mostrar_submenu_usuario()
            opcion_submenu = input("Seleccioná una opción del submenú: ")

            if opcion_submenu == "1":
                print("→ Creando usuario...")
            elif opcion_submenu == "2":
                print("→ Eliminando usuario...")
            elif opcion_submenu == "0":
                print("→ Volviendo al menú principal.")
                # Podriamos usar la palabra reservada break, esto hace salir del ciclo y quedar en el ciclo principal
                #break
            else:
                print("✖ Opción no válida en el submenú.")

    elif opcion_principal == "2":
        print("→ Esta es una aplicación de ejemplo con menú y submenú.")

    elif opcion_principal == "0":
        print("→ Saliendo del programa. ¡Hasta luego!")        
        # Podriamos usar la palabra reservada break, esto hace salir del ciclo
        #break
    
    else:
        print("✖ Opción no válida en el menú principal.")
