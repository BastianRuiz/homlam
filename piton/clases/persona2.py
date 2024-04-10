class persona2:
    rut:str
    nombre:str
    edad:int
    email:str

    def __init__(self, rut, nom, edad, email):
        self.rut = rut
        self.nombre =  nom
        self.edad = edad
        self.email = email

    def mostrardatos(self):
        datos = f"""
        rut: {self.rut}
        nombre: {self.nombre}
        edad: {self.edad}
        email: {self.email}"""
        
        return datos  

    def mayorde18(self):
        mayor = ""
        if self.edad >= 18:
            mayor = "es mayor de edad"

        else:
            mayor = "es menor de edad"

        return mayor
    
pelsona = persona2("21744095-5", "Bastian", 18, "pxlnoz@gmail.com")
print(pelsona.mostrardatos())
print(pelsona.mayorde18())

            
            

    


    

