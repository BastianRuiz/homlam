class persona:
    run:str
    nombre:str
    email:str
    edad:int

    def __init__(self, run, name, email, edad):
        self.run = run
        self.nombre = name
        self.email = email
        self.edad = edad

    def MostrarDatosPersona(self):
        losdatos = f"""
        run: {self.run}
        nombre: {self.nombre}
        email: {self.email}
        edad: {self.edad}
        """
        return losdatos

    def mayoredad(self):
        mensaje = ""
        if self.edad >=18:
            mensaje = "es mayor de edad"
        else:
            mensaje = "es menor de edad"

        return mensaje

persona1 = persona("21.744.095-5", "Bastian", "pxlnoz@gmail.com", 18)
print(persona1.MostrarDatosPersona())
print(persona1.mayoredad())



