from EstudianteClass import Estudiante

mat = int(input("Ingrse matricula: "))
nom = input("Ingrese nombre: ")
email = input("ingrese email")
edad = int(input("Ingrese su edad: "))
grat = bool(input("True/False tiene gratuidad: "))
arancel = int(input("Ingresa arancel: "))
prom = float(input("ingresa promedio: "))


est = Estudiante(mat, nom, email, edad, grat, arancel, prom)

print(f"""Menu:
1. Listar datos
2. verificar edad
3. verificar beca
4. modificar promedio
5. ver descuento arancel
0. salir""")

op = 1
while op > 0:
    op = int(input("Ingresa opcion: "))
    match op:
        case 1:
            print(est.listar())
        case 2:
            print(est.verificaredad())
            


print(est.listar())
print(est.verificargratuidad())
print(est.modificarpromedio(5.1))
print(est.listar())
print(f"su descuento es de {est.beca()}")