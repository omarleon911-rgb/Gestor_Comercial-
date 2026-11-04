# PROGRAMA PRINCIPAL
# Para ejecutarlo todos los archivos .py deben estar en la misma carpeta.
#
#   estructuras.py        -> constantes y funciones que usan todos
#   productos.py          -> Modulo 1: gestion de productos
#   ventas.py             -> Modulo 2: registro de ventas
#   inventario.py         -> Modulo 3: control de inventarios
#   reportes.py           -> Modulo 4: reportes y estadisticas

# Traemos las funciones que necesitamos de cada archivo
from estructuras import pedir_fecha
from productos import menu_productos
from ventas import registrar_venta
from inventario import menu_inventario
from reportes import menu_reportes

# Las listas donde se guardan todos los datos mientras el programa esta abierto
productos = []
ventas = []
detalle_ventas = []
movimientos = []

fecha_hoy = pedir_fecha()

opcion = ""
while opcion != "5":
    print("\n===== SISTEMA COMERCIAL =====")
    print("1. Productos")
    print("2. Ventas")
    print("3. Inventario")
    print("4. Reportes")
    print("5. Salir")
    opcion = input("Opcion: ")
    if opcion == "1":
        menu_productos(productos, movimientos, fecha_hoy)
    elif opcion == "2":
        registrar_venta(productos, ventas, detalle_ventas, movimientos, fecha_hoy)
    elif opcion == "3":
        menu_inventario(productos, movimientos, fecha_hoy)
    elif opcion == "4":
        menu_reportes(productos, ventas, detalle_ventas)
    elif opcion == "5":
        print("Adios")
    else:
        print("Opcion invalida")
