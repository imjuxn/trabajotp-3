EDAD_MINIMA = 21

edad= int(input("¿Me indicarías tu edad, por favor?: "))
categoria = input("ingrese su categoria (A, B, C, D, E, F, G)")

if edad >= EDAD_MINIMA and (categoria == "D" or categoria == "d"):
    print("Puede conducir una ambulancia")
else:
    print("No puede conducir ambulancia")