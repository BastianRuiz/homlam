#En una lista se pueden almacenar diferentes tipos de datos tales como: strings, enteros, flotantes, todas estas juntas e incluso otras
#listas, los valores dentro de esta van entre corchetes [].
Mi_lista = ["a", "b", "c"]
print(type(Mi_lista))

#Se pueden usar indexaciones y concatenaciones.
Otra_lista = [1, 2, 3]
print(Otra_lista[1])
Otra_lista2 = [4, 5, 6]
print(Otra_lista + Otra_lista2)

#Las listas son modificables, se pueden agregar, reemplazar, eliminar, etc, los datos.

#Reemplazar:
Mi_lista[0] = "z"
print(Mi_lista)

#Agregar:
Mi_lista.append("d")
print(Mi_lista)

#Eliminar:
Mi_lista.pop()  #Si no se especifica el parametro que se desea eliminar dentro del parentesis automaticamente borrará el último
print(Mi_lista)
popeado = Mi_lista.pop(0) #Se puede guardar el elemento eliminado en una variable por si se desea, al colocar un index dentro de pop 
print(popeado)            #no es necesesario colocarlo entre corchetes

#Ordenar:
Nueva_Lista = [1, 3, 6, 7, 2]
Nueva_Lista.sort()
print(Nueva_Lista)
#El sort sirve para poder ordenar una lista numerica o alfabeticamente, no se puede crear una nueva
##variable para guardar la lista ya previamente ordenada, esto debido a que el tipo de dato no Noone, osea que no posee nada en lo 
#absoluto, osea que no es necesario el crear una nueva variable, ya una vez usado de sort la lista ya abrá sido modificada.

#Reversa:
Nueva_Lista.reverse()
print(Nueva_Lista) #Esto da vuelta los datos, como un espejo



