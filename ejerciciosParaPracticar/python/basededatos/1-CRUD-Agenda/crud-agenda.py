""" 
CRUD similar al ejemplo de Agenda usando Diccionario, pero en esta ocasión es conectado a una base de datos MySQL.
Este código utiliza la biblioteca mysql.connector para interactuar con la base de datos.

Primero, asegurarse tener instalada la biblioteca mysql-connector-python ejecutando:

pip install mysql-connector-python

"""

import mysql.connector

def crear_base_datos():
    """Crea la base de datos si no existe."""
    conexion_temp = mysql.connector.connect(
        host="localhost",
        user="EL_USUARIO",  # Cambia esto por tu usuario de MySQL
        password="LA_CLAVE"  # Cambia esto por tu contraseña de MySQL
    )
    cursor_temp = conexion_temp.cursor()
    #Acá hay código SQL
    cursor_temp.execute("CREATE DATABASE IF NOT EXISTS agenda_db") # agenda_db se llamará la base de datos (puedes elegir el nombre que desees)
    conexion_temp.close()

def crear_tabla_si_no_existe(conexion):
    """Crea la tabla 'personas' si no existe."""
    cursor = conexion.cursor()
    
    #Acá hay código SQL
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personas (
        dni VARCHAR(20) PRIMARY KEY,
        apellido VARCHAR(50),
        nombre VARCHAR(50),
        email VARCHAR(100),
        telefono VARCHAR(20)
    )
    """)
    conexion.commit()

# Crear la base de datos si no existe
crear_base_datos()

# Configuración de la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="EL_USUARIO",  # Cambia esto por tu usuario de MySQL
    password="LA_CLAVE",  # Cambia esto por tu contraseña de MySQL
    database="agenda_db"  # Cambia esto por el nombre de tu base de datos
)

# Crear la tabla si no existe
crear_tabla_si_no_existe(conexion)

cursor = conexion.cursor()

while True:
    print("\nBienvenido a la agenda telefónica (MySQL)")
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar toda la agenda")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        dni = input("Ingrese el DNI: ")
        apellido = input("Ingrese el apellido: ")
        nombre = input("Ingrese el nombre: ")
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el número de teléfono: ")

        #Acá hay código SQL
        cursor.execute("""
        INSERT INTO personas (dni, apellido, nombre, email, telefono) 
        VALUES (%s, %s, %s, %s, %s)
        """, (dni, apellido, nombre, email, telefono))
        conexion.commit()
        print("Persona agregada exitosamente.")

    elif opcion == "2":
        dni = input("Ingrese el DNI de la persona que desea modificar: ")
        cursor.execute("SELECT * FROM personas WHERE dni = %s", (dni,)) #Acá hay código SQL
        persona = cursor.fetchone()

        if persona:
            print("Datos actuales de la persona:", persona)
            apellido = input("Ingrese el nuevo apellido: ")
            nombre = input("Ingrese el nuevo nombre: ")
            email = input("Ingrese el nuevo email: ")
            telefono = input("Ingrese el nuevo número de teléfono: ")

            #Acá hay código SQL
            cursor.execute("""
            UPDATE personas
            SET apellido = %s, nombre = %s, email = %s, telefono = %s
            WHERE dni = %s
            """, (apellido, nombre, email, telefono, dni))
            conexion.commit()
            print("Persona modificada exitosamente.")
        else:
            print("No se encontró ninguna persona con ese DNI.")

    elif opcion == "3":
        dni = input("Ingrese el DNI de la persona que desea eliminar: ")
        cursor.execute("DELETE FROM personas WHERE dni = %s", (dni,)) #Acá hay código SQL
        conexion.commit()
        if cursor.rowcount > 0:
            print("Persona eliminada exitosamente.")
        else:
            print("No se encontró ninguna persona con ese DNI.")

    elif opcion == "4":
        cursor.execute("SELECT * FROM personas") #Acá hay código SQL
        personas = cursor.fetchall()
        if personas:
            print("Agenda:")
            for persona in personas:
                print(f"DNI: {persona[0]}, Apellido: {persona[1]}, Nombre: {persona[2]}, Email: {persona[3]}, Teléfono: {persona[4]}")
        else:
            print("La agenda está vacía.")

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

# Cerrar la conexión
cursor.close()
conexion.close()