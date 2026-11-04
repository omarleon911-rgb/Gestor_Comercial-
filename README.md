Sistema de Gestión Comercial en Python



Este es un proyecto en Python para administrar un pequeño negocio. Permite manejar productos, registrar ventas, llevar el control del inventario y ver reportes básicos.



Fue creado usando solo funciones, listas, ciclos y validaciones básicas, sin usar librerías externas ni bases de datos.



¿Qué hace el programa?



El sistema está dividido en varias partes o módulos:



Productos: permite registrar productos nuevos, ver la información de un producto, ver la lista completa, modificar sus datos y desactivarlos.



Ventas: permite agregar productos a un carrito, calcular el subtotal, el IVA (12%) y el total a pagar. También descuenta los productos vendidos del inventario.



Inventario: muestra las existencias actuales, permite registrar cuando entra más mercadería, avisa qué productos están por terminarse (stock mínimo) y guarda el historial de movimientos.



Reportes: muestra las ventas realizadas, el total de dinero ingresado, el producto más vendido, cuánto vale todo el inventario y el promedio de ventas por mes.



Requisitos



Tener instalado Python 3 (cualquier versión reciente).



¿Cómo ejecutar el programa?



Abrir la terminal o consola de comandos.



Ir a la carpeta donde está el código.



Ejecutar el siguiente comando:



python main.py



Al iniciar, el programa pedirá ingresar la fecha del día de hoy con el formato AAAA-MM-DD para poder comenzar a usar el menú.



Archivos del proyecto



main.py: tiene el menú principal y une todas las partes del programa.



productos.py: funciones para manejar los productos.



ventas.py: funciones para realizar las ventas.



inventario.py: funciones para ver existencias y registrar entradas de stock.



reportes.py: funciones para mostrar los datos estadísticos.



estructuras.py: constantes y funciones para pedir datos o hacer búsquedas.



A tener en cuenta



Los datos solo se guardan mientras el programa está abierto. Si se cierra la consola, los datos se borran porque no se está usando una base de datos ni archivos de texto.
