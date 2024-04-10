#los strings como tal son inmutables.

#se pueden hacer saltos de linea como en siguiente ejemplo:
frase = """hola como
estas, yo estoy
muy bien"""
print(frase)

#se puede buscar una palabra escrita dentro una variable, la cual te respondera con una respuesta booleana:
print("hola" in frase)

#tambien se puede preguntar si no esta determinada palabra:
print("hola" not in frase)

#preguntar que tan largo es frase, osea preguntar la cantidad de caracteres dentro de este:
print(len(frase))
