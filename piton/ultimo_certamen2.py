# 1: crear una tupla llamada venta
venta = ("Producto Ejemplo", 3, 10.5)

# 2: Crear una lista llamada registro_venta que almacene múltiples tuplas de ventas
registro_venta = ("Producto1", 5, 12.5), ("Producto2", 2, 20.0), ("Producto3", 7, 8.75), ("Producto4", 1, 5.0), ("Producto5", 10, 15.0)


# 3: Función para calcular el total recaudado en el día
def total_venta(registro_venta):
    total = 0
    for venta in registro_venta:
        total += venta[1] * venta[2]
    return total

# 4: Función para encontrar el producto más vendido
def producto_mas_vendido(registro_venta):
    mas_vendido = ""
    max_cantidad = 0
    for venta in registro_venta:
        if venta[1] > max_cantidad:
            max_cantidad = venta[1]
            mas_vendido = venta[0]
    return mas_vendido

# 5: Función para calcular el precio unitario promedio de todos los productos vendidos
def promedio_precio_unitario(registro_venta):
    total_productos = len(registro_venta)
    total_precios = sum(venta[2] for venta in registro_venta)
    promedio = total_precios / total_productos
    return promedio

# 6: Función para obtener la cantidad total vendida y el monto total recaudado por un producto específico
def venta_producto(registro_venta, nombre_producto):
    cantidad_total_vendida = 0
    monto_total_recaudado = 0
    for venta in registro_venta:
        if venta[0] == nombre_producto:
            cantidad_total_vendida += venta[1]
            monto_total_recaudado += venta[1] * venta[2]
    return cantidad_total_vendida, monto_total_recaudado

# Ejemplo de uso:
print("Monto total recaudado en el día:", total_venta(registro_venta))
print("Producto más vendido:", producto_mas_vendido(registro_venta))
print("Precio unitario promedio:", promedio_precio_unitario(registro_venta))
nombre_producto = "Producto3"
cantidad_vendida, monto_recaudado = venta_producto(registro_venta, nombre_producto)
print(f"Producto '{nombre_producto}' - Cantidad vendida: {cantidad_vendida}, Monto recaudado: {monto_recaudado}")

