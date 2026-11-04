# MODULO 4 - Reportes y estadisticas
# Todos los resultados se calculan con los datos guardados en las listas.

# Traemos lo que necesitamos de los otros archivos
from estructuras import POS_PRECIO, POS_CANTIDAD, POS_ACTIVO, buscar_posicion
from productos import listar_productos
from inventario import ver_stock_minimo


# ------------------------------------------------------
# FUNCIONES DE CALCULO (devuelven un resultado, no usan print)
# ------------------------------------------------------

def calcular_total_ingresos(ventas):
    # Suma el total de todas las ventas
    suma = 0
    for numero, fecha, subtotal, iva, total in ventas:
        suma = suma + total
    return suma


def calcular_valor_inventario(productos):
    # Suma precio x cantidad de los productos activos
    suma = 0
    for producto in productos:
        if producto[POS_ACTIVO]:
            suma = suma + (producto[POS_PRECIO] * producto[POS_CANTIDAD])
    return suma


def calcular_unidades_por_producto(detalle_ventas):
    # Devuelve dos listas: los codigos vendidos y las unidades vendidas de cada uno
    codigos = []
    unidades = []
    for numero_venta, codigo, cantidad, subtotal in detalle_ventas:
        posicion = buscar_posicion(codigos, codigo)
        if posicion == -1:
            codigos.append(codigo)
            unidades.append(cantidad)
        else:
            unidades[posicion] = unidades[posicion] + cantidad
    return codigos, unidades


def buscar_posicion_del_mayor(valores):
    # Devuelve la posicion del valor mas grande de la lista
    posicion_mayor = 0
    for i in range(len(valores)):
        if valores[i] > valores[posicion_mayor]:
            posicion_mayor = i
    return posicion_mayor


def calcular_ventas_por_mes(ventas):
    # Devuelve dos listas: los meses (AAAA-MM) y lo vendido en cada mes
    meses = []
    totales = []
    for numero, fecha, subtotal, iva, total in ventas:
        mes = fecha[0:7]  # ejemplo: 2026-10
        posicion = buscar_posicion(meses, mes)
        if posicion == -1:
            meses.append(mes)
            totales.append(total)
        else:
            totales[posicion] = totales[posicion] + total
    return meses, totales


def calcular_promedio(valores):
    suma = 0
    for valor in valores:
        suma = suma + valor
    return suma / len(valores)


# ------------------------------------------------------
# FUNCIONES QUE MUESTRAN LOS REPORTES
# ------------------------------------------------------

def mostrar_historial_ventas(ventas):
    print("\n--- HISTORIAL DE VENTAS ---")
    if len(ventas) == 0:
        print("No hay ventas")
    else:
        for numero, fecha, subtotal, iva, total in ventas:
            print("Venta", numero, "|", fecha, "| Subtotal:", subtotal, "| IVA:", iva, "| Total:", total)


def mostrar_total_ingresos(ventas):
    print("\n--- TOTAL DE INGRESOS ---")
    total_ingresos = calcular_total_ingresos(ventas)
    print("Total de ingresos: Q", round(total_ingresos, 2))


def mostrar_producto_mas_vendido(detalle_ventas):
    print("\n--- PRODUCTO MAS VENDIDO ---")
    if len(detalle_ventas) == 0:
        print("No hay ventas")
    else:
        codigos, unidades = calcular_unidades_por_producto(detalle_ventas)
        posicion_mayor = buscar_posicion_del_mayor(unidades)
        print("Codigo del producto:", codigos[posicion_mayor])
        print("Unidades vendidas:", unidades[posicion_mayor])


def mostrar_valor_inventario(productos):
    print("\n--- VALOR DEL INVENTARIO ---")
    valor_total = calcular_valor_inventario(productos)
    print("Valor total: Q", round(valor_total, 2))


def mostrar_promedio_ventas(ventas):
    print("\n--- PROMEDIO DE VENTAS POR MES ---")
    if len(ventas) == 0:
        print("No hay ventas")
    else:
        meses, totales = calcular_ventas_por_mes(ventas)
        for i in range(len(meses)):
            print("Mes", meses[i], ": Q", round(totales[i], 2))
        promedio = calcular_promedio(totales)
        print("Promedio por mes: Q", round(promedio, 2))


def menu_reportes(productos, ventas, detalle_ventas):
    opcion = ""
    while opcion != "8":
        print("\n=== REPORTES ===")
        print("1. Listado general de productos")
        print("2. Productos en stock minimo o menos")
        print("3. Historial de ventas")
        print("4. Total de ingresos")
        print("5. Producto mas vendido")
        print("6. Valor del inventario")
        print("7. Promedio de ventas por mes")
        print("8. Volver")
        opcion = input("Opcion: ")
        if opcion == "1":
            listar_productos(productos)
        elif opcion == "2":
            ver_stock_minimo(productos)
        elif opcion == "3":
            mostrar_historial_ventas(ventas)
        elif opcion == "4":
            mostrar_total_ingresos(ventas)
        elif opcion == "5":
            mostrar_producto_mas_vendido(detalle_ventas)
        elif opcion == "6":
            mostrar_valor_inventario(productos)
        elif opcion == "7":
            mostrar_promedio_ventas(ventas)
        elif opcion != "8":
            print("Opcion invalida")
