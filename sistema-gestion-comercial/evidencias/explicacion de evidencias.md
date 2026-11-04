Evidencias de las pruebas

Detalle de cada caso

01 - Registrar un producto con datos válidos



Datos utilizados: Código 1; nombre Cuaderno; categoría Papeleria; precio 25.5; cantidad 20; stock mínimo 5



Resultado esperado: El sistema muestra “Producto registrado”, agrega el producto activo a la lista y registra un movimiento ENTRADA de 20 unidades (inventario inicial).



Resultado obtenido: Mensaje: “Producto registrado”. Listado: 1 | Cuaderno | Papeleria | Precio: 25.5 | Cantidad: 20 | Minimo: 5 | Activo. Lista productos = \[\['1', 'Cuaderno', 'Papeleria', 25.5, 20, 5, True]]. Movimientos = \[\['2026-11-01', '1', 'ENTRADA', 20, 'Inventario inicial']].



Conclusión: Cumple. El producto se registró con todos sus datos y quedó activo.



02 - Consultar un producto existente



Datos utilizados: Código a consultar: 1 (registrado antes)



Resultado esperado: El sistema muestra los siete datos del producto: código, nombre, categoría, precio, cantidad, stock mínimo y estado Activo.



Resultado obtenido: Se mostraron: Codigo: 1; Nombre: Cuaderno; Categoria: Papeleria; Precio: 25.5; Cantidad: 20; Stock minimo: 5; Estado: Activo.



Conclusión: Cumple. La consulta por código devuelve la información completa del producto.



03 - Modificar el precio de un producto



Datos utilizados: Código 1; opción 3 (precio); nuevo precio 30



Resultado esperado: El sistema muestra “Listo” y el producto queda con precio 30.0; la consulta posterior lo confirma.



Resultado obtenido: Mensaje: “Listo”. La consulta posterior muestra: Precio: 30.0. Precio en la lista = 30.0.



Conclusión: Cumple. El cambio de precio se aplicó y se conservó en la lista.



04 - Registrar una entrada de inventario



Datos utilizados: Código 1 (20 unidades); cantidad que entra 15; descripción “compra a proveedor”



Resultado esperado: La existencia sube de 20 a 35 y se registra un movimiento ENTRADA de 15 unidades con la descripción escrita.



Resultado obtenido: Entrada registrada. Nueva cantidad: 35. Existencias: 1 | Cuaderno | Cantidad: 35. Último movimiento = \['2026-11-01', '1', 'ENTRADA', 15, 'compra a proveedor'].



Conclusión: Cumple. La entrada actualizó la existencia y quedó registrada en el historial.



05 - Venta válida: subtotal, IVA y total



Datos utilizados: 1 con precio 25.5 y 20 unidades; se vende 1 producto: 1 × 4; confirma con “s”



Resultado esperado: Subtotal = 25.5 × 4 = 102.0; IVA 12 % = 12.24; Total = 114.24; venta No. 1; la existencia baja de 20 a 16.



Resultado obtenido: Resumen: Subtotal: Q 102.0; IVA 12%: Q 12.24; Total: Q 114.24. Venta guardada = \[\[1, '2026-11-01', 102.0, 12.24, 114.24]]. Existencia de 1 = 16.



Conclusión: Cumple. Los cálculos coinciden con el resultado hecho a mano y el inventario se actualizó.



06 - Venta con varios productos y actualización de las listas



Datos utilizados: 1 (25.5, 20 unidades) y 3 (4.0, 15 unidades); se vende 1 × 2 y 3 × 5; confirma con “s”



Resultado esperado: Subtotales 51.0 y 20.0; subtotal general 71.0; IVA 8.52; total 79.52. Existencias: 1 = 18 y 3 = 10. Dos movimientos SALIDA y dos renglones en el detalle de la venta.



Resultado obtenido: Resumen: Subtotal: Q 71.0; IVA 12%: Q 8.52; Total: Q 79.52. Detalle = \[\[1, '1', 2, 51.0], \[1, '3', 5, 20.0]]. Existencias: 1 = 18, 3 = 10. Movimientos SALIDA = 2.



Conclusión: Cumple. Los totales son correctos y las listas de productos, detalle y movimientos quedaron actualizadas.



07 - Intentar registrar un código duplicado



Datos utilizados: 1 ya registrado; se intenta registrar otra vez el código 1



Resultado esperado: El sistema muestra “Error: ese codigo ya existe” y no agrega un segundo producto.



Resultado obtenido: Mensaje: “Error: ese codigo ya existe”. Productos en la lista = 1: \[\['1', 'Cuaderno', 'Papeleria', 25.5, 20, 5, True]].



Conclusión: Cumple. El código repetido fue rechazado y no se duplicó el producto.



08 - Ingresar precio y cantidad negativos



Datos utilizados: Precio -10 (luego 25.5); cantidad -3 (luego 20)



Resultado esperado: El sistema muestra “Error: no puede ser negativo” en cada caso, vuelve a pedir el dato y solo guarda los valores válidos.



Resultado obtenido: El mensaje “Error: no puede ser negativo” apareció 2 veces y se volvió a pedir el dato. Producto guardado = \[\['1', 'Cuaderno', 'Papeleria', 25.5, 20, 5, True]].



Conclusión: Cumple. Los valores negativos fueron rechazados y el producto se guardó solo con datos válidos.



09 - Ingresar datos de tipo incorrecto



