def calificaciones() :

    cantidad_alumnos = (input("presione 'S' desea analizar notas de alumnos: "))
    cantidad_alumnos = "S".lower

    Ingresar_calificación = int(input("Ingrese la calificación de este alumno: "))


    if Ingresar_calificación >= 4:
            print("Aprobado")

    else:
            print("reprobado")

    return cantidad_alumnos


    

calificaciones()



    