""" 
----------------------------------------------------------------------------------
Leer números hasta que se ingrese 0 y mostrar su suma

Análisis EPS:
Entrada: Números ingresados por usuario hasta que sea 0.
Proceso: Leer número, si no es 0, sumar.
Salida: Suma total.
"""
print("Ejercicio 1 - Leer números hasta que se ingrese 0 y mostrar su suma")

suma = 0
numero = int(input("Ingrese un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))
print("La suma es:", suma)



""" 
----------------------------------------------------------------------------------
Pedir contraseñas hasta que sea correcta

Análisis EPS:
Entrada: Contraseña ingresada por el usuario.
Proceso: Comparar con clave correcta, repetir si es incorrecta.
Salida: Mensaje de bienvenida.
"""
print("Ejercicio 2 - Pedir contraseñas hasta que sea correcta")

clave_correcta = "secreta"
clave = input("Ingrese la contraseña: ")
while clave != clave_correcta:
    print("Incorrecta. Intente de nuevo.")
    clave = input("Ingrese la contraseña: ")
print("¡Acceso concedido!")



""" 
----------------------------------------------------------------------------------
Leer números positivos hasta que aparezca uno negativo y mostrar cuántos se ingresaron

Análisis EPS:
Entrada: Números positivos ingresados por usuario.
Proceso: Contar repeticiones mientras el número sea positivo.
Salida: Cantidad de números positivos ingresados.
"""

print("Ejercicio 3 - Leer números positivos")

contador = 0
numero = int(input("Ingrese un número positivo: "))
while numero >= 0:
    contador += 1
    numero = int(input("Ingrese otro número positivo: "))
print("Se ingresaron", contador, "números positivos.")
