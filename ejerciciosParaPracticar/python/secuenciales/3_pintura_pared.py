# Calcular los litros de pintura necesarios

# Ingresamos el ancho de la pared
ancho = float(input("Ingrese el ancho de la pared (en metros): "))

# Ingresamos el alto de la pared
alto = float(input("Ingrese el alto de la pared (en metros): "))

# Ingresamos el rendimiento del producto (m2 que cubre por litro)
rendimiento = float(input("Ingrese el rendimiento del producto (m2 por litro): "))

# Calculamos el área de la pared
area = ancho * alto

# Calculamos los litros necesarios dividiendo el área por el rendimiento
litros_necesarios = area / rendimiento

# Mostramos cuántos litros se necesitan
print("Se necesitan", litros_necesarios, "litros de pintura")
