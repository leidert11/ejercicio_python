# Problema 1: Encontrar el camino más corto entre dos nodos en un grafo ponderado utilizando el algoritmo de Dijkstra.
# Solución:
import heapq

def dijkstra(grafo, nodo_inicial):
    distancia = {nodo: float('inf') for nodo in grafo}
    distancia[nodo_inicial] = 0
    cola = [(0, nodo_inicial)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if distancia_actual > distancia[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual].items():
            distancia_total = distancia_actual + peso
            if distancia_total < distancia[vecino]:
                distancia[vecino] = distancia_total
                heapq.heappush(cola, (distancia_total, vecino))

    return distancia

# Problema 2: Resolver el problema de la mochila (Knapsack problem) utilizando una búsqueda exhaustiva (combinaciones).
# Solución:
def mochila_combinaciones(capacidad, pesos, valores):
    n = len(pesos)
    mejor_valor = 0
    mejor_combinacion = None

    for i in range(2 ** n):
        combinacion = format(i, f'0{n}b')
        peso_total = sum(pesos[j] for j in range(n) if combinacion[j] == '1')
        valor_total = sum(valores[j] for j in range(n) if combinacion[j] == '1')

        if peso_total <= capacidad and valor_total > mejor_valor:
            mejor_valor = valor_total
            mejor_combinacion = combinacion

    indices_mejor_combinacion = [i for i in range(n) if mejor_combinacion[i] == '1']
    return indices_mejor_combinacion

# Problema 3: Resolver el problema del viajante de comercio (Traveling Salesman Problem) utilizando el algoritmo genético.
# Solución:
import random

def distancia_ciudades(ciudad1, ciudad2):
    return abs(ciudad1[0] - ciudad2[0]) + abs(ciudad1[1] - ciudad2[1])

def calcular_distancia_recorrido(ciudades, recorrido):
    distancia_total = 0
    for i in range(len(recorrido) - 1):
        distancia_total += distancia_ciudades(ciudades[recorrido[i]], ciudades[recorrido[i + 1]])
    return distancia_total

def crear_poblacion_inicial(ciudades, tamano_poblacion):
    poblacion = []
    indices_ciudades = list(range(len(ciudades)))

    for _ in range(tamano_poblacion):
        recorrido = random.sample(indices_ciudades, len(indices_ciudades))
        poblacion.append(recorrido)

    return poblacion

def seleccionar_padres(poblacion, ciudades):
    padres = []
    for _ in range(len(poblacion) // 2):
        padre1 = min(poblacion, key=lambda x: calcular_distancia_recorrido(ciudades, x))
        poblacion.remove(padre1)
        padre2 = min(poblacion, key=lambda x: calcular_distancia_recorrido(ciudades, x))
        poblacion.remove(padre2)
        padres.append((padre1, padre2))
    return padres

def cruzar_padres(padres):
    hijos = []
    for padre1, padre2 in padres:
        punto_cruce = random.randint(1, len(padre1) - 1)
        hijo1 = padre1[:punto_cruce] + [c for c in padre2 if c not in padre1[:punto_cruce]]
        hijo2 = padre2[:punto_cruce] + [c for c in padre1 if c not in padre2[:punto_cruce]]
        hijos.extend([hijo1, hijo2])
    return hijos

def mutar_hijos(hijos, probabilidad_mutacion):
    for i in range(len(hijos)):
        if random.random() < probabilidad_mutacion:
            indices_mutar = random.sample(range(len(hijos[i])), 2)
            hijos[i][indices_mutar[0]], hijos[i][indices_mutar[1]] = hijos[i][indices_mutar[1]], hijos[i][indices_mutar[0]]
    return hijos

def algoritmo_genetico(ciudades, tamano_poblacion, num_generaciones, probabilidad_mutacion):
    poblacion = crear_poblacion_inicial(ciudades, tamano_poblacion)

    for _ in range(num_generaciones):
        padres = seleccionar_padres(poblacion, ciudades)
        hijos = cruzar_padres(padres)
        hijos_mutados = mutar_hijos(hijos, probabilidad_mutacion)
        poblacion = hijos_mutados

    mejor_recorrido = min(poblacion, key=lambda x: calcular_distancia_recorrido(ciudades, x))
    return mejor_recorrido

# Problema 4: Implementar una función que calcule el área de la unión de rectángulos en un plano cartesiano.
# Solución:
def area_union_rectangulos(rectangulos):
    def area_rectangulo(rectangulo):
        return (rectangulo[2] - rectangulo[0]) * (rectangulo[3] - rectangulo[1])

    def area_interseccion(rectangulo1, rectangulo2):
        x1 = max(rectangulo1[0], rectangulo2[0])
        y1 = max(rectangulo1[1], rectangulo2[1])
        x2 = min(rectangulo1[2], rectangulo2[2])
        y2 = min(rectangulo1[3], rectangulo2[3])
        if x1 < x2 and y1 < y2:
            return (x2 - x1) * (y2 - y1)
        return 0

    area_total = 0
    for i, rectangulo1 in enumerate(rectangulos):
        area_total += area_rectangulo(rectangulo1)
        for j in range(i + 1, len(rectangulos)):
            area_total -= area_interseccion(rectangulo1, rectangulos[j])

    return area_total
