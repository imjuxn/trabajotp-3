def realizar_operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    
    print(f"Resultados de las operaciones:")
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
    print(f"División: {num1} / {num2} = {division:.2f}")

def main():
    num1 = int(input("Ingrese el primer número: "))
    while num1 == 0:
        print("El número no puede ser 0. Por favor, ingrese un número distinto de 0.")
        num1 = int(input("Ingrese el primer número: "))
    
    num2 = int(input("Ingrese el segundo número: "))
    while num2 == 0:
        print("El número no puede ser 0. Por favor, ingrese un número distinto de 0.")
        num2 = int(input("Ingrese el segundo número: "))
    
    realizar_operaciones(num1, num2)

if __name__ == "__main__":
    main()