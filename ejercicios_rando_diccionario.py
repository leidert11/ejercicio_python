# Problema 1: Iterar sobre un diccionario que contiene listas y dentro de esas listas hay otros diccionarios.
# Solución:
def iterar_diccionario(diccionario):
    for llave, lista in diccionario.items():
        print(f"Clave: {llave}")
        for elemento in lista:
            print(f" - Elemento: {elemento}")

# Problema 2: Filtrar los elementos de un diccionario que cumplan con cierta condición.
# Solución:
def filtrar_elementos(diccionario):
    resultado = {llave: lista for llave, lista in diccionario.items() if len(lista) >= 2}
    print(resultado)

# Problema 3: Encontrar el valor máximo de un diccionario que contiene listas con diccionarios.
# Solución:
def encontrar_valor_maximo(diccionario):
    maximo = float('-inf')
    for llave, lista in diccionario.items():
        for elemento in lista:
            if 'valor' in elemento:
                maximo = max(maximo, elemento['valor'])
    print(f"El valor máximo encontrado es: {maximo}")

# Problema 4: Sumar todos los valores de un diccionario que contiene listas con diccionarios.
# Solución:
def sumar_valores(diccionario):
    total = 0
    for llave, lista in diccionario.items():
        for elemento in lista:
            if 'valor' in elemento:
                total += elemento['valor']
    print(f"La suma de todos los valores es: {total}")

# Problema 5: Contar cuántos elementos hay en un diccionario que contiene listas con diccionarios.
# Solución:
def contar_elementos(diccionario):
    total = 0
    for llave, lista in diccionario.items():
        total += len(lista)
    print(f"El número total de elementos es: {total}")

# Diccionario de ejemplo
diccionario_ejemplo = {
    'lista1': [{'valor': 10}, {'valor': 20}, {'valor': 30}],
    'lista2': [{'valor': 5}, {'valor': 15}],
    'lista3': [{'valor': 25}, {'valor': 35}, {'valor': 40}, {'valor': 50}]
}

# Ejecución de las funciones con el diccionario de ejemplo
print("Iteración sobre el diccionario:")
iterar_diccionario(diccionario_ejemplo)

print("\nFiltrar elementos con más de 2 elementos en la lista:")
filtrar_elementos(diccionario_ejemplo)

print("\nEncontrar el valor máximo:")
encontrar_valor_maximo(diccionario_ejemplo)

print("\nSumar todos los valores:")
sumar_valores(diccionario_ejemplo)

print("\nContar el número de elementos:")
contar_elementos(diccionario_ejemplo)
