#Esto ya se vio en clases prcenciales, es sobre if. elif, else, entre otros, pero esta vez vamos a verlo mejor explicado y mas a fondo.

#Esto no hace falta explicarlo
if 10 > 9:
    print("Es correcto") #Recordar que debe de estar dentro de if

#Tambien unicamente colocando true nos dira que es verdadero, tambien se puede crear una variable que sea verdadera y colocarlo dentro
#del if
if True:
    print("Es correcto")

if 5 == 2:
    print("Es correcto") #esto al ser erroneo python no dira nada
else:
    print("Es incorrecto")#else es como decir "de lo contrario"

print("que animal es mi mascota?\n")
mascota = "perro"

if mascota == "gato":
    print("tu mascota es un gato")

elif mascota == "perro":
    print("tu mascota es un perro") #elif sirve colocar mas opciones ademas del if y else

else:
    print("no tengo idea cual es tu mascota")

#-----------------------------------------------
edad = int(input("Ingrese su edad: "))
calificacion = float(input("Ingrese su calificacion: "))

if edad >= 18:
    print("usted es mayor de edad")
    if calificacion >= 4.0:
        print("calificacion aprobada")
    else:
        print("calificacion reprobada")

else:
    print("usted es menor de edad")




