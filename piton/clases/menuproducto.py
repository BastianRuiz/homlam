from product import producto

nom = input("nombre del producto: ")
com = int(input("precio compra: "))
ven = int(input("precio venta: "))
stock = int(input("stock: "))
des = input("descripcion  del producto: ")

prod = producto(nom, com, ven, stock, des)

print(prod.datosproduc())
print(prod.ventaiva())
print(prod.agregardescrip())
