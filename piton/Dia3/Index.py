#mediante el uso de [] podemos saber en cual indice esta cada palabra, el primer caracter siempre sera 0, por ende si colocamos un 
#numero negativo este lo tomara de derecha a izquierda empezando por -1, colocando el indice se sabe la posicion del caracter al 
#se está refiriendo
texto = "esto es una prueba \n"
resultado = texto[-1]
print(resultado)

#----------

#con el codigo .index colocando una letra x se podra saber el indice de esta, si es una palabra completa, se detectara de donde empieza
#esta palabra, tambien podemos colocar de donde quiero empezar a detectar el indice de una palabra especifica colocando una coma y un
#numero de esta, y hasta que indice se desea buscar colocando otra coma y numero, OJO que empieza a detectar un numero antes del
#buscado
mi_texto = "esto es una prueba"
mi_resultado = mi_texto.index("una")
print(mi_resultado)

el_resultado = mi_texto.index("e", 1, 10)
print(el_resultado)

#----------

#la unica diferencia con .rindex es que empieza a buscar de derecha a izquierda
texto = "esto es una prueba"
resultado = texto.rindex("a")
print(resultado)

#En resumen la indexizacion sirve para saber la posicion o indice de lo buscado.

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper)