# Convertir segundos a minutos y segundos

# Ingresamos la cantidad total de segundos
segundos_totales = int(input("Ingrese la cantidad de segundos: "))

# Calculamos los minutos usando división entera
minutos = segundos_totales // 60

"""
// → División entera (sin decimales)
Este operador devuelve la parte entera de una división, descartando los decimales.

Es como trunc() en PSeInt.
"""

# Calculamos los segundos restantes usando el módulo
segundos_restantes = segundos_totales % 60

"""
% → Módulo (resto de la división)
Este operador devuelve el resto que queda al dividir dos números.
"""

# Mostramos el resultado
print("Equivale a", minutos, "minuto(s) y", segundos_restantes, "segundo(s)")
