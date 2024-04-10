pregunta1 = input("cual es tu nombre?: ")
pregunta2 = int(input("Cuanto has vendido este mes?: "))

comision = pregunta2 * 0.13
comision = int(comision)

print(f"Hola {pregunta1}, basado en sus ventas su comision es de {comision}")