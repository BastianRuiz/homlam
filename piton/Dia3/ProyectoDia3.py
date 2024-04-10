text = input("Ingrese un texto cualquiera: ").lower()

print("Ingrese 3 letras de su eleccion")
letra1 = input("Ingrese la primera letra: ").lower()
letra2 = input("Ingrese la segunda letra: ").lower()
letra3 = input("Ingrese la tercera letra: ").lower()

listaletras = [letra1, letra2, letra3]

print("1.- ¿cuántas veces aparece cada una de las letras que eligió en el texto?")
print(f"la primera letra aparece un total de {text.count(listaletras[0])} veces")
print(f"la segunda letra aparece un total de {text.count(listaletras[1])} veces")
print(f"la tercera letra aparece un total de {text.count(listaletras[2])} veces")

print("2.- cuántas palabras hay a lo largo de todo el texto?")
print(len(text))

print("3.- cuál es la primera letra del texto y cuál es la última?")
print(f"la primera letra del texto es: {text[0]}")
print(f"la ultima letra del texto es: {text[-1]}")

print("4.-  cómo quedaría el texto si invirtiéramos el orden de las palabras?")
print(text[::-1])

print("5.- el sistema nos va a decir si la palabra “Python” se encuentra dentro del texto")
que = "Pyhton" in text

print(f"Se encuentra la palabra 'Python' dentro del texto?: {que}")



