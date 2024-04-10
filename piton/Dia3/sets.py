#Los sets son parecidos a los ya vistos anteriormente, se puede llamar utilizando la palabra clave set([]) o solo colocando llaves{},
#la diferencia con los diccionarios es que en los sets solo se pueden agregar valores unicos, osea que si colocas un valor repetido 
#python lo descartará automaticamente, y no hay que preocuparse para saber si uno es un set o un diccionario ya que la metodología de 
#ambos es distinta. No existe la indexizacion, los valores son imnutables y no se pueden agregar otras weas como listas, diccionarios,etc.

mi_set = {1, "hola", 2, "como", 3, "estas"}
print(type(mi_set)) 

#Union de sets, se selecciona el set.union(aqui va el set con el que lo quieres unir)
set1 = {1, 2, 3}
set2 = {4, 5 ,6}
set3 = set1.union(set2)
print(set3)

#symmetric_difference(set) retorna todos los valores de 2 sets excepto los que tienen en común
set4 = set1.symmetric_difference(set3)
print(set4)

#Agregar valores al set, se hace con .add()
set1.add(4)
print(set1)

#eliminar valor, se hace con remove()
set2.remove(5)
print(set2)

#limpiar el set, limpia el set seleccionado con .clear()
set3.clear()
print(set3)

