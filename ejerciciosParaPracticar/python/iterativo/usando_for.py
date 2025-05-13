""" 
Sumar 5 números que ingresa el usuario

Análisis EPS:
Entrada: 5 números ingresados por el usuario.
Proceso: Repetir 5 veces: leer número y acumularlo.
Salida: Suma total.
""" 
print("Ejercicio 1 - Sumar 5 números que ingresa el usuario")

suma = 0
for i in range(5):
    numero = int(input("Ingrese un número: "))
    suma += numero
print("La suma total es:", suma)


""" 
----------------------------------------------------------------------------------
Mostrar los primeros 10 múltiplos de 3

Análisis EPS:
Entrada: No se necesita entrada.
Proceso: Iterar 10 veces, calcular múltiplo de 3 y mostrar.
Salida: Múltiplos de 3 del 1° al 10°.
"""
print("Ejercicio 2 - Mostrar los primeros 10 múltiplos de 3")

for i in range(1, 11):
    print(i * 3)

""" 
----------------------------------------------------------------------------------
Leer 4 edades y mostrar la mayor

Análisis EPS:
Entrada: 4 edades.
Proceso: Repetir 4 veces: comparar cada edad con la mayor actual.
Salida: Edad mayor.
"""
print("Ejercicio 3 - Leer 4 edades y mostrar la mayor")

mayor = 0
for i in range(4):
    edad = int(input("Ingrese una edad: "))
    if edad > mayor:
        mayor = edad
print("La edad mayor es:", mayor)

