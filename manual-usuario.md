# Manual de usuario - Sistema de gestión comercial

## 1. Presentación y propósito del sistema

El Sistema de gestión comercial es un programa de consola que ayuda a un negocio pequeño a llevar el control de sus productos, sus ventas y su inventario, y a obtener reportes sencillos. Se maneja escribiendo números y datos en el teclado; no hace falta saber programar.

Con el sistema se puede:

- Registrar, consultar, modificar y desactivar productos.
- Registrar ventas con el cálculo automático del subtotal, el IVA (12 %) y el total.
- Controlar las existencias, registrar entradas de mercancía y ver los productos con poco inventario.
- Consultar reportes: historial de ventas, total de ingresos, producto más vendido, valor del inventario y promedio de ventas por mes.

## 2. Requisitos para utilizarlo

- Una computadora con Windows, macOS o Linux.
- Python 3 instalado (se descarga gratis en python.org). No se necesita instalar nada más.
- La carpeta `src` del programa (archivo principal `main.py`).
- Teclado. No se necesita internet.

## 3. Cómo iniciar y cerrar el programa

**Para iniciar:**

1. Abra la carpeta `src` del programa.
2. Abra una terminal en esa carpeta (en Windows: escriba `cmd` en la barra de direcciones de la carpeta y presione ENTER).
3. Escriba `python main.py` y presione ENTER. Si no funciona, pruebe con `py main.py`.
4. El programa pide la fecha de hoy. Escríbala con el formato AAAA-MM-DD, por ejemplo `2026-11-03`, y presione ENTER. Esa fecha se usa en todas las ventas y movimientos de la sesión.
5. Aparece el menú principal.

**Para cerrar:** en el menú principal escriba `5` y presione ENTER. El programa muestra "Adios" y termina. Importante: la información no se guarda en archivos; al cerrar el programa se borra (vea la sección 11).

## 4. Explicación del menú principal

Para elegir una opción, escriba su número y presione ENTER. Los submenús tienen una opción "Volver" para regresar al menú anterior.

| Opción | Nombre | Para qué sirve |
|---|---|---|
| 1 | Productos | Registrar, consultar, listar, modificar y desactivar productos |
| 2 | Ventas | Registrar una venta |
| 3 | Inventario | Ver existencias, registrar entradas, ver stock mínimo e historial de movimientos |
| 4 | Reportes | Historial de ventas, ingresos, producto más vendido, valor del inventario y promedio por mes |
| 5 | Salir | Cerrar el programa |

## 5. Productos: registrar, consultar y modificar

En el menú principal escriba `1`. Opciones: 1 Registrar, 2 Consultar, 3 Listado, 4 Modificar, 5 Desactivar y 6 Volver.

### Registrar un producto (opción 1)

1. Escriba `1` y presione ENTER.
2. **Codigo:** escriba un código único, por ejemplo `P001`. No puede repetirse ni quedar vacío.
3. **Nombre** y **Categoria:** escriba texto, por ejemplo `Cuaderno` y `Papeleria`.
4. **Precio:** escriba un número, con punto para los decimales, por ejemplo `25.5`.
5. **Cantidad:** las unidades que hay en este momento, un número entero, por ejemplo `20`.
6. **Stock minimo:** la cantidad a partir de la cual quiere recibir aviso de que queda poco, por ejemplo `5`.
7. El programa muestra "Producto registrado". La cantidad inicial se anota automáticamente en el historial como una ENTRADA.

### Consultar un producto (opción 2)

1. Escriba `2` y presione ENTER.
2. Escriba el código del producto.
3. Se muestran su código, nombre, categoría, precio, cantidad, stock mínimo y estado (Activo o Desactivado). Si el código no existe, aparece "El producto no existe".

Para ver todos los productos a la vez, use la opción `3` (Listado de productos).

### Modificar un producto (opción 4)

1. Escriba `4` y presione ENTER, y luego el código del producto.
2. Elija qué cambiar: `1` Nombre, `2` Categoría, `3` Precio o `4` Stock mínimo.
3. Escriba el nuevo valor. El programa muestra "Listo".

