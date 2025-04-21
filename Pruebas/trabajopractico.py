#Ejercicio 1
print("Hola Mundo")

#Ejercicio 2


nombre = input("Ingresa tu nombre: ")
print(f"Hola, {nombre}")

#Ejercicio 3
nombre = input("¿Me podrías indicar tu nombre, por favor?: ")
Edad = input("También me sería de gran ayuda tu edad: ")
Localidad = input("Por último dime de dónde eres, por favor: ")
print(f"Soy {nombre}, tengo {Edad} años y vivo en {Localidad}")

#Ejercicio 5

def imprimir_tabla_de_multiplicar(numero, rango):
    """Imprime la tabla de multiplicar de un número"""
    print(f"Tabla de multiplicar de {numero}:")
    for i in range(1, rango + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    numero = int(input("Ingrese un número: "))
    rango = int(input("Ingrese el rango de la tabla de multiplicar: "))
    imprimir_tabla_de_multiplicar(numero, rango)

if __name__ == "__main__":
    main()

    #ejercicio 7

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