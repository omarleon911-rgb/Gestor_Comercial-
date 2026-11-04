# MODULO 2 - REGISTRO DE VENTAS

def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_iva(subtotal):
    return subtotal * TASA_IVA


def calcular_total(subtotal, iva):
    return subtotal + iva


def calcular_subtotal_general(carrito):
    suma = 0
    for codigo, nombre, cantidad, precio, subtotal in carrito:
        suma = suma + subtotal
    return suma


def calcular_cantidad_en_carrito(carrito, codigo_buscado):
    unidades = 0
    for codigo, nombre, cantidad, precio, subtotal in carrito:
        if codigo == codigo_buscado:
            unidades = unidades + cantidad
    return unidades


def calcular_numero_venta(ventas):
    return len(ventas) + 1


def llenar_carrito(productos):
    carrito = []
    codigo = "x"
    while codigo != "":
        codigo = input("Codigo del producto (ENTER para terminar): ")
        if codigo != "":
            posicion = buscar_producto(productos, codigo)
            if posicion == -1:
                print("Error: el producto no existe")
            elif not productos[posicion][POS_ACTIVO]:
                print("Error: el producto esta desactivado")
            else:
                cantidad = pedir_entero("Cantidad: ")
                en_carrito = calcular_cantidad_en_carrito(carrito, codigo)
                disponible = productos[posicion][POS_CANTIDAD]
                if cantidad <= 0:
                    print("Error: la cantidad debe ser mayor que 0")
                elif cantidad + en_carrito > disponible:
                    print("Error: no hay suficiente inventario. Disponible:", disponible)
                else:
                    nombre = productos[posicion][POS_NOMBRE]
                    precio = productos[posicion][POS_PRECIO]
                    subtotal = calcular_subtotal(precio, cantidad)
                    carrito.append([codigo, nombre, cantidad, precio, subtotal])
                    print("Agregado. Subtotal del producto:", subtotal)
    return carrito


def mostrar_resumen_venta(numero, carrito, subtotal_general, iva, total):
    print("\n--- VENTA No.", numero, "---")
    for codigo, nombre, cantidad, precio, subtotal in carrito:
        print(nombre, "x", cantidad, "= Q", subtotal)
    print("Subtotal: Q", round(subtotal_general, 2))
    print("IVA 12%: Q", round(iva, 2))
    print("Total: Q", round(total, 2))


def descontar_inventario(productos, carrito):
    for codigo, nombre, cantidad, precio, subtotal in carrito:
        posicion = buscar_producto(productos, codigo)
        productos[posicion][POS_CANTIDAD] = productos[posicion][POS_CANTIDAD] - cantidad


def guardar_detalle_venta(detalle_ventas, movimientos, fecha, numero, carrito):
    for codigo, nombre, cantidad, precio, subtotal in carrito:
        detalle_ventas.append([numero, codigo, cantidad, subtotal])
        registrar_movimiento(movimientos, fecha, codigo, "SALIDA", cantidad, "Venta No. " + str(numero))


def registrar_venta(productos, ventas, detalle_ventas, movimientos, fecha):
    print("\n--- REGISTRAR VENTA ---")
    carrito = llenar_carrito(productos)

    if len(carrito) == 0:
        print("No se agrego nada. Venta cancelada")
    else:
        subtotal_general = calcular_subtotal_general(carrito)
        iva = calcular_iva(subtotal_general)
        total = calcular_total(subtotal_general, iva)
        numero = calcular_numero_venta(ventas)

        mostrar_resumen_venta(numero, carrito, subtotal_general, iva, total)

        confirmar = input("Confirmar venta? (s/n): ")
        if confirmar == "s":
            descontar_inventario(productos, carrito)
            guardar_detalle_venta(detalle_ventas, movimientos, fecha, numero, carrito)
            ventas.append([numero, fecha, round(subtotal_general, 2), round(iva, 2), round(total, 2)])
            print("Venta guardada")
        else:
            print("Venta cancelada")