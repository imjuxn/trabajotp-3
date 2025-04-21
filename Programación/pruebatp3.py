def determinar_estacion(hemisferio, mes, dia):
    # Determinar la estación según el mes y el día
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        if hemisferio == 'N':
            return 'Invierno'
        else:
            return 'Verano'
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        if hemisferio == 'N':
            return 'Primavera'
        else:
            return 'Otoño'
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        if hemisferio == 'N':
            return 'Verano'
        else:
            return 'Invierno'
    else:
        if hemisferio == 'N':
            return 'Otoño'
        else:
            return 'Primavera'

def main():
    hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
    while hemisferio not in ['N', 'S']:
        hemisferio = input("Por favor, ingresa N para hemisferio norte o S para hemisferio sur: ").upper()

    mes = int(input("¿Qué mes es? (1-12): "))
    while mes < 1 or mes > 12:
        mes = int(input("Por favor, ingresa un mes válido (1-12): "))

    dia = int(input("¿Qué día es? (1-31): "))
    while dia < 1 or dia > 31:
        dia = int(input("Por favor, ingresa un día válido (1-31): "))

    # Validación básica para meses con menos de 31 días
    while (mes in [4, 6, 9, 11] and dia > 30) or (mes == 2 and dia > 28):
        dia = int(input("El mes ingresado no tiene tantos días. Por favor, ingresa un día válido: "))

    estacion = determinar_estacion(hemisferio, mes, dia)
    print(f"Te encuentras en {estacion}.")

if __name__ == "__main__":
    main()