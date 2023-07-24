# 1 ) Escribe un programa que solicite al usuario dos números enteros e imprima la suma, resta, multiplicación y división de esos números.
# primer_numero = int(input("Ingrese el primer número: "))
# segundo_numero = int(input("Ingrese el segundo número: "))

# operacion=input("escoja una operacion 1) suma 2) resta 3) multiplicación 4) div :  ")

# if operacion=="1":
#     print(primer_numero, "+", segundo_numero)
#     print("La suma es= ", primer_numero + segundo_numero)
# elif operacion=="2":    
#     print(primer_numero, "-", segundo_numero)
#     print("La resta es= ", primer_numero - segundo_numero)
# elif operacion=="3":    
#     print(primer_numero, "*", segundo_numero)
#     print("La multiplicación es= ", primer_numero * segundo_numero)
# elif operacion=="4":    
#     print(primer_numero, "/", segundo_numero)
#     print("La div es= ", primer_numero / segundo_numero)
# else:
#     print("La operación no existe")
    

# 2 ) Crea una lista de nombres de ciudades y luego utiliza un bucle for para imprimir cada ciudad en una línea separada.

# ciudades=["Ciudad de México", "valleduar", "medellin","bogota","cali"]

# for ciudad in ciudades:
#     print("---------------------")
#     print(ciudad)

# 3 ) Escribe una función que tome una cadena de texto y devuelva la cadena invertida.
# def invertir_cadena(cadena):
#     cadena_invertida = cadena[::-1]
#     return cadena_invertida

# # Ejemplo de uso
# texto = "Hola, mundo!"
# cadena_invertida = invertir_cadena(texto)
# print(cadena_invertida)


# #----------------------------------------------------------------
# def invertir_cadena(cadena):
#     cadena_invertida = ""
#     for caracter in cadena:
#         cadena_invertida = caracter + cadena_invertida
#     return cadena_invertida

# # Ejemplo de uso
# texto = "Hola, mundo!"
# cadena_invertida = invertir_cadena(texto)
# print(cadena_invertida)

# 4 ) Crea un diccionario con los nombres de tus amigos como claves y sus edades como valores. Luego, utiliza un bucle for para imprimir el nombre y la edad de cada amigo en una línea separada.

# amigos={
#     "Juan": 22,
#     "Pedro": 23,
#     "Ana": 21,
#     "Maria": 20,
#     "Juanita": 19
# }

# for amigo in amigos:
#     print("---------------------")
#     print(amigo)
#     print(amigos[amigo])
    
# #en caso tal que se desee tener mas de un valor en cada clave, inserta una lista en cada clave.

# datos = {
#     "Juan": [22, "Estudiante"],
#     "Pedro": [23, "Ingeniero"],
#     "Ana": [21, "Abogada"]
# }

# for clave, valor in datos.items():
#     print("---------------------")
#     print("Nombre:", clave)
#     print("Edad:", valor[0])
#     print("Profesión:", valor[1])    
    
# 5 ) Escribe un programa que solicite al usuario una palabra y verifique si es un palíndromo (es decir, se lee igual de izquierda a derecha y de derecha a izquierda).

# palabra = input("Ingrese una palabra: ")

# palabra_invertida = palabra[::-1]

# if palabra == palabra_invertida:
#     print("La palabra es un palíndromo.")
# else:
#     print("La palabra no es un palíndromo.")


# 6 ) Escribe un programa que solicite al usuario una lista de números y calcule el promedio de esos números.

# entrada = input("Ingrese una lista de números separados por espacios: ")

# #dividir la entrada en una lista de numeros individuales
# numeros=entrada.split()

# #convertir los numeros de texto a tipo float
# numeros = [float(numero) for numero in numeros]

# # Calcular el promedio de los números
# promedio = sum(numeros)/len(numeros)

# # Imprimir el resultado
# print("El promedio es: ", promedio)

# 7 ) Crea una función que tome una lista de números y devuelva una nueva lista que contenga solo los números pares.
# def obtener_pares(lista):
#     pares = []
#     for numero in lista:
#         if numero % 2 == 0:
#             pares.append(numero)
#     return pares

# # Ejemplo de uso
# numeros = [12, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = obtener_pares(numeros)
# print(pares)

# 8 ) Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas veces aparece una letra específica en esa cadena.

# texto="hola, mundo! como va la vida , dale espero que bien "
# letra_buscar="l"
# contador = 0
# for cont in texto:
#     if cont == letra_buscar:
#         contador += 1
# print(contador)

# 9 ) Crea una función que tome dos listas y devuelva una nueva lista que contenga elementos comunes entre las dos listas.

# def listas(lista1, lista2):
#     comunes = []
#     for elemento in lista1:
#         if elemento in lista2:
#             comunes.append(elemento)
#     return comunes
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [4, 5, 6, 7, 8]
# resultado = listas(lista1, lista2)
# print(resultado)

# 10 ) Escribe un programa que solicite al usuario una serie de números y encuentre el número más grande y el más pequeño
def encontrar_extremos():
    numeros= input("Ingrese una serie de números separados por espacios: ")
    numeros=numeros.split()

    numeros = [int(numero) for numero in numeros]

    minimo = min(numeros)
    maximo = max(numeros)
    
    return minimo, maximo 

minimo, maximo = encontrar_extremos()
print("El número más pequeño es:", minimo)
print("El número más grande es:", maximo)
