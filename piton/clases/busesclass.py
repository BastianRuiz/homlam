#El dueño de una empresa de buses lo invita a desarrollar un programa que lleve el control de sus buses. Del bus se desea, patente,
#marca, cantidad de asientos, precio del pasaje, kilometros y año. El programa debe permitir ingresar buses, listar, verificar el
#kilometraje, siendo el bus menor a 100k nuevo, menor a 200k regular y superior a 200k viejo. Debe permitir mostrar cual es el total 
#que se puede ganar por bus, finalmente, saber cuantos años tiene el bus, crear menu de opciones.

class buses:
    patente:str
    marca:str
    asientos:int
    pasaje:int
    km:int
    año:int

    def __init__(self, pat, marca, asien, pasaje, km, año):
        self.patente = pat
        self.marca = marca
        self.asientos = asien
        self.pasaje = pasaje
        self.kilometraje = km
        self.año = año
    
    def verificarkm(self):
        tipo = ""
        if self.km <= 100000:
            tipo = "Bus nuevo"   
        elif self.km <= 200000:
            tipo = "Bus viejo"  
        return tipo
    
    def ganancia(self):
        total = self.asientos*self.pasaje
        return total
    
    def cantidadyear(self):
        cantidadA = 2023 - self.año
        return cantidadA
