import CRUDPersonaConFunciones

# Programa principal
while True:
    CRUDPersonaConFunciones.mostrar_menu()
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        CRUDPersonaConFunciones.agregar_persona()
    elif opcion == "2":
        CRUDPersonaConFunciones.modificar_persona()
    elif opcion == "3":
        CRUDPersonaConFunciones.eliminar_persona()
    elif opcion == "4":
        CRUDPersonaConFunciones.mostrar_agenda()
    elif opcion == "5":
        print("La agenda completa:")
        print(CRUDPersonaConFunciones.agenda)
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

