from CertamenClases import peliculas

tit = input("El titulo de la pelicula es: ")
año = int(input("El año de estreno de la pelicula es: "))
direc = input("El director de la pelicula es: ")
gen = input("El genero de la pelicula es: ")
dura = int(input("La duracion de la pelicula en minutos es: "))
visuali = int(input("La cantidad de visualizaciones de la pelicula es: "))

pelis = peliculas(tit, año, direc, gen, dura, visuali)

def MostrarDetalles():
    detalles = f"""
    {tit}
    {año}
    {direc}
    {gen}
    {dura}
    {visuali}"""
    return detalles

print(pelis.titulo)
print(pelis.visualizaciones)
cat = pelis.categorizarpelicula()
print(f"La pelicula {tit} tiene x años y esta categorizada como {cat}")  