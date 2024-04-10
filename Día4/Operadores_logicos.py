#Los operadores logicos son: and, or y not, and quiere decir que ambas condiciones deben cumplirse, or quiere decir que basta con que
#se cumpla una condicion, y not quiere decir que no se debe cumplir ninguna condicion

#condicion logica and
mi_bool = 4 < 5 and 5 > 6 #saldra que mi_bool es igual a false, esto debido que si bien 4 si es menor a 5, 5 no es mayor a 6, y con and
print(mi_bool)            #deben cumplirse ambas condiciones 
#tambien se puede usar and con strings
mi_bool2 = 10 == 10 and "gato" == "gato"
print(mi_bool2)

#condicion logica or
mi_bool3 = 5 == 4 or 3 < 6 #en este caso dara como resultado true esto debido que con or solo pide como requisito que se cumpla una 
print(mi_bool3 )           #condicion, en este caso es la segunda comparacion.

#condicion logica not
mi_bool4 = not "hola" == "hola" #lo que hace not es algo asi como una doble comparacion, "hola" es igual a "hola" pero con not esto 
print(mi_bool4)                 #daria falso debido a lo que esta haciendo es comprobar si NO es verdadero, lo cual es este caso es falso


#Otro dato es que estos operadores logicos tambien aplican con not in e in