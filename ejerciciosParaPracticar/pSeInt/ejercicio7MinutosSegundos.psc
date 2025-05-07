Algoritmo ejercicio7MinutosSegundos
	Definir segundos, minutos, restantes Como Real
	Escribir "Ingrese la cantidad de segundos:"
    Leer segundos
    minutos <- segundos / 60
    restantes <- segundos % 60
    Escribir "Equivale a ", minutos, " minuto(s) y ", restantes, " segundo(s)"
FinAlgoritmo
