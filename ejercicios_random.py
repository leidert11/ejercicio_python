# Problema 1: Calcular el promedio de una lista de números.
# Solución:
def calcular_promedio(lista):
    total = sum(lista)
    promedio = total / len(lista)
    return promedio

# Problema 2: Encontrar el número máximo y mínimo en una lista de números.
# Solución:
def encontrar_maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

# Problema 3: Verificar si una palabra es un palíndromo.
# Solución:
def es_palindromo(palabra):
    return palabra == palabra[::-1]

# Problema 4: Contar la cantidad de veces que aparece cada letra en una palabra.
# Solución:
def contar_letras(palabra):
    contador_letras = {}
    for letra in palabra:
        if letra in contador_letras:
            contador_letras[letra] += 1
        else:
            contador_letras[letra] = 1
    return contador_letras

# Problema 5: Encontrar el número más grande en una matriz (lista de listas).
# Solución:
def encontrar_maximo_matriz(matriz):
    maximo = float("-inf")
    for fila in matriz:
        for numero in fila:
            if numero > maximo:
                maximo = numero
    return maximo

# Problema 6: Calcular el factorial de un número utilizando recursión.
# Solución:
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Problema 7: Contar la cantidad de números pares e impares en una lista.
# Solución:
def contar_pares_impares(lista):
    pares = sum(1 for num in lista if num % 2 == 0)
    impares = sum(1 for num in lista if num % 2 != 0)
    return pares, impares

# Problema 8: Crear una lista de números primos hasta un número dado.
# Solución:
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def lista_primos(hasta):
    primos = [num for num in range(2, hasta + 1) if es_primo(num)]
    return primos

# Problema 9: Unir dos diccionarios y sumar los valores de las claves comunes.
# Solución:
def unir_diccionarios(dicc1, dicc2):
    for clave, valor in dicc2.items():
        if clave in dicc1:
            dicc1[clave] += valor
        else:
            dicc1[clave] = valor
    return dicc1

# Problema 10: Crear una tupla de coordenadas (x, y) a partir de dos listas.
# Solución:
def crear_tupla_coordenadas(lista_x, lista_y):
    coordenadas = [(x, y) for x, y in zip(lista_x, lista_y)]
    return coordenadas

# Problema 11: Calcular el área de un triángulo dado sus lados usando la fórmula de Herón.
# Solución:
def calcular_area_triangulo(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Problema 12: Convertir una cadena de texto a una lista de palabras.
# Solución:
def cadena_a_lista_palabras(cadena):
    lista_palabras = cadena.split()
    return lista_palabras

# Problema 13: Verificar si una lista está ordenada de manera ascendente.
# Solución:
def esta_ordenada_ascendente(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))

