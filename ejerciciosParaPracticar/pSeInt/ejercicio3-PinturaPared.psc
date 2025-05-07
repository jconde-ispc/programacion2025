Algoritmo ejercicio3 //Litros de pintura necesarios
	
	//Averiguar cuántos litros de pintura se necesitan para pintar una pared,
	// conociendo sus medidas y el rendimiento del producto.

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	//LEXICO
	//DATOS
	Definir ancho, alto, rendimiento como Real
	//CALCULOS
	Definir area como Real
	//RESULTADO
	Definir litros como Real
	
	//OBTENIENDO LOS DATOS
	Escribir "Ingrese el ancho de la pared:"
    Leer ancho
    Escribir "Ingrese el alto de la pared:"
    Leer alto
    Escribir "Ingrese el rendimiento del producto (m2 por litro):"
    Leer rendimiento
    
	//HACIENDO LOS CALCULOS
	area <- ancho * alto	
	litros <- area / rendimiento
	
	//MOSTRANDO EL RESULTADO
    Escribir "Se necesitan ", litros, " litros de pintura"
FinAlgoritmo
