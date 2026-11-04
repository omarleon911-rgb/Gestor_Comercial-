# MODULO 1 - Gestion de productos
# Registrar, consultar, listar, modificar y desactivar productos.

# Traemos lo que necesitamos del archivo estructuras.py
from estructuras import POS_NOMBRE, POS_CATEGORIA, POS_PRECIO, POS_STOCK_MINIMO, POS_ACTIVO
from estructuras import pedir_entero, pedir_decimal, buscar_producto, registrar_movimiento


def registrar_producto(productos, movimientos, fecha):
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Codigo: ")
    if codigo == "":
        print("Error: el codigo no puede estar vacio")
    elif buscar_producto(productos, codigo) != -1:
        print("Error: ese codigo ya existe")
    else:
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        precio = pedir_decimal("Precio de venta: ")
        cantidad = pedir_entero("Cantidad disponible: ")
        stock_minimo = pedir_entero("Stock minimo: ")
        productos.append([codigo, nombre, categoria, precio, cantidad, stock_minimo, True])
        if cantidad > 0:
            registrar_movimiento(movimientos, fecha, codigo, "ENTRADA", cantidad, "Inventario inicial")
        print("Producto registrado")


def mostrar_producto(producto):
    codigo, nombre, categoria, precio, cantidad, stock_minimo, activo = producto
    print("Codigo:", codigo)
    print("Nombre:", nombre)
    print("Categoria:", categoria)
    print("Precio:", precio)
    print("Cantidad:", cantidad)
    print("Stock minimo:", stock_minimo)
    if activo:
        print("Estado: Activo")
    else:
        print("Estado: Desactivado")


def consultar_producto(productos):
    print("\n--- CONSULTAR PRODUCTO ---")
    codigo = input("Codigo: ")
    posicion = buscar_producto(productos, codigo)
    if posicion == -1:
        print("El producto no existe")
    else:
        mostrar_producto(productos[posicion])


def listar_productos(productos):
    print("\n--- LISTADO DE PRODUCTOS ---")
    if len(productos) == 0:
        print("No hay productos")
    else:
        for codigo, nombre, categoria, precio, cantidad, stock_minimo, activo in productos:
            if activo:
                estado = "Activo"
            else:
                estado = "Desactivado"
            print(codigo, "|", nombre, "|", categoria, "| Precio:", precio,
                  "| Cantidad:", cantidad, "| Minimo:", stock_minimo, "|", estado)


def modificar_producto(productos):
    print("\n--- MODIFICAR PRODUCTO ---")
    codigo = input("Codigo: ")
    posicion = buscar_producto(productos, codigo)
    if posicion == -1:
        print("El producto no existe")
    else:
        print("1. Nombre")
        print("2. Categoria")
        print("3. Precio")
        print("4. Stock minimo")
        opcion = input("Que quiere modificar? ")
        if opcion == "1":
            productos[posicion][POS_NOMBRE] = input("Nuevo nombre: ")
            print("Listo")
        elif opcion == "2":
            productos[posicion][POS_CATEGORIA] = input("Nueva categoria: ")
            print("Listo")
        elif opcion == "3":
            productos[posicion][POS_PRECIO] = pedir_decimal("Nuevo precio: ")
            print("Listo")
        elif opcion == "4":
            productos[posicion][POS_STOCK_MINIMO] = pedir_entero("Nuevo stock minimo: ")
            print("Listo")
        else:
            print("Opcion invalida")


def desactivar_producto(productos):
    print("\n--- DESACTIVAR PRODUCTO ---")
    codigo = input("Codigo: ")
    posicion = buscar_producto(productos, codigo)
    if posicion == -1:
        print("El producto no existe")
    else:
        productos[posicion][POS_ACTIVO] = False
        print("Producto desactivado")


def menu_productos(productos, movimientos, fecha):
    opcion = ""
    while opcion != "6":
        print("\n=== PRODUCTOS ===")
        print("1. Registrar producto")
        print("2. Consultar producto")
        print("3. Listado de productos")
        print("4. Modificar producto")
        print("5. Desactivar producto")
        print("6. Volver")
        opcion = input("Opcion: ")
        if opcion == "1":
            registrar_producto(productos, movimientos, fecha)
        elif opcion == "2":
            consultar_producto(productos)
        elif opcion == "3":
            listar_productos(productos)
        elif opcion == "4":
            modificar_producto(productos)
        elif opcion == "5":
            desactivar_producto(productos)
        elif opcion != "6":
            print("Opcion invalida")
