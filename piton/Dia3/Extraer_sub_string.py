#extraer la palabra controlar con slicing
frase = "Controlar la complejidad es la esencia de la programación"

resultado = frase[0:9]
print(resultado)
#lo primero es colocar el indice y luego lo largo de la frase
#----------

#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

caracter = frase[9::3]
print(caracter)
#----------

#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

inverso = frase[::-1]
print(inverso)
#No se pq chucha esto invierte las weas pero el caso es que lo hace

