#se define la clase
class auto:
    #atributos de la calse
    patente:str
    marca:str
    modelo:str
    precio:int
    color:str
    year:int

    #definir un constructor(metodo que tienen todas las clases)
    def __init__(self, pat, marca, model, precio, color, year):
        self.patente = pat
        self.marca = marca
        self.modelo = model 
        self.precio = precio 
        self.color = color 
        self.year = year

    
    #metodo que permite mostrar el objeto de la clase
    def __str__(self):
        return f"Patente: {self.patente}"
    
    def mostrardatos(self):
        datos = f"""
        Patente: {self.patente}
        Marca: {self.marca}
        modelo: {self.modelo}
        precio: {self.precio}
        color: {self.color}
        año: {self.year}
        """
        return datos

#Instanciar la clase, crear un objeto que permita acceder a sus atributos y metodos
auto1 = auto('abcd12', 'fiat', 'uno', 20000, 'verder', 2010)
print(auto1)

#Llamar metodo mostrar datos
print(auto1.mostrardatos())


#Atributos: 
# NombreAtributo: tipo de dato

#Metodos:
#def__init__
#self. : permite acceder a metodos 

#-------------------------------------------------------