La cantidad en existencia no se cambia aquí: se modifica con las ventas y las entradas de inventario (sección 7).

### Desactivar un producto (opción 5)

Use esta opción cuando ya no se venda un producto. Escriba `5` y luego el código. El producto no se borra: queda como Desactivado, se conserva su información y ya no se puede vender.

## 6. Registrar una venta

Antes de vender, el producto debe estar registrado, activo y con existencias.

1. En el menú principal escriba `2` y presione ENTER.
2. **Codigo del producto:** escriba el código del producto que se vende.
3. **Cantidad:** escriba cuántas unidades. El programa responde "Agregado" y muestra el subtotal de ese producto.
4. Repita los pasos 2 y 3 por cada producto distinto de la venta.
5. Cuando termine, presione ENTER sin escribir ningún código.
6. El programa muestra el resumen: cada producto con su subtotal, el **Subtotal**, el **IVA 12%** y el **Total**.
7. **Confirmar venta? (s/n):** escriba `s` para guardar la venta o `n` para cancelarla.
8. Al confirmar, el programa muestra "Venta guardada", descuenta las unidades del inventario y anota las salidas en el historial de movimientos.

Si presiona ENTER sin haber agregado productos, o responde `n`, la venta se cancela y no se modifica nada.

## 7. Consultar y actualizar el inventario

En el menú principal escriba `3`. Opciones: 1 Ver existencias, 2 Registrar entrada, 3 Productos en stock mínimo, 4 Historial de movimientos y 5 Volver.

| Opción | Qué hace |
|---|---|
| 1 | Muestra el código, el nombre y la cantidad actual de cada producto |
| 3 | Muestra los productos cuya cantidad es igual o menor a su stock mínimo; son los que conviene reponer |
| 4 | Muestra todos los movimientos: fecha, código, tipo (ENTRADA o SALIDA), cantidad y descripción |

### Actualizar el inventario: registrar una entrada (opción 2)

Use esta opción cuando llegue mercancía nueva.

1. Escriba `2` y presione ENTER.
2. **Codigo:** escriba el código del producto. Si no existe, el programa muestra "El producto no existe".
3. **Cantidad que entra:** escriba las unidades recibidas (mayor que 0).
4. **Descripcion:** escriba una nota corta, por ejemplo `compra a proveedor`.
5. El programa muestra "Entrada registrada" con la nueva cantidad. Las salidas no se escriben a mano: se generan solas al registrar ventas.

## 8. Generar y consultar reportes

En el menú principal escriba `4`. Los reportes se calculan en el momento con la información registrada; no hay que "generarlos" aparte. Escriba el número del reporte y presione ENTER; cuando termine de leerlo, el menú vuelve a aparecer. Para salir escriba `8` (Volver).

| Opción | Reporte | Qué muestra |
|---|---|---|
| 1 | Listado general de productos | Todos los productos con sus datos |
| 2 | Productos en stock mínimo o menos | Los productos que hay que reponer |
| 3 | Historial de ventas | Cada venta con fecha, subtotal, IVA y total |
| 4 | Total de ingresos | La suma de los totales de todas las ventas |
| 5 | Producto más vendido | El código con más unidades vendidas y cuántas son |
| 6 | Valor del inventario | Precio × cantidad de los productos activos, sumado |
| 7 | Promedio de ventas por mes | Lo vendido en cada mes y el promedio mensual |

Si todavía no hay datos, el reporte muestra mensajes como "No hay ventas" o "No hay productos"; no es un error.

## 9. Mensajes de error más frecuentes

El programa no se cierra cuando ocurre un error: muestra el mensaje y vuelve a pedir el dato o regresa al menú.

