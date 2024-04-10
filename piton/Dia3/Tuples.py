#Los tuples o tuplas son muy similares a las listas, la diferencia es que los datos dentro de un tuple son inmutables, en vez de 
#encerrarlos en corchetes se hace entre paretesis (no es necesario), otra cosa tambien es los tuples usan menos espacio que las listas.
mi_tuple = (1, 2, 3, 4)
print(type(mi_tuple))

#Se pueden meter listas, diccionarios u otras tuplas dentro de un tuple asi como ocurre tambien con los otros.

#Una manera de modificar un tuple es cambiar su tipo por el de una lista, tamben se puede hacer lo mismo con una lista pero viceversa
mi_tuple = list(mi_tuple)
print(type(mi_tuple))

#O puedes convertirlo a un tuple de nuevo
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

#Puedes asignar el contenido de un tuple a diferentes variables, siempre y cuando la cantidad de variables sea iguales a los valores
#del tuple
t = (1, 2, 3)
x,y,z = t
print(x,y,z)

#Metodos con los tuples:

#el largo del tuple, osea cuantos valores hay
print(len(t))

#contador, osea cuantas veces se repite un valor
print(t.count(1))

#Consultar el numero de indice
print(t.index(3))
