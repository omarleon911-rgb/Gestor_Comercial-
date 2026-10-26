#Sistema de gestion comercia. 


TASA_IVA = 0.12

POS_CODIGO = 0
POS_NOMBRE = 1
POS_CATEGORIA = 2
POS_PRECIO = 3
POS_CANTIDAD = 4
POS_STOCK_MINIMO = 5
POS_ACTIVO = 6



def pedir_entero(mensaje):
    # Pide un numero entero que no sea negativo y lo devuelve
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
    # Pide un numero con decimales que no sea negativo y lo devuelve
    numero = -1.0
    while numero < 0:
        try:
            numero = float(input(mensaje))
            if numero < 0:
                print("Error: no puede ser negativo")
        except ValueError:
            print("Error: escriba un numero")
    return numero