| Mensaje | Causa | Qué hacer |
|---|---|---|
| Error: use el formato AAAA-MM-DD | La fecha del inicio no tiene 10 caracteres | Escriba la fecha completa, por ejemplo 2026-11-03 |
| Error: ese codigo ya existe | Se intentó registrar un código ya usado | Use otro código; para ver los existentes use el listado |
| Error: el codigo no puede estar vacio | Se presionó ENTER sin escribir el código | Escriba un código |
| Error: no puede ser negativo | Se escribió un número menor que 0 | Escriba un número de 0 en adelante |
| Error: escriba un numero / escriba un numero entero | Se escribieron letras, o decimales donde va un entero (cantidad, stock mínimo) | Escriba solo números; el precio usa punto decimal (25.5) |
| El producto no existe / Error: el producto no existe | El código no está registrado | Revise el código en el listado de productos |
| Error: el producto esta desactivado | Se intentó vender un producto desactivado | No se puede vender; si es necesario, regístrelo con otro código |
| Error: la cantidad debe ser mayor que 0 | Se escribió 0 como cantidad | Escriba una cantidad de 1 o más |
| Error: no hay suficiente inventario. Disponible: N | Se pidieron más unidades de las que hay (contando las ya agregadas a la venta) | Escriba una cantidad igual o menor a N, o registre primero una entrada |
| Opcion invalida | Se escribió una opción que no está en el menú | Escriba uno de los números mostrados |
| Venta cancelada / No se agrego nada. Venta cancelada | Se respondió `n`, o no se agregó ningún producto | Es normal; no se cambió el inventario. Repita la venta si es necesario |

## 10. Ejemplos de uso con capturas de pantalla

En las capturas, se muestra tanto lo que escribe el usuario como lo que responde el programa.

### Ejemplo 1: iniciar y cerrar

Se escribe la fecha, se prueba una opción que no existe (9) y se sale con la opción 5.

![Ejemplo 1: inicio y cierre del programa](../evidencias/MU-inicio.png)

### Ejemplo 2: registrar un producto

Menú 1, opción 1: se registra el producto P001 (Cuaderno, precio 25.5, 20 unidades, stock mínimo 5) y luego se muestra el listado con la opción 3.

![Ejemplo 2: registrar un producto](../evidencias/CP-01.png)

### Ejemplo 3: registrar una venta

Con los productos P001 (precio 25.5) y P003 (precio 4.0) ya registrados, se venden 2 y 5 unidades. El resumen muestra Subtotal 71.0, IVA 8.52 y Total 79.52, y se confirma con `s`.

![Ejemplo 3: venta con dos productos](../evidencias/CP-06.png)

### Ejemplo 4: registrar una entrada de inventario

Menú 3, opción 2: llegan 15 unidades de P001 y la existencia pasa de 20 a 35. Después se verifican las existencias con la opción 1.

![Ejemplo 4: entrada de inventario](../evidencias/CP-04.png)

### Ejemplo 5: consultar reportes

Después de dos ventas, se consultan el historial (opción 3), el total de ingresos (4) y el producto más vendido (5).

![Ejemplo 5: reportes de ventas](../evidencias/CP-15.png)

### Ejemplo 6: un mensaje de error

P001 tiene 20 unidades. Se piden 25 y el programa lo rechaza con "no hay suficiente inventario. Disponible: 20"; la venta continúa con una cantidad válida.

![Ejemplo 6: no hay suficiente inventario](../evidencias/CP-10.png)

## 11. Recomendaciones para conservar la información

**Este sistema no guarda archivos de datos.** Los productos, ventas y movimientos viven solo en la memoria mientras el programa está abierto; al elegir "Salir" (o cerrar la ventana) se pierden. Por eso:

1. **Registre todo en una sola sesión** y no cierre el programa hasta terminar de consultar los reportes.
2. **Antes de salir, deje constancia de lo importante:** abra los reportes que necesite (historial de ventas, total de ingresos, existencias) y tome una captura de pantalla o anótelos.
3. **No cierre la ventana de la terminal** por error mientras trabaja; cerrarla equivale a salir sin guardar.
4. **Conserve una copia del programa:** guarde la carpeta `src` en un lugar fijo y haga una copia de respaldo en una memoria USB o en la nube. No cambie los nombres de los archivos.
5. **Al iniciar una nueva sesión** el sistema empieza vacío: hay que registrar de nuevo los productos con sus existencias actuales.
