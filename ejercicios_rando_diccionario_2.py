# Diccionario de ejemplo con estructura compleja
diccionario_ejemplo = {
    'lista1': [{'valor': 10}, {'valor': 20}, {'valor': 30}],
    'lista2': [{'valor': 5}, {'valor': 15}],
    'lista3': [{'valor': 25}, {'valor': 35}, {'valor': 40}, {'valor': 50}]
}

# Problema 1: Iterar sobre el diccionario y sumar los valores de 'valor' de cada lista
def suma_valores(diccionario):
    suma_total = 0
    for lista_contenido in diccionario.values():
        for elemento in lista_contenido:
            suma_total += elemento['valor']
    return suma_total

# Problema 2: Encontrar el valor máximo y mínimo en todas las listas
def encontrar_max_min(diccionario):
    valores = []
    for lista_contenido in diccionario.values():
        for elemento in lista_contenido:
            valores.append(elemento['valor'])
    maximo = max(valores)
    minimo = min(valores)
    return maximo, minimo

# Problema 3: Contar cuántos elementos hay en cada lista
def contar_elementos(diccionario):
    conteo = {}
    for lista_nombre, lista_contenido in diccionario.items():
        conteo[lista_nombre] = len(lista_contenido)
    return conteo

# Problema 4: Encontrar la lista con el mayor y menor número de elementos
def encontrar_mayor_menor_lista(diccionario):
    mayor = None
    menor = None
    for lista_nombre, lista_contenido in diccionario.items():
        num_elementos = len(lista_contenido)
        if mayor is None or num_elementos > len(diccionario[mayor]):
            mayor = lista_nombre
        if menor is None or num_elementos < len(diccionario[menor]):
            menor = lista_nombre
    return mayor, menor

# Impresión del diccionario de ejemplo
print("Diccionario de ejemplo:")
print(diccionario_ejemplo)

# Prueba de las soluciones
print("\nProblema 1 - Suma de valores:")
print(suma_valores(diccionario_ejemplo))

print("\nProblema 2 - Valor máximo y mínimo:")
maximo, minimo = encontrar_max_min(diccionario_ejemplo)
print(f"Maximo: {maximo}, Minimo: {minimo}")

print("\nProblema 3 - Conteo de elementos en cada lista:")
print(contar_elementos(diccionario_ejemplo))

print("\nProblema 4 - Lista con mayor y menor número de elementos:")
mayor, menor = encontrar_mayor_menor_lista(diccionario_ejemplo)
print(f"Mayor: {mayor}, Menor: {menor}")
