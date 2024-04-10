texto = "Esto Es Un Texto De Prueba"
print(texto)

#Upper: se usa para transformar el texto en mayuscula, de igual manera dentro de corchetes despues del texto puedes eleguir 
#el indice que desees transformar
print(texto[1].upper())

#Lower: se usa para transformar el texto en minuscula, de igual manera dentro de corchetes despues del texto puedes eleguir 
#el indice que desees transformar
print(texto.lower())


#Split: separa los elementos y los guarda en una lista, las listas estan dentro de corchetes, dentro del parentesis podemos escribir la
#palabra o el texto que dessemos para colocarlo como separador
print(texto.split())

#Join: puede unir variables y crear listas, dependiendo de lo que coloquemos dentro de las comillas estas actuaran como separador, si no
#colocamos nada estara todo junto
a = "Aprender"
b = "Python"
c = "es"
d = "genial"

e = " ".join([a, b, c, d])
print(e)

#Find: es casi igual al metodo index, busca el indice dependiendo el caracter que le indiquemos, la diferencia con index es que si se 
#coloca un caracter que no existe, en vez de salir un error, saldra un -1
print(texto.find("z"))

#Replace: sirve para remplazar texto
print(texto.replace("Esto", "This"))

#Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra 
#en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
a = lista_palabras[0]
b = lista_palabras[1]
c = lista_palabras[2]
d = " ".join([a, b, c])
print(d)


#Se usan .() pq son todos condicionales


