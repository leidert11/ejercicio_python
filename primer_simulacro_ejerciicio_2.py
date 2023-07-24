def numeros_perfectos():
    # se crea la función para encontrar los números perfectos
    numeros_perfectos_encontrados = []
    # se crea esta lista en la cual más adelante se agregarán los números perfectos
    numero = 2
    # esta variable se inicializa en dos, siendo ese el número mínimo

    while len(numeros_perfectos_encontrados) < 4:
        # el while es para que se detenga una vez que encuentre el número con 4 dígitos "8128"
        suma_divisores = 0
        # esta variable se inicializa en 0 para que sea a la que se le agregue el divisor más adelante

        for i in range(1, numero):
            # se itera el for con rango 1 hasta que llegue al número indicado
            if numero % i == 0:
                # aquí se van a encontrar todos los números divisibles entre 0
                suma_divisores += i
                # y se le sumará por cada iteración que se haga

        if suma_divisores == numero:
            # una vez se complete de agregar los números que el resto es 0 de "numero"
            # se itera la variable "suma_divisores"
            numeros_perfectos_encontrados.append(numero)
            # para que se utilice la lista de números perfectos y se le agregue los números
            # los cuales el resto es 0
        numero += 1

    return numeros_perfectos_encontrados
    # se retorna la lista con los números perfectos que se encontró hasta el 4

print("Los primeros 4 números perfectos son:")
numeros_encontrados = numeros_perfectos()
# se encapsula la función en una variable "numeros_encontrados" para poderla imprimir
print(numeros_encontrados)
# impresión de la variable que contiene la función
