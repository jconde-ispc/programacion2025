import matematicas

def main():
    #try:
        aaa = float(input("Ingrese el primer número: "))
        bbb = float(input("Ingrese el segundo número: "))

        print(f"Suma: {matematicas.suma(aaa, bbb)}")
        print(f"Resta: {matematicas.resta(aaa, bbb)}")
        print(f"Multiplicación: {matematicas.multiplicacion(aaa, bbb)}")
        print(f"División: {matematicas.division(aaa, bbb)}")
    #except ValueError as e:
    #    print(f"Error: {e}")

if __name__ == "__main__":
    main()
