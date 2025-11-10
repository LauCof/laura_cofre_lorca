def numeros_positivos(mensaje:str) -> int:
    bruto = input(mensaje).strip()
    try:
        valor = int(bruto)
    except ValueError as err:
        raise ValueError("Por favor, ingresar numero entero valido") from err
    if valor < 0:
        raise ValueError("Los numeros no pueden ser negativos")
    return valor

def calculo_inventario(stock:int, vendidos: int) -> int:
    if vendidos> stock:
        raise ValueError("Cantidad de productos vendidos no puede superar el stock del producto")
    return stock-vendidos

def main():
    print("Control de inventarios - Chocolamu")
    while True:
        try:
            stock = numeros_positivos("Por favor, ingresar cantidad actual de inventario:")
            vendidos = numeros_positivos("Ingrese cantidad de productos vendidos:")
            nuevo = calculo_inventario(stock, vendidos)
        except ValueError as verror:
            print(f"Error: {verror} \nValor no aceptado, por favor, ingresar numeros enteros positivo.\n")
            continue
        except KeyboardInterrupt:
            print("Operacion detenida por usuario o keyboard")
            break
        else:
            print(f"Datos validados. El stock ha sido actualizado. Hay:{nuevo}")
            break
    print("Gracias por usar nuestro sistema de control. Volver a Inicio para actualizacion de inventario")


if __name__ == "__main__":
    main()
    