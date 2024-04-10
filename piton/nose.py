nombre = input("cual es tu nombre?: ")
asignatura = input("cual es la asignatura?: ")
nota1 = float(input("Ingresa la nota 1: "))
nota1 = nota1*0.15
nota2 = float(input("Ingresa la nota 2: "))
nota2 = nota2 * 0.25
nota3 = float(input("Ingresa la nota 3: "))
nota3 = nota3 * 0.30
nota4 = float(input("Ingresa la nota 4: "))
nota4 = nota4 * 0.30
notafinal = nota1 + nota2 + nota3 + nota4

print(f"tu nombre es: {nombre}")
print(f"tu asignatura es: {asignatura}")
print(f"tu nota  final es {notafinal}")
