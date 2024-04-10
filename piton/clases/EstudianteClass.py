#Se desea registrar los datos de un estudiante de enseñanza superior, del estudiante se sabe, n° de matricula, nombre, email, edad,
#promedio, arancel, gratuidad. Generar el ingreso de datos, desde otro archivo. La clase debe poder listar los datos, verificar si es 
#mayor de edad, verificar si posee gartuidad, en caso de no poseer, aplicar beca , segun arancel (si vale 1000000,)

class Estudiante:
    matricula:int
    email:str
    edad:int
    gratuidad:bool
    arancel:int
    promedio:float

#metodo constructor(_init_) con parametros de entrada
    def __init__(self, mat, nombre, mail, edad, grat, aran, prom):
        self.matricula = mat
        self.nombre = nombre
        self.email = mail
        self.edad = edad
        self.gratuidad = grat
        self.arancel = aran
        self.promedio = prom

    def listar(self):
        grat = ''
        if self.gratuidad: #es igual a self.gratuidad == true
            grat = 'si'
        else:
            grat = 'no'

        info = f"""
        n° matricula: {self.matricula}
        nombre: {self.nombre}
        email: {self.email}
        gratuidad: {grat}
        arancel: {self.arancel}
        promedio: {self.promedio}
        """
        return info
    
    def verificaredad(self):
        if self.edad >= 18:
            return "Mayor de edad"
        return "menor de edad"
    
    def verificargratuidad(self):
        if self.gratuidad:
            return f"{self.nombre} tiene gratuidad"
        return f"{self.nombre} no tiene gratuidad"
    
    def modificarpromedio(self, prom):
        self.promedio = prom
        return "su promedio a sido modificado con exito"
    
    def beca(self):
        if not self.gratuidad: #self.gratuidad == false
            descuento = 0
            if self.arancel == 1000000:
                descuento = self.arancel*0.03
            elif self.arancel > 1000000 and self.arancel <= 1500000:
                descuento = self.arancel*0.05
            elif self.arancel > 1500000:
                descuento = self.arancel*0.1
            return descuento
        


    



