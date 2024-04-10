def mostrar_lista(paises, capitales):
    for i in range(len(paises)):
        print(f"{paises[i]} - {capitales[i]}")

def buscar(paises, capitales, busqueda):
    for i in range(len(paises)):
        if busqueda in paises[i] or busqueda in capitales[i]:
            print(f"País: {paises[i]}, Capital: {capitales[i]}")

def modificar(paises, capitales, busqueda):
    for i in range(len(paises)):
        if busqueda in paises[i]:
            nuevo_pais = input("Ingrese el nuevo país: ")
            nuevo_capital = input("Ingrese la nueva capital: ")
            paises[i] = nuevo_pais
            capitales[i] = nuevo_capital
            print("País y capital actualizados.")
            break

def deletrear(capital):
    for letra in capital:
        print(letra)

def saltear(paises, capitales, pais):
    index = paises.index(pais)
    print("Saltando...")
    print(f"País: {paises[index]}, Capital: {capitales[index]}")

# Lista inicial de países y capitales
paises = ["España", "Francia", "Alemania", "Italia", "Reino Unido"]
capitales = ["Madrid", "París", "Berlín", "Roma", "Londres"]

# Agregar 5 países y capitales más introducidos por el usuario
for i in range(5):
    pais = input("Ingrese un país: ")
    capital = input("Ingrese la capital: ")
    paises.append(pais)
    capitales.append(capital)

# Mostrar lista inicial
mostrar_lista(paises, capitales)

# Búsqueda por país o capital
busqueda = input("Ingrese el país o la capital que desea buscar: ")
buscar(paises, capitales, busqueda)

# Modificar país y capital
modificacion = input("Ingrese el país que desea modificar: ")
modificar(paises, capitales, modificacion)
mostrar_lista(paises, capitales)

# Deletrear la capital
capital_buscar = input("Ingrese el país del cual quiere deletrear la capital: ")
index = paises.index(capital_buscar)
deletrear(capitales[index])

# Saltear país con su capital
pais_saltear = input("Ingrese el país que quiere saltar: ")
saltear(paises, capitales, pais_saltear)
