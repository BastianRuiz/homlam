class peliculas:
    titulo:str
    añoestreno:int
    director:str
    genero:str
    duracionmin:int
    visualizaciones:int

    def __init__(self, tit, año, direc, gen, duracion, visuali):
        self.titulo=tit
        self.añoestreno=año
        self.director=direc
        self.genero=gen
        self.duracionmin=duracion
        self.visualizaciones=visuali

    def mostrardetalles(self):
        detalle=f"""
        titulo de la pelicula: {self.titulo}
        año de estreno: {self.añoestreno}
        director: {self.director}
        genero de la pelicula: {self.genero}
        duracion en minutos de la pelicula: {self.duracionmin}
        visualizaciones a la fecha de la pelicula: {self.visualizaciones}"""
        
        return detalle
    
    def calcularpopularidad(self):
        popularidad = ""
        if self.duracionmin > 1:
            popularidad = f"la cantidad de visualizaciones es de {self.visualizaciones}"
        return popularidad 
    
    def antiguedadpelicula(self):
        calcularantiguedad = "Han transcurrido un total de 5 años"
        return calcularantiguedad
    
    def categorizarpelicula(self):
        categorizar = ""
        if self.añoestreno < 2020:
            categorizar = "pelicula reciente"
        
        elif self.añoestreno >= 2020 and self.añoestreno <= 2018:
            categorizar = "pelicula moderna"

        elif self.añoestreno > 2018 and self.añoestreno <= 2013:
            categorizar = "pelicula del recuerdo"

        elif self.añoestreno > 2013 and self.añoestreno <= 2003:
            categorizar = "pelicula clasica de los XXI"

        elif self.añoestreno > 2003:
            categorizar = "Gran clasico"
        return categorizar
    
Peliculas2 = peliculas("Hola", 2018, "Bastian", "Fantasia", 120, 50000)
print(Peliculas2.mostrardetalles())
print(Peliculas2.calcularpopularidad())
print(Peliculas2.antiguedadpelicula())
print(Peliculas2.categorizarpelicula())