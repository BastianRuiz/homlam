#Los diccionarios tienen una "palabra clave" la cual posee un valor, los diccionarios se hacen entre llaves{} y la posición de la clave
#es irrelevante puesto que los diccionarios no tienen índice.
diccionario = {"c1":"valor1", "c2":"valor2", "c3":"valor3"}
print(diccionario)
a = diccionario["c1"]
print(a)

#otro ejemplo mas realista:
cliente = {"nombre":"Bastian", "apellido":"Ruiz", "peso":60, "altura": 1.64}
print(cliente["peso"])

#Se pueden meter otras cosas dentro de diccionarios, como por ejemplo listas y otros diccionarios:
dic = {"a":123, "lista":["hola", "como", "estas"], "otrodic":{"x":"bien", "y":"gracias", "z":"adios"}}
print(dic["otrodic"]["z"])

#ejercicio, muestra en pantalla la "e" pero en mayuscula de el siguiente diccionario, todo en una sola linea:
diccionario2 = {"c1":["a", "b", "c"], "c2":["d","e","f"]}
print(diccionario2["c2"][1].upper())

#agregar al diccionario:
diccionario3 = {1:"a", 2:"b"}
diccionario3[3] = "c"
print(diccionario3)

#Sobreescribir:
diccionario3[2] = "tuputamadre"
print(diccionario3)

#otros metodos para diccionarios:

#mostrar solo claves:
print(diccionario3.keys())
#mostrar solo valores:
print(diccionario3.values())
#mostrar todos los elementos por separado:
print(diccionario3.items())

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["pais"] = "Colombia"
print(mi_dic)

#NOTA: Siempre que nos refiramos a una clave debemos de colocarlo entre corchetes, ya sea para reeemplazar o agregar un valor.