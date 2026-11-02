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

