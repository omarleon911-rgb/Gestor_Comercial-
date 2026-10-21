#Sistema de gestion comercia. 

#solicitar fecha actual
fecha_hoy = ""

#registra los prodcutos, por nombre, codigo, categoria, precio, cantidad, stock. activo. 
#activo:  si es 1 si se puede vender, si es 0 no esta activo.
productos = []

#registra cada venta, por numero, fecha, sutotal, iva, total
ventas = []

#detaslles de las ventas: fecha, codigo, tipo, cantidad, descripcion 
detalle_ventas = []

#movimientos: fecha, codigo, tipo, cantidad, descripcion
movimientos = []    

IVA = 0.12

#==============================================================================
def guardar_movimiento(co   
