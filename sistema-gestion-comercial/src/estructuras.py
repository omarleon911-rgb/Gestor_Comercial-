# estructuras.py
# Constantes y funciones que usan todos los modulos del sistema.

# ------------------------------------------------------
# CONSTANTES
# ------------------------------------------------------

TASA_IVA = 0.12

# Un producto es una lista con estos datos, en este orden:
# [codigo, nombre, categoria, precio, cantidad, stock_minimo, activo]
# activo es True si se puede vender y False si esta desactivado
POS_CODIGO = 0
POS_NOMBRE = 1
POS_CATEGORIA = 2
POS_PRECIO = 3
POS_CANTIDAD = 4
POS_STOCK_MINIMO = 5
POS_ACTIVO = 6

# Las otras listas guardan registros asi:
# venta:      [numero, fecha, subtotal, iva, total]
# detalle:    [numero_venta, codigo, cantidad, subtotal]
# movimiento: [fecha, codigo, tipo, cantidad, descripcion]
# item del carrito: [codigo, nombre, cantidad, precio, subtotal]


# ------------------------------------------------------
# FUNCIONES PARA PEDIR DATOS
# ------------------------------------------------------

def pedir_entero(mensaje):
    # Pide un numero entero que no sea negativo y lo devuelve
    numero = -1
    while numero < 0:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Error: no puede ser negativo")
        except ValueError:
            print("Error: escriba un numero entero")
    return numero


def pedir_decimal(mensaje):
    # Pide un numero con decimales que no sea negativo y lo devuelve
    numero = -1.0
    while numero < 0:
        try:
            numero = float(input(mensaje))
            if numero < 0:
                print("Error: no puede ser negativo")
        except ValueError:
            print("Error: escriba un numero")
    return numero


def pedir_fecha():
    # Pide la fecha de hoy con el formato AAAA-MM-DD y la devuelve
    fecha = ""
    while len(fecha) != 10:
        fecha = input("Escriba la fecha de hoy (AAAA-MM-DD): ")
        if len(fecha) != 10:
            print("Error: use el formato AAAA-MM-DD")
    return fecha


# ------------------------------------------------------
# FUNCIONES DE BUSQUEDA Y REGISTRO
# ------------------------------------------------------

def buscar_producto(productos, codigo):
    # Devuelve la posicion del producto en la lista, o -1 si no existe
    for i in range(len(productos)):
        if productos[i][POS_CODIGO] == codigo:
            return i
    return -1


def buscar_posicion(lista, valor):
    # Devuelve la posicion de un valor dentro de una lista, o -1 si no esta
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1


def registrar_movimiento(movimientos, fecha, codigo, tipo, cantidad, descripcion):
    # Agrega un movimiento de inventario (ENTRADA o SALIDA) al historial
    movimientos.append([fecha, codigo, tipo, cantidad, descripcion])
