# MODULO 3 - Control de inventarios
# Existencias, entradas de mercancia, stock minimo e historial de movimientos.

# Traemos lo que necesitamos del archivo estructuras.py
from estructuras import POS_CODIGO, POS_NOMBRE, POS_CANTIDAD, POS_STOCK_MINIMO
from estructuras import pedir_entero, buscar_producto, registrar_movimiento


def esta_en_stock_minimo(producto):
    # Devuelve True si la existencia es igual o menor que el stock minimo
    return producto[POS_CANTIDAD] <= producto[POS_STOCK_MINIMO]


def ver_existencias(productos):
    print("\n--- EXISTENCIAS ---")
    if len(productos) == 0:
        print("No hay productos")
    else:
        for producto in productos:
            print(producto[POS_CODIGO], "|", producto[POS_NOMBRE], "| Cantidad:", producto[POS_CANTIDAD])


def registrar_entrada(productos, movimientos, fecha):
    print("\n--- ENTRADA DE INVENTARIO ---")
    codigo = input("Codigo: ")
    posicion = buscar_producto(productos, codigo)
    if posicion == -1:
        print("El producto no existe")
    else:
        cantidad = pedir_entero("Cantidad que entra: ")
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que 0")
        else:
            descripcion = input("Descripcion: ")
            productos[posicion][POS_CANTIDAD] = productos[posicion][POS_CANTIDAD] + cantidad
            registrar_movimiento(movimientos, fecha, codigo, "ENTRADA", cantidad, descripcion)
            print("Entrada registrada. Nueva cantidad:", productos[posicion][POS_CANTIDAD])


def ver_stock_minimo(productos):
    print("\n--- PRODUCTOS CON STOCK MINIMO ---")
    hay_alertas = False
    for producto in productos:
        if esta_en_stock_minimo(producto):
            print(producto[POS_CODIGO], "|", producto[POS_NOMBRE], "| Cantidad:",
                  producto[POS_CANTIDAD], "| Minimo:", producto[POS_STOCK_MINIMO])
            hay_alertas = True
    if not hay_alertas:
        print("Ningun producto llego al stock minimo")


def ver_movimientos(movimientos):
    print("\n--- HISTORIAL DE MOVIMIENTOS ---")
    if len(movimientos) == 0:
        print("No hay movimientos")
    else:
        for fecha, codigo, tipo, cantidad, descripcion in movimientos:
            print(fecha, "|", codigo, "|", tipo, "|", cantidad, "|", descripcion)


def menu_inventario(productos, movimientos, fecha):
    opcion = ""
    while opcion != "5":
        print("\n=== INVENTARIO ===")
        print("1. Ver existencias")
        print("2. Registrar entrada")
        print("3. Productos en stock minimo")
        print("4. Historial de movimientos")
        print("5. Volver")
        opcion = input("Opcion: ")
        if opcion == "1":
            ver_existencias(productos)
        elif opcion == "2":
            registrar_entrada(productos, movimientos, fecha)
        elif opcion == "3":
            ver_stock_minimo(productos)
        elif opcion == "4":
            ver_movimientos(movimientos)
        elif opcion != "5":
            print("Opcion invalida")
