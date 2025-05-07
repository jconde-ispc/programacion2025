Algoritmo ejercicio8Galletitas
	Definir total, paquetes, sobrantes Como Entero
	Escribir "Ingrese la cantidad total de galletitas:"
    Leer total
    paquetes <- trunc(total / 12) //la función trunc se utiliza para truncar (recortar) un número real (decimal) y quedarse únicamente con la parte entera, sin redondear
    sobrantes <- total % 12
    Escribir "Se pueden armar ", paquetes, " paquetes completos"
    Escribir "Sobrantes: ", sobrantes
FinAlgoritmo
