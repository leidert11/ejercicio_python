"""Crea un menú que se repita hasta que el usuario ingrese la opción de salida (a tu elección) y utilice una función para cada opción válida. Las funcionalidades son:
Mostrar cuántas empresas tienen más de 10 empleados en Recursos Humanos
Mostrar el promedio de empleados por departamento (teniendo en cuenta todas las empresas para cada calculo)
Mostrar cuántas empresas tienen el doble o más del doble de empleados en operaciones con respecto a ventas
Mostrar una nueva estructura de datos reorganizada donde las llaves del diccionario principal no sea empresas sino por departamento.
"""

Empresas = {

    "Empresa 1": [
                    {"departamento": "Recursos Humanos", "empleados": 5}, 
                    {"departamento": "Contabilidad", "empleados": 4}, 
                    {"departamento": "Ventas", "empleados": 10}, 
                    {"departamento": "Operaciones", "empleados": 25}],

    "Empresa 2": [
                    {"departamento": "Recursos Humanos", "empleados": 10},
                    {"departamento": "Contabilidad", "empleados": 15},
                    {"departamento": "Ventas", "empleados": 25}, 
                    {"departamento": "Operaciones", "empleados": 41}],

    "Empresa 3": [
                    {"departamento": "Recursos Humanos", "empleados": 8}, 
                    {"departamento": "Contabilidad", "empleados": 20},
                    {"departamento": "Ventas", "empleados": 32},
                    {"departamento": "Operaciones", "empleados": 56}],

    "Empresa 4": [
                    {"departamento": "Recursos Humanos", "empleados": 5},
                    {"departamento": "Contabilidad", "empleados": 8},
                    {"departamento": "Ventas", "empleados": 15}, 
                    {"departamento": "Operaciones", "empleados": 29}],

    "Empresa 5": [
                    {"departamento": "Recursos Humanos", "empleados": 20},
                    {"departamento": "Contabilidad", "empleados": 35},
                    {"departamento": "Ventas", "empleados": 58},
                    {"departamento": "Operaciones", "empleados": 97}
                    ]

}
    

def mostrar_empresas_recursos_humanos():
    # Función para mostrar cuántas empresas tienen más de 10 empleados en el departamento de "Recursos Humanos"
    contador_empresas_recursos_humanos = 0

    for empresa, departamentos in Empresas.items():
        # Iteramos por cada empresa y sus departamentos
        for departamento in departamentos:
            # Buscamos el departamento "Recursos Humanos" en cada empresa
            if departamento["departamento"] == "Recursos Humanos":
                if departamento["empleados"] > 10:
                    # Si la empresa tiene más de 10 empleados en "Recursos Humanos", aumentamos el contador
                    contador_empresas_recursos_humanos += 1
                    # Usamos break para salir del bucle interno y no contar la misma empresa dos veces

    print(f"Empresas con más de 10 empleados en Recursos Humanos: {contador_empresas_recursos_humanos}")


def calcular_promedio_empleados():
    # Función para calcular el promedio de empleados por departamento
    departamentos_empleados = {}  # Diccionario para almacenar el número de empleados por departamento

    for empresa, departamentos in Empresas.items():
        # Iteramos por cada empresa y sus departamentos
        for departamento in departamentos:
            nombre_departamento = departamento["departamento"]
            empleados_departamento = departamento["empleados"]
            # Si el departamento ya está en el diccionario, agregamos el número de empleados
            # Si no, lo inicializamos con el número de empleados
            departamentos_empleados[nombre_departamento] = departamentos_empleados.get(nombre_departamento, 0) + empleados_departamento

    # Calculamos el promedio de empleados para cada departamento
    for departamento, empleados in departamentos_empleados.items():
        promedio = empleados / len(Empresas)
        print(f"Promedio de empleados en {departamento}: {promedio:.2f}")


def mostrar_empresas_operaciones_ventas():
    # Función para mostrar cuántas empresas tienen el doble o más del doble de empleados en "Operaciones" con respecto a "Ventas"
    contador_empresas_operaciones_ventas = 0

    for empresa, departamentos in Empresas.items():
        # Iteramos por cada empresa y sus departamentos
        empleados_operaciones = 0
        empleados_ventas = 0

        for departamento in departamentos:
            # Buscamos los departamentos "Operaciones" y "Ventas" en cada empresa
            if departamento["departamento"] == "Operaciones":
                empleados_operaciones = departamento["empleados"]
            elif departamento["departamento"] == "Ventas":
                empleados_ventas = departamento["empleados"]

        if empleados_operaciones >= empleados_ventas * 2:
            # Si los empleados en "Operaciones" son el doble o más del doble de los empleados en "Ventas",
            # aumentamos el contador
            contador_empresas_operaciones_ventas += 1

    print(f"Empresas con el doble o más del doble de empleados en Operaciones respecto a Ventas: {contador_empresas_operaciones_ventas}")


def reorganizar_por_departamento():
    # Función para reorganizar el diccionario principal por departamentos
    departamentos_reorganizados = {}

    for empresa, departamentos in Empresas.items():
        # Iteramos por cada empresa y sus departamentos
        for departamento in departamentos:
            nombre_departamento = departamento["departamento"]

            if nombre_departamento not in departamentos_reorganizados:
                # Si el departamento no existe en el nuevo diccionario, lo creamos y le asignamos una lista vacía
                departamentos_reorganizados[nombre_departamento] = []

            # Agregamos el departamento actual a la lista correspondiente en el nuevo diccionario
            departamentos_reorganizados[nombre_departamento].append(departamento)

    # Mostramos la nueva estructura de datos resultante
    print("Nueva estructura de datos reorganizada por departamentos:")
    print(departamentos_reorganizados)


def menu():
    # Función para mostrar el menú y repetirlo hasta que el usuario elija la opción de salida
    while True:
        print("\nMenú:")
        print("1. Mostrar empresas con más de 10 empleados en Recursos Humanos")
        print("2. Calcular promedio de empleados por departamento")
        print("3. Mostrar empresas con el doble o más del doble de empleados en Operaciones respecto a Ventas")
        print("4. Reorganizar el diccionario por departamentos")
        print("5. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            mostrar_empresas_recursos_humanos()
        elif opcion == "2":
            calcular_promedio_empleados()
        elif opcion == "3":
            mostrar_empresas_operaciones_ventas()
        elif opcion == "4":
            reorganizar_por_departamento()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


# Llamamos a la función menu para iniciar el programa
menu()
