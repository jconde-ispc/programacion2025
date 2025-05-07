Algoritmo ejercicio9DiasyHoras
	Definir horas, dias, restantes Como Entero
    Escribir "Ingrese la cantidad total de horas:"
    Leer horas
    dias <- trunc(horas / 24)
    restantes <- horas % 24
    Escribir "Equivale a ", dias, " día(s) y ", restantes, " hora(s)"
FinAlgoritmo
