TASA_IVA = 0.12


POS_CODIGO = 0
POS_NOMBRE = 1
POS_CATEGORIA = 2
POS_PRECIO = 3
POS_CANTIDAD = 4
POS_STOCK_MINIMO = 5
POS_ACTIVO = 6


def pedir_entero(mensaje):
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
    fecha = ""
    while len(fecha) != 10:
        fecha = input("Escriba la fecha de hoy (AAAA-MM-DD): ")
        if len(fecha) != 10:
            print("Error: use el formato AAAA-MM-DD")
    return fecha


# FUNCIONES PARA LA BUSQUEDA Y REGISTRO

def buscar_producto(productos, codigo):
    for i in range(len(productos)):
        if productos[i][POS_CODIGO] == codigo:
            return i
    return -1


def buscar_posicion(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1


def registrar_movimiento(movimientos, fecha, codigo, tipo, cantidad, descripcion):
    movimientos.append([fecha, codigo, tipo, cantidad, descripcion])

# MODULO 1 - GESTION DE PRODUCTOS

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

# MODULO 3 - CONTROL DE INVENTARIOS

def esta_en_stock_minimo(producto):
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

# MODULO 4 - REPORTES Y ESTADISTICAS

def calcular_total_ingresos(ventas):
    suma = 0
    for numero, fecha, subtotal, iva, total in ventas:
        suma = suma + total
    return suma


def calcular_valor_inventario(productos):
    suma = 0
    for producto in productos:
        if producto[POS_ACTIVO]:
            suma = suma + (producto[POS_PRECIO] * producto[POS_CANTIDAD])
    return suma


def calcular_unidades_por_producto(detalle_ventas):
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
    posicion_mayor = 0
    for i in range(len(valores)):
        if valores[i] > valores[posicion_mayor]:
            posicion_mayor = i
    return posicion_mayor


def calcular_ventas_por_mes(ventas):
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