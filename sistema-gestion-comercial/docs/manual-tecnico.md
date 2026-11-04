# Manual técnico

## 1\. Descripción general

Aplicación de consola en Python 3 sin librerías externas. Los datos viven en listas en memoria mientras el programa está abierto; no se guardan en archivos.

## 2\. Estructura del código

|Archivo|Contenido|
|-|-|
|`src/main.py`|Crea las listas, pide la fecha y muestra el menú principal|
|`src/estructuras.py`|Constantes y funciones comunes: `pedir\_entero`, `pedir\_decimal`, `pedir\_fecha`, `buscar\_producto`, `buscar\_posicion`, `registrar\_movimiento`|
|`src/productos.py`|`registrar\_producto`, `consultar\_producto`, `listar\_productos`, `modificar\_producto`, `desactivar\_producto`, `menu\_productos`|
|`src/ventas.py`|`llenar\_carrito`, `registrar\_venta` y las funciones de cálculo `calcular\_subtotal`, `calcular\_iva`, `calcular\_total`, `calcular\_subtotal\_general`, `calcular\_numero\_venta`|
|`src/inventario.py`|`ver\_existencias`, `registrar\_entrada`, `ver\_stock\_minimo`, `ver\_movimientos`, `menu\_inventario`|
|`src/reportes.py`|Cálculos (`calcular\_total\_ingresos`, `calcular\_valor\_inventario`, `calcular\_unidades\_por\_producto`, `calcular\_ventas\_por\_mes`, `calcular\_promedio`) y los reportes `mostrar\_\*`|

Cada módulo recibe las listas como parámetros (no se usan variables globales). Las funciones de cálculo devuelven el resultado con `return` y no imprimen.

## 3\. Estructuras de datos (matrices)

|Lista|Cada registro es una lista con|
|-|-|
|`productos`|`\[codigo, nombre, categoria, precio, cantidad, stock\_minimo, activo]`|
|`ventas`|`\[numero, fecha, subtotal, iva, total]`|
|`detalle\_ventas`|`\[numero\_venta, codigo, cantidad, subtotal]`|
|`movimientos`|`\[fecha, codigo, tipo, cantidad, descripcion]`|

Las posiciones de un producto se nombran con constantes (`POS\_CODIGO` = 0 … `POS\_ACTIVO` = 6) definidas en `estructuras.py`.

## 4\. Reglas de negocio

* IVA del 12 % (`TASA\_IVA = 0.12`) sobre el subtotal de cada venta.
* El código de producto es único y no puede estar vacío.
* No se aceptan precios, cantidades ni stock mínimo negativos.
* Un producto desactivado no se vende, pero se conserva.
* No se vende más de lo que hay en existencia, contando lo ya agregado a la venta.
* Toda entrada y toda salida deja un movimiento en el historial.

## 5\. Convenciones

* Nombres de variables y funciones en minúsculas con guion bajo.
* Menús, comentarios y mensajes sin tildes ni ñ, para evitar problemas de codificación en la consola.
* Ciclos `while` para repetir la petición de datos y `for` para recorrer las listas.

## 6\. Pruebas

casos documentados en "evidencias/". 

