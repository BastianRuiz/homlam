cont=0
while cont < 10:
    cont=cont+1
    print(cont)

cont2=-100
while cont2 < 0:
    cont2 = cont2 + 1
    print(cont2)

#Ingresar nombre, edad, sueldo de una persona, tener en cuenta que la edad debe estar en el rango de 18 a 65 años, cualquier otra edad
#es un error y debe reingresar, para el sueldo el rango debe ser de 100 a 999, sino repetir.
#Si la persona es mayor a 50 y tiene un sueldo menor a 600 añadir el 18% su sueldo. 
# Mostrar los datos.

nom = input("Ingrse su nombre: ")
edad = 0
while edad < 18 and edad > 65:
    print("error volver a ingresar edad")