# Problema 14: Contar la cantidad de veces que aparecen los elementos de una lista.
# Solución:
def contar_elementos(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

# Problema 15: Sumar dos matrices (listas de listas) y retornar la matriz resultante.
# Solución:
def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_resultante = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_resultante[i][j] = matriz1[i][j] + matriz2[i][j]

    return matriz_resultante


# Ejemplo de uso del menú:

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular promedio de una lista de números")
        print("2. Encontrar máximo y mínimo en una lista de números")
        print("3. Verificar si una palabra es un palíndromo")
        print("4. Contar la cantidad de veces que aparece cada letra en una palabra")
        print("5. Encontrar el número más grande en una matriz")
        print("6. Calcular factorial de un número")
        print("7. Contar la cantidad de números pares e impares en una lista")
        print("8. Crear una lista de números primos")
        print("9. Unir dos diccionarios y sumar los valores de las claves comunes")
        print("10. Crear una tupla de coordenadas")
        print("11. Calcular el área de un triángulo dado sus lados")
        print("12. Convertir una cadena de texto a una lista de palabras")
        print("13. Verificar si una lista está ordenada de manera ascendente")
        print("14. Contar la cantidad de veces que aparecen los elementos de una lista")
        print("15. Sumar dos matrices")
        print("16. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            lista_numeros = [float(x) for x in input("Ingrese los números separados por espacios: ").split()]
            promedio = calcular_promedio(lista_numeros)
            print(f"El promedio de los números es: {promedio}")
        elif opcion == "2":
            lista_numeros = [float(x) for x in input("Ingrese los números separados por espacios: ").split()]
            maximo, minimo = encontrar_maximo_minimo(lista_numeros)
            print(f"El número máximo es: {maximo}")
            print(f"El número mínimo es: {minimo}")
        elif opcion == "3":
            palabra = input("Ingrese una palabra: ")
            if es_palindromo(palabra):
                print("Es un palíndromo.")
            else:
                print("No es un palíndromo.")
        elif opcion == "4":
            palabra = input("Ingrese una palabra: ")
            contador_letras = contar_letras(palabra)
            print(f"Conteo de letras: {contador_letras}")
        elif opcion == "5":
            matriz = []
            while True:
                fila = input("Ingrese una fila de números separados por espacios (o 'q' para terminar): ")
                if fila == "q":
                    break
                matriz.append([float(x) for x in fila.split()])
            maximo = encontrar_maximo_matriz(matriz)
            print(f"El número máximo en la matriz es: {maximo}")
        elif opcion == "6":
            numero = int(input("Ingrese un número entero positivo: "))
            resultado = factorial(numero)
            print(f"El factorial de {numero} es: {resultado}")
        elif opcion == "7":
            lista_numeros = [int(x) for x in input("Ingrese los números separados por espacios: ").split()]
            pares, impares = contar_pares_impares(lista_numeros)
            print(f"Cantidad de números pares: {pares}")
            print(f"Cantidad de números impares: {impares}")
        elif opcion == "8":
            hasta = int(input("Ingrese un número entero positivo: "))
            primos = lista_primos(hasta)
            print(f"Lista de números primos hasta {hasta}: {primos}")
        elif opcion == "9":
            diccionario1 = eval(input("Ingrese el primer diccionario (en formato de diccionario en línea): "))
            diccionario2 = eval(input("Ingrese el segundo diccionario (en formato de diccionario en línea): "))
            resultado = unir_diccionarios(diccionario1, diccionario2)
            print(f"Diccionario unido y sumado: {resultado}")
        elif opcion == "10":
            lista_x = [float(x) for x in input("Ingrese los valores de x separados por espacios: ").split()]
            lista_y = [float(y) for y in input("Ingrese los valores de y separados por espacios: ").split()]
            coordenadas = crear_tupla_coordenadas(lista_x, lista_y)
            print(f"Lista de coordenadas: {coordenadas}")
        elif opcion == "11":
            a = float(input("Ingrese el valor del lado a del triángulo: "))
            b = float(input("Ingrese el valor del lado b del triángulo: "))
            c = float(input("Ingrese el valor del lado c del triángulo: "))
            area = calcular_area_triangulo(a, b, c)
            print(f"El área del triángulo es: {area}")
        elif opcion == "12":
            cadena = input("Ingrese una cadena de texto: ")
            lista_palabras = cadena_a_lista_palabras(cadena)
            print(f"Lista de palabras: {lista_palabras}")
        elif opcion == "13":
            lista_numeros = [float(x) for x in input("Ingrese los números separados por espacios: ").split()]
            if esta_ordenada_ascendente(lista_numeros):
                print("La lista está ordenada de manera ascendente.")
            else:
                print("La lista no está ordenada de manera ascendente.")
        elif opcion == "14":
            lista_elementos = [float(x) for x in input("Ingrese los elementos separados por espacios: ").split()]
            contador_elementos = contar_elementos(lista_elementos)
            print(f"Conteo de elementos: {contador_elementos}")
        elif opcion == "15":
            matriz1 = []
            matriz2 = []
            print("Ingrese los valores de la matriz 1:")
            while True:
                fila = input("Ingrese una fila de números separados por espacios (o 'q' para terminar): ")
                if fila == "q":
                    break
                matriz1.append([float(x) for x in fila.split()])
            print("Ingrese los valores de la matriz 2:")
            while True:
                fila = input("Ingrese una fila de números separados por espacios (o 'q' para terminar): ")
                if fila == "q":
                    break
                matriz2.append([float(x) for x in fila.split()])
            resultado = sumar_matrices(matriz1, matriz2)
            print(f"Matriz resultante de la suma: {resultado}")
        elif opcion == "16":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Llamamos a la función menu para iniciar el programa
menu()
