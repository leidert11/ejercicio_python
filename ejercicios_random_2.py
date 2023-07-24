# Problema 1: Encontrar el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.
# Solución:
def mcd_euclides(a, b):
    if b == 0:
        return a
    else:
        return mcd_euclides(b, a % b)

# Problema 2: Encontrar el mínimo común múltiplo (MCM) de dos números.
# Solución:
def mcm(a, b):
    return abs(a * b) // mcd_euclides(a, b)

# Problema 3: Encontrar el n-ésimo número de la secuencia de Fibonacci utilizando recursión.
# Solución:
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

# Problema 4: Leer un archivo de texto y contar la cantidad de veces que aparece cada palabra.
# Solución:
def contar_palabras_archivo(nombre_archivo):
    contador = {}
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            palabras = linea.strip().split()
            for palabra in palabras:
                palabra = palabra.lower()
                if palabra in contador:
                    contador[palabra] += 1
                else:
                    contador[palabra] = 1
    return contador

# Problema 5: Encontrar todos los subconjuntos de un conjunto dado.
# Solución:
def encontrar_subconjuntos(conjunto):
    subconjuntos = [[]]
    for elemento in conjunto:
        nuevos_subconjuntos = [subconjunto + [elemento] for subconjunto in subconjuntos]
        subconjuntos.extend(nuevos_subconjuntos)
    return subconjuntos

# Problema 6: Implementar una función de ordenamiento Merge Sort.
# Solución:
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    lista_ordenada = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista_ordenada.append(izquierda[i])
            i += 1
        else:
            lista_ordenada.append(derecha[j])
            j += 1

    lista_ordenada.extend(izquierda[i:])
    lista_ordenada.extend(derecha[j:])
    return lista_ordenada

# Problema 7: Encontrar la longitud de la secuencia de Collatz para un número dado.
# Solución:
def collatz_secuencia(numero):
    secuencia = [numero]
    while numero != 1:
        if numero % 2 == 0:
            numero = numero // 2
        else:
            numero = 3 * numero + 1
        secuencia.append(numero)
    return secuencia

# Problema 8: Implementar una función para verificar si un número es primo utilizando el algoritmo de Miller-Rabin.
# Solución:
def es_primo_miller_rabin(n, k=10):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Problema 9: Implementar una función que genere una contraseña segura de longitud n.
# Solución:
import random
import string

def generar_contrasena_segura(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Problema 10: Resolver el juego de las Torres de Hanoi utilizando recursión.
# Solución:
def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    torres_hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    torres_hanoi(n - 1, auxiliar, destino, origen)

# Problema 11: Implementar una función para calcular la suma de los dígitos de un número entero.
# Solución:
def suma_digitos(numero):
    suma = 0
    while numero != 0:
        suma += numero % 10
        numero //= 10
    return suma

# Problema 12: Implementar una función para determinar si un número es un número de Harshad.
# Solución:
def es_harshad(numero):
    return numero % suma_digitos(numero) == 0

# Problema 13: Encontrar la subsecuencia creciente más larga en una lista de números.
# Solución:
def subsecuencia_creciente_mas_larga(lista):
    n = len(lista)
    subsecuencia = [1] * n

    for i in range(1, n):
        for j in range(i):
            if lista[i] > lista[j] and subsecuencia[i] < subsecuencia[j] + 1:
                subsecuencia[i] = subsecuencia[j] + 1

    maximo = max(subsecuencia)
    indice_maximo = subsecuencia.index(maximo)

    secuencia_creciente = [lista[indice_maximo]]
    maximo -= 1

    for i in range(indice_maximo - 1, -1, -1):
        if subsecuencia[i] == maximo and lista[i] < secuencia_creciente[-1]:
            secuencia_creciente.append(lista[i])
            maximo -= 1

    return secuencia_creciente[::-1]

# Problema 14: Implementar una función que convierta una lista de números a una cadena de caracteres.
# Solución:
def lista_a_cadena(lista):
    cadena = ""
    for elemento in lista:
        cadena += str(elemento)
    return cadena

# Problema 15: Resolver el problema de la mochila (Knapsack problem) utilizando programación dinámica.
# Solución:
def mochila(capacidad, pesos, valores):
    n = len(pesos)
    matriz = [[0] * (capacidad + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            if pesos[i - 1] <= w:
                matriz[i][w] = max(valores[i - 1] + matriz[i - 1][w - pesos[i - 1]], matriz[i - 1][w])
            else:
                matriz[i][w] = matriz[i - 1][w]

    resultado = []
    w = capacidad
    for i in range(n, 0, -1):
        if matriz[i][w] != matriz[i - 1][w]:
            resultado.append(i - 1)
            w -= pesos[i - 1]

    resultado.reverse()
    return resultado

# Problema 16: Implementar una función que calcule la distancia Euclidiana entre dos puntos en un plano cartesiano.
# Solución:
import math

def distancia_euclidiana(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