Datos utilizados: Precio “abc” (luego 25.5); cantidad “diez” (luego 20); stock mínimo “5.5” (luego 5)



Resultado esperado: El sistema muestra un mensaje de error por cada texto o decimal no permitido, vuelve a pedir el dato y no se cierra.



Resultado obtenido: Se mostró “Error: escriba un numero” 1 vez (precio) y “Error: escriba un numero entero” 2 veces (cantidad y stock). Producto guardado = \[\['1', 'Cuaderno', 'Papeleria', 25.5, 20, 5, True]].



Conclusión: Cumple. El programa no falló con datos de tipo incorrecto y pidió el dato otra vez.



10 - Intentar vender más unidades de las disponibles



Datos utilizados: 1 con 20 unidades; se intenta 1 × 25; luego 1 × 15 (válido) y 1 × 10 (15 + 10 supera 20); confirma con “s”



Resultado esperado: Se rechazan 1 × 25 y 1 × 10 con “no hay suficiente inventario”; solo se vende 1 × 15: subtotal 382.5, IVA 45.9, total 428.4; la existencia queda en 5.



Resultado obtenido: El mensaje “no hay suficiente inventario. Disponible: 20” apareció 2 veces. Solo se vendieron 15 unidades: Total: Q 428.4. Venta guardada = \[\[1, '2026-11-01', 382.5, 45.9, 428.4]]. Existencia final de 1 = 5.



Conclusión: Cumple. El sistema impidió vender más de lo disponible, incluso sumando lo que ya estaba en el carrito.



11 - Consultar un producto inexistente



Datos utilizados: Lista de productos vacía; código a consultar: 999



Resultado esperado: El sistema muestra “El producto no existe” y regresa al menú sin errores.



Resultado obtenido: Mensaje: “El producto no existe”. La lista de productos sigue vacía = \[].



Conclusión: Cumple. Un código inexistente se maneja con un mensaje y el programa continúa.



12 - Intentar vender un producto desactivado



Datos utilizados: 1 desactivado con la opción 5; se intenta vender 1



Resultado esperado: El sistema muestra “Error: el producto esta desactivado”, no se registra ninguna venta y la existencia sigue en 20.



Resultado obtenido: Mensaje: “Error: el producto esta desactivado”. Ventas = \[]. Existencia de 1 = 20. Activo = False.



Conclusión: Cumple. Un producto desactivado no se puede vender y su información se conserva.



13 - Elegir una opción inválida en los menús



Datos utilizados: Menú principal: 9, abc y vacío (solo ENTER); menú de productos: x



Resultado esperado: El sistema muestra “Opcion invalida”, vuelve a mostrar el menú y no se cierra; al final sale con la opción 5.



Resultado obtenido: El mensaje “Opcion invalida” apareció 4 veces (3 en el menú principal y 1 en el de productos). El programa siguió funcionando y terminó con “Adios”.



Conclusión: Cumple. Una opción inválida no termina el programa y la salida es controlada.



14 - Venta cancelada y carrito vacío



Datos utilizados: Venta 1: 1 × 3 y respuesta “n” a la confirmación; venta 2: ENTER sin agregar productos



Resultado esperado: En ambos casos no se registra venta, la existencia sigue en 20 y no se crean movimientos nuevos.



Resultado obtenido: Mensajes “Venta cancelada” (confirmación n) y “No se agrego nada. Venta cancelada” (carrito vacío). Ventas = \[]. Existencia de 1 = 20. Movimientos = 1 (solo el inventario inicial).



Conclusión: Cumple. Las ventas canceladas no modifican el inventario ni los registros.



15 - Reportes de ventas: historial, total de ingresos y producto más vendido



Datos utilizados: 1 (25.5, 20 unidades) y 2 (2.75, 3 unidades). Venta 1: 1 × 4 y 2 × 1. Venta 2: 1 × 6. Reportes 3, 4 y 5



Resultado esperado: Venta 1: subtotal 104.75, IVA 12.57, total 117.32. Venta 2: subtotal 153.0, IVA 18.36, total 171.36. Total de ingresos = 288.68. Más vendido: 1 con 10 unidades.



Resultado obtenido: Historial: Venta 1 | 2026-11-01 | Subtotal: 104.75 | IVA: 12.57 | Total: 117.32 ; Venta 2 | 2026-11-01 | Subtotal: 153.0 | IVA: 18.36 | Total: 171.36. Total de ingresos: Q 288.68. Más vendido: Codigo del producto: 1, Unidades vendidas: 10.



Conclusión: Cumple. Los reportes se calculan con los datos guardados y coinciden con el cálculo manual.



16 - Reportes de inventario: listado, stock mínimo, valor del inventario y promedio por mes



Datos utilizados: Mismos datos del caso anterior (después de las dos ventas). Reportes 1, 2, 6 y 7



Resultado esperado: Existencias: 1 = 10 y 2 = 2. Stock mínimo: solo 2 (2 ≤ 5). Valor del inventario = 10 × 25.5 + 2 × 2.75 = 260.5. Promedio por mes (un solo mes, 2026-11) = 288.68.



Resultado obtenido: Stock mínimo: 2 | Lapiz | Cantidad: 2 | Minimo: 5 (1 no aparece). Valor total: Q 260.5. Mes 2026-11 : Q 288.68; Promedio por mes: Q 288.68. Existencias: 1 = 10, 2 = 2.



Conclusión: Cumple. El valor del inventario, la alerta de stock mínimo y el promedio coinciden con el cálculo manual.



