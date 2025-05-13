# Calcular cuántos paquetes de galletitas se pueden armar

# Ingresamos el total de galletitas disponibles
total_galletitas = int(input("Ingrese la cantidad total de galletitas: "))

# Calculamos cuántos paquetes completos se pueden armar (de 12 unidades)
paquetes = total_galletitas // 12



# Calculamos cuántas galletitas sobran
sobrantes = total_galletitas % 12

# Mostramos los resultados
print("Se pueden armar", paquetes, "paquetes completos")
print("Sobrantes:", sobrantes, "galletitas")


