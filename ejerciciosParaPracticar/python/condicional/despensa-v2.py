"""
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos
la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
el costo tiene un descuento del 10%. Si compra más de 24 unidades, el 
descuento es del 15%. Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento (si posee otros 
descuentos, se suma los descuentos).
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.
"""





unidadesDeLeche = int(input("Ingrese la cantidad de unidades de leche que compra el cliente"))
esJubiado = int(input("Ingrese 0 si el cliente no es jubilado, cualquier otro numero si el cliente es Jubilado"))


montoParcial = unidadesDeLeche * 1000
print(f"unidadesDeLeche {unidadesDeLeche} esJubiado {esJubiado}")

descuento = 0

if(esJubiado):
    descuento = 10

if(unidadesDeLeche > 24):
    descuento += 15
elif (unidadesDeLeche > 12):
    descuento += 10

montoDescontado = (montoParcial * descuento) / 100
montoAPagar = montoParcial - montoDescontado

print(f"El monto sin descuento es: {montoParcial}, el {descuento=}% da {montoDescontado} y el monto total a pagar es: {montoAPagar}")

