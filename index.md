REGLAS GENERALES DEL SISTEMA



\-El IVA es del 12% sobre el subtotal de cada venta realizada.

\-Cualquier opción que se seleccione en el menú, no cierra el programa.

\-Los códigos de los productos son únicos.

\-No se aceptan precios ni cantidades negativas.

\-El producto desactivado no se puede vender, pero si se conserva la información.





***Modulo 1 - Gestión de Productos***



\#Objetivo: 

Registrar un producto nuevo con todos sus datos, para que pueda ser vendido y controlar el inventario.



\#Descripción del funcionamiento: 

Al momento de seleccionar en "Registrar producto" en el menú, el programa pide el código y verifica y ya existe o no, luego pide los demás datos, se valida los números, luego agrega el producto a la lista y lo guarda. Si el producto esta en existencias, se registra además un movimiento de Entrada.



\#Datos de entrada:

* Código
* Nombre y categoría
* Precio de venta
* Cantidad disponible
* Stock mínimo



\#Procesamiento realizado:

1. Buscar el código en la lista de productos.
2. Solicitar nombre, categoría, recio, cantidad y stock mínimo, repitiendo cada numero.
3. Crear el producto en estado activo.
4. Agregarlo a la lista y guardar la lista en el archivo de productos.
5. Si la cantidad es mayor que el 0, se registra un movimiento en Entrada con la descripción "Inventario inicial"



\#Datos de salida:

* Mensaje "Producto registrado"
* Una dato nuevo en el registro de productos.
* Un movimiento en el registro de movimientos, si hay en existencias iniciales.



\#Reglas de negocio:

* Cada código es único y no puede estar vacío.
* El precio, cantidad y stock mínimo no pueden ser negativos.
* Todo producto nuevo queda activo y disponible para la venta.
* Las existencias iniciales cuentan como una entrada de inventario.



\#Validaciones y posibles errores:

* Numero negativo: se muestra "no puede ser negativo" y se vuelve a pedir el dato.
* Texto en lugar de números: se muestra "escriba un numero" y se vuelve a pedir el dato correcto.
* Código vacío o repetido: Se muestra un error y no se puede registrar.



***Modulo 2 - Registro de Ventas***

\#Objetivo:

Consultar los datos de un producto mediante su código y corregir cuando cambien.



\#Descripción del funcionamiento:

Para poder consultar el usuario escribe un código y el programa enseña todos los datos del producto. para modificar el código, se elige que dato cambiar, ya sea el nombre, código, precio o stock. se escribe el valor nuevo y el programa guarda ese cambio. 

Desactivar un producto también es una modificación, ya que cambia su estado a inactivo para que ya no este disponible para venta. 



\#Datos de entrada:

* Código del producto.
* Opción para modificar. 
* Nuevo valor del dato elegido. 



\#Procesamiento realizado:

1. Buscar el código en la lista de productos. 
2. Si es una consulta, mostrar código, nombre categoría, precio, stock mínimo, cantidad y estado. 
3. Si es una modificación debe mostrar las opciones, leer la opción y pedir el nuevo valor y validando si es un numero. 
4. Se debe reemplazar el dato en la lista y guardar la lista en productos. 



\#Datos de salida:

* Los datos de producto en pantalla. 
* Mensaje "Listo" y el archivo de productos actualizado. 



\#Reglas de negocio:

1. El código de un producto no se puede cambiar. 
2. Las existencias no se modifican aquí, solo se cambian con entradas de inventario y con ventas. 
3. El nuevo precio y el nuevo stock mínimo no pueden ser negativos.
4. Un producto desactivado se conserva en el archivo y no se borra. 



\#Validaciones y posibles errores:

* Código que no existe, se muestra "El producto no existe" y el proceso termina.
* Opción fuera del rango 1 a 4, se muestra "Opción valida" y no se cambia nada. 
* Valor numérico negativo o con texto, se muestra el error y se vuelve a pedir. 



Modulo 3 - Control de inventarios

\#Objetivo:

Registrar la venta de uno o mas productos, calcular lo que paga el cliente y descontar lo vendido del inventario. 



\#Descripción del funcionamiento:

El usuario escribe código y cantidades hasta presionar Enter, sin escribir un código, cada producto valido se agrega a un carrito. Al terminar, el programa calcula el subtotal, el IVA y el total, se asigna el numero de venta, muestra el resumen y pide confirmación. Sil el usuario confirma, descuenta las existencias guarda la venta y registra las salidas de inventario. 



\#Datos de entrada:

* Código de cada producto a vender.
* Cantidad de cada producto. 
* Confirmación de la venta. 



\#Procesamiento realizado:

1. Verificar que el producto exista y este activo.
2. Verificar que la cantidad sea mayor que 0 y que sumada a lo ya agregado al carrito, no supere la existencia. 
3. Calcular el subtotal de cada producto: precio por cantidad. 
4. calcular el subtotal general(suma de subtotales), el IVA(subtotal general)
5. Asignar el numero de venta: ventas anteriores +1.
6. Si el usuario confirma: restar las cantidades de la existencia, registrar un movimiento de Salida por producto, guardar el detalle y la venta en sus archivos y guardar la lista de productos.



\#Datos de salida:

* Resumen en pantalla: producto, cantidad y subtotal de cada linea, subtotal general, IVA y total.
* Mensaje "Venta guardada" o "Venta cancelada".
* Lineas nuevas en ventas, detalles de ventas y movimientos. 
* Existencias actualizadas en productos. 



\#Reglas de negocio:

* El IVA es del 12 % sobre el subtotal general.
* Solo se venden productos activos.
* No se vende más de lo que hay en inventario, contando lo que ya está en el carrito.
* Un carrito vacío no genera una venta.
* El inventario solo cambia cuando la venta se confirma.
* El número de venta es consecutivo y empieza en 1.



\#Validaciones y posibles errores:

•  Código inexistente: “el producto no existe”.

•  Producto desactivado: “el producto está desactivado”.

•  Cantidad 0 o texto: se muestra el error y se vuelve a pedir.

•  Cantidad mayor que la existencia: “no hay suficiente inventario” y se muestra lo disponible.

•  Carrito vacío o respuesta distinta de “s”: la venta se cancela sin cambiar nada.



Modulo 4 - Reportes y Estadísticas

\#Objetivo:

\#Descripción del funcionamiento:

\#Datos de entrada:

\#Procesamiento realizado:

\#Datos de salida:

\#Reglas de negocio:

\#Validaciones y posibles errores:









