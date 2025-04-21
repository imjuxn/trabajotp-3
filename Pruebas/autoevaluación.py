a = 1
b = 2
c = 4

A = True
B = False
C = False

r1 = (2 * b - 1) / (2 * a) > 3
r2 = a * (b * c) >= 30 and not((a + b) * c >= (350 * c))
r3 = A and r1 or B == r2
r4= A and B and r3 and C != r1

print(f"{r2}, {r3}, {r1}, {r4}")

#----
cantidad_invitados = input int("inserte la cantidad de invitados: ")
hamburguesas_por_invitado = input int("inserte la cantidad de hamburguesas que come cada invitado: ")

hamgurguesas_a_comprar = cantidad_invitados * hamburguesas_por_invitado

print(hamgurguesas_a_comprar)