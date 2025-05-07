# Calcular precio final con descuento

# Ingresamos el precio original del producto
precio_original = float(input("Ingrese el precio del producto: "))

# Ingresamos el porcentaje de descuento
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

# Calculamos el valor del descuento
descuento = (precio_original * porcentaje_descuento) / 100

# Calculamos el precio final restando el descuento al precio original
precio_final = precio_original - descuento

# Mostramos el precio final con el descuento aplicado
print("El precio final con descuento es:", precio_final)
