def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por cero."
        #raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    print(f"Esta es la invocacion a la funcion {suma(3,4)=}")
