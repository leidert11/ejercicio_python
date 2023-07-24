def sumar(num_1, num_2):
    operacion = num_1 + num_2
    return operacion

def resta(num_1, num_2):
    operacion = num_1 - num_2
    return operacion

def multi(num_1, num_2):
    operacion = num_1 * num_2
    return operacion

def divi(num_1, num_2):
    operacion = num_1 // num_2
    return operacion

def potencia(num_1, num_2):
    operacion = num_1 ** num_2
    return operacion

def pedir_numero():
    print("Seleccione la operacion a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("0. Salir")
    eleccion = int(input("Ingrese el número correspondiente: "))

    if eleccion == 0:
        return eleccion, 0, 0

    num_1 = int(input('Ingrese el primer número: '))
    num_2 = int(input('Ingrese el segundo número: '))

    return eleccion, num_1, num_2

def ejecutar_operaciones():
    flag = True

    while flag:
        eleccion, num_1, num_2 = pedir_numero()

        if eleccion == 0:
            break
        elif eleccion == 1:
            resultado = sumar(num_1, num_2)
        elif eleccion == 2:
            resultado = resta(num_1, num_2)
        elif eleccion == 3:
            resultado = multi(num_1, num_2)
        elif eleccion == 4:
            resultado = divi(num_1, num_2)
        elif eleccion == 5:
            resultado = potencia(num_1, num_2)
        else:
            print("Opción inválida. Intente nuevamente.")
            continue

        print(f"El resultado de la operación es: {resultado}")


ejecutar_operaciones()
