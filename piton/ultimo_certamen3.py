def mostrar_precio_fruta():
    # Tabla de precios de frutas
    precios_frutas = {"Platano": 1020, "Frutilla": 2400, "Palta": 3500, "Naranja":990}

    # Solicitar al usuario la fruta y la cantidad de kilos
    fruta = input("Ingrese el nombre de la fruta: ")
    cantidad_kilos = int(input("Ingrese la cantidad de kilos de la fruta: "))

    # Verificar si la fruta está en el diccionario
    if fruta in precios_frutas:
        precio_total = precios_frutas[fruta] * cantidad_kilos
        print(f"El precio de {cantidad_kilos} kilos de {fruta} es: ${precio_total}.")
    else:
        print("La fruta ingresada no está en la lista de precios.")



mostrar_precio_fruta()
