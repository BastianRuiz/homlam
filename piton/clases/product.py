#Crear la clase Producto, de esta clase se sabe, nombre producto, precio de compra del producto, precio de venta del producto,
#stock del producto y descripcion. Se necesita poder ingresar los datos del producto, mostrar todos los datos, metodo que permita
#ver la utilidad del producto, metodo que permita mostrar el precio de venta con iva.
#Generar menu con opciones.

class producto:
    nombrep:str
    preciocompra:int
    precioventa:int
    stockp:int
    descrip:str

    def __init__(self, nom, com, ven, stock, des):
        self.nombrep = nom
        self.preciocompra = com
        self.precioventa = ven
        self.stockp = stock
        self.descrip = des

    def datosproduc(self):
        datos = f"""
        nombre del producto = {self.nombrep}
        precio de compra = {self.preciocompra}
        precio de venta = {self.precioventa}
        stock del producto = {self.stockp}
        descripción del producto = {self.descrip}"""
        return datos
    
    def ventaiva(self):
        iva = self.precioventa*0.10
        print(f"el precio total es: {iva}")
        return iva
    
    def agregardescrip(self):
        descripcion = self.descrip
        return descripcion
        
    

        
        
