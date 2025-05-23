import matematicas

def main():
    #try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        print(f"Suma: {matematicas.suma(a, b)}")
        print(f"Resta: {matematicas.resta(a, b)}")
        print(f"Multiplicación: {matematicas.multiplicacion(a, b)}")
        print(f"División: {matematicas.division(a, b)}")
    #except ValueError as e:
    #    print(f"Error: {e}")

if __name__ == "__main__":
    main()
