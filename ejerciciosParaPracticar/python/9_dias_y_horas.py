# Calcular días y horas a partir de una cantidad de horas

# Ingresamos la cantidad total de horas
horas_totales = int(input("Ingrese la cantidad total de horas: "))

# Calculamos los días completos usando división entera
dias = horas_totales // 24

# Calculamos las horas restantes usando el módulo
horas_restantes = horas_totales % 24

# Mostramos los resultados
print("Equivale a", dias, "día(s) y", horas_restantes, "hora(s)")
