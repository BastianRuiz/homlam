from persona import persona

persona1 = persona("21.744.095-5", "Bastian", "pxlnoz@gmail.com", 18)
print(persona1.MostrarDatosPersona())
print(persona1.mayoredad())

#Ingresar los datos de la persona por teclado, luego crear un  menu para acceder a los metodos
run = input("ingresar run de la persona: ")
nombre = input("ingresar nombre de la persona: ")
email = input("ingresar email de la persona: ")
edad = int(input("ingresar edad de la persona: "))

p2 = persona(run, nombre, email, edad)
print("### Menu ###")
print("# 1. mostrardatos #")
print("# 2. verificar edad #" )
print("####################")
op = 0
while(op>0):
    op = int(input("Ingresar una opcion: "))
    if op == 1:
        print(p2.MostrarDatosPersona())
    elif op == 2:
        print(p2.mayoredad())


print(p2.MostrarDatosPersona())
print(p2.mayoredad())


