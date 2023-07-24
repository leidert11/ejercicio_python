# Ejemplo de uso de métodos en diferentes estructuras de datos

# Métodos de la lista (list)
lista = [1, 2, 3, 4, 5]

# append(elemento)
lista.append(6)  # Agrega el elemento 6 al final de la lista
print(lista)  # Resultado: [1, 2, 3, 4, 5, 6]

# extend(iterable)
lista.extend([7, 8, 9])  # Agrega los elementos del iterable al final de la lista
print(lista)  # Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert(posición, elemento)
lista.insert(2, 10)  # Inserta el elemento 10 en la posición 2 de la lista
print(lista)  # Resultado: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# remove(elemento)
lista.remove(5)  # Elimina la primera aparición del elemento 5 de la lista
print(lista)  # Resultado: [1, 2, 10, 3, 4, 6, 7, 8, 9]

# pop([índice])
elemento = lista.pop()  # Elimina y devuelve el último elemento de la lista
print(elemento)  # Resultado: 9
print(lista)  # Resultado: [1, 2, 10, 3, 4, 6, 7, 8]

# index(elemento[, inicio[, fin]])
indice = lista.index(3)  # Devuelve el índice de la primera aparición del elemento 3 en la lista
print(indice)  # Resultado: 3

# count(elemento)
conteo = lista.count(10)  # Cuenta el número de veces que aparece el elemento 10 en la lista
print(conteo)  # Resultado: 1

# sort()
lista.sort()  # Ordena los elementos de la lista de forma ascendente
print(lista)  # Resultado: [1, 2, 3, 4, 6, 7, 8, 10]

# reverse()
lista.reverse()  # Invierte el orden de los elementos de la lista
print(lista)  # Resultado: [10, 8, 7, 6, 4, 3, 2, 1]

# clear()
lista.clear()  # Elimina todos los elementos de la lista
print(lista)  # Resultado: []

# Métodos de la tupla (tuple)
tupla = (1, 2, 3, 4, 5)

# Los métodos de las listas también se pueden aplicar a las tuplas
# Aunque las tuplas son inmutables, por lo que no se pueden modificar directamente

# Métodos del conjunto (set)
conjunto = {1, 2, 3, 4, 5}

# add(elemento)
conjunto.add(6)  # Agrega el elemento 6 al conjunto
print(conjunto)  # Resultado: {1, 2, 3, 4, 5, 6}

# remove(elemento)
conjunto.remove(5)  # Elimina el elemento 5 del conjunto
print(conjunto)  # Resultado: {1, 2, 3, 4, 6}

# pop()
elemento = conjunto.pop()  # Elimina y devuelve un elemento aleatorio del conjunto
print(elemento)  # Resultado: Alguno de los elementos restantes en el conjunto
print(conjunto)  # Resultado: {1, 2, 3, 4}

# clear()
conjunto.clear()  # Elimina todos los elementos del conjunto
print(conjunto)  # Resultado: set()

# Métodos del diccionario (dict)
#(la estrutura es (key : value) y separamos por comas )
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
    }

# keys()
claves = diccionario.keys()  # Devuelve una vista de todas las claves del diccionario
print(claves)  # Resultado: dict_keys(['nombre', 'edad', 'ciudad'])

# values()
valores = diccionario.values()  # Devuelve una vista de todos los valores del diccionario
print(valores)  # Resultado: dict_values(['Juan', 30, 'Madrid'])

# items()
items = diccionario.items()  # Devuelve una vista de pares (clave, valor) de todos los elementos del diccionario
print(items)  # Resultado: dict_items([('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Madrid')])

# get(clave[, valor_predeterminado])
valor = diccionario.get("edad")  # Devuelve el valor asociado a la clave "edad"
print(valor)  # Resultado: 30

# pop(clave[, valor_predeterminado])
valor = diccionario.pop("ciudad")  # Elimina y devuelve el valor asociado a la clave "ciudad"
print(valor)  # Resultado: "Madrid"
print(diccionario)  # Resultado: {'nombre': 'Juan', 'edad': 30}

# update(diccionario) o update(iterable)
diccionario.update({"apellido": "Pérez"})  # Agrega los pares clave-valor del diccionario al diccionario actual
print(diccionario)  # Resultado: {'nombre': 'Juan', 'edad': 30, 'apellido': 'Pérez'}

# clear()
diccionario.clear()  # Elimina todos los elementos del diccionario
print(diccionario)  # Resultado: {}

