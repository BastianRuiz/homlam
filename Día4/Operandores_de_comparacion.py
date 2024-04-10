#Los operadores de comparacion son para determinar booleanos en este caso, es muy similar a lo que se vio en la clase tres, es 
#basicamente una continuacion, como ya sabemos esxisten varios tipos de operadores.

#En los siguientes ejemplos podemos ver que las variables declaradas no son el contenido que muestra al simple vista, son respuestas 
#booleanas que entregan si es que son verdaderas o falsas, osea que las variables pasan a ser true o false.

mi_var = 10 == 10.0 #funcionará igual siempre y cuando el resutado sea el mismo
print(mi_var)

otra_var = 10 + 10 == 30 - 10
print(otra_var)

var3 = 10 != 10.0
print(var3)

#Tambien se pueden comparar strings, se les pueden agregar condicionales como lower o upper.

string1 = "hola" == "adios"
print(string1)

string2 = "comoestas" == "Comoestas".lower()
print(string2)

