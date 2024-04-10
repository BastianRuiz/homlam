nombre = input("Ingrese el nombre: ")
peso = float(input("Ingrese el peso: "))
altura = float(input("Ingrese la altura: "))
imc = peso/altura**2


if imc < 18.5:
    print("Bajo peso")

elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")

elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")

elif imc >= 30 and imc <= 34.9:
    print("Obesidad tipo 1")

elif imc >= 35 and imc <= 39.9:
    print("Obesidad tipo 2")

elif imc >= 40 :
    print("Obesidad tipo 3")

print(f"""tu nombre es: {nombre}
tu peso es: {peso}
 tu imc es: {imc}""")







