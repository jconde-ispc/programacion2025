Algoritmo ejercicio4PrecioDescuento
	//Precio con descuento
	Definir precio, descuento, montoDescuento, precioFinal Como Real
	Escribir "Ingrese el precio del producto:"
    Leer precio
    Escribir "Ingrese el porcentaje de descuento:"
    Leer descuento
    montoDescuento <- precio * descuento / 100
    precioFinal <- precio - montoDescuento
    Escribir "El precio final con descuento es: ", precioFinal
FinAlgoritmo
