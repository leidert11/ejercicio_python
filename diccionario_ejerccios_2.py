"""1. Escribe un programa que solicite al usuario un número entero y calcule su factorial. El factorial es la cantidad que resulta de la multiplicación de determinado número natural por todos los números naturales que le anteceden excluyendo el cero; se representa por n! "el factorial de 4 es 24 (producto de 4 x 3 x 2 x 1)"
"""
"""2. Escribe un programa que genere los primeros 20 términos de la serie de Fibonacci. Se trata de una secuencia infinita de números naturales; a partir del 0 y el 1, se van sumando a pares, de manera que cada número es igual a la suma de sus dos anteriores, de manera que: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
"""
"""3. Escribe un programa que solicite al usuario un número entero y calcule la suma de sus dígitos.
"""
"""4. Escribe un programa que genere los primeros 4 números perfectos. Un número perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos. Dicho de otra forma, un número perfecto es aquel que es amigo de sí mismo. Así, 6 es un número perfecto porque sus divisores propios positivos son 1, 2 y 3; y 6 = 1 + 2 + 3.
"""
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


"""5. Dada la siguiente estructura de datos:"""

calificaciones = {

"Alumno 1": [{"asignatura": "Latin", "calificacion": 8}, {"asignatura": "Castellano", "calificacion": 8}, {"asignatura": "Francés", "calificacion": 9}, {"asignatura": "Inglés", "calificacion": 4}],

"Alumno 2": [{"asignatura": "Latin", "calificacion": 7}, {"asignatura": "Castellano", "calificacion": 6}, {"asignatura": "Francés", "calificacion": 7}, {"asignatura": "Inglés", "calificacion": 2}],

"Alumno 3": [{"asignatura": "Latin", "calificacion": 10}, {"asignatura": "Castellano", "calificacion": 7}, {"asignatura": "Francés", "calificacion": 8}, {"asignatura": "Inglés", "calificacion": 9}],

"Alumno 4": [{"asignatura": "Latin", "calificacion": 4}, {"asignatura": "Castellano", "calificacion": 4}, {"asignatura": "Francés", "calificacion": 3}, {"asignatura": "Inglés", "calificacion": 2}],

"Alumno 5": [{"asignatura": "Latin", "calificacion": 9}, {"asignatura": "Castellano", "calificacion": 8}, {"asignatura": "Francés", "calificacion": 9}, {"asignatura": "Inglés", "calificacion": 6}],

}

"""Muestra por pantalla cuántos alumnos suspendieron cada asignatura
Realiza la media de las notas de cada alumno
Muestra por pantalla los nombres de los alumnos que obtuvieron una nota media superior a 5."""