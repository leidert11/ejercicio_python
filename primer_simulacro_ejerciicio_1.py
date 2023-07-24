
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
    
def menu():
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::MENU:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(":: 1. Mostrar cunatas empresas tienen mas de 10 empleados                                                                                  ::")
    print(":: 2. Mostrar el promedio de empleados por departamento                                                                                    ::")
    print(":: 3. Mostrar cuántas empresas tienen el doble o más del doble de empleados en operaciones con respecto a ventas                           ::")
    print(":: 4. Mostrar una nueva estructura de datos reorganizada donde las llaves del diccionario principal no sea empresas sino por departamento. ::")
    print(":: 5. para terminar                                                                                                                        ::")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    opcion= input("ingrese la opcion deseada : ")
    
    return opcion
    
    
def mostrar_recursos_humanos(x):
    dic = dict(x)
    contador = 0
    for i in dic.keys():
        for j in dic[i]:
            if j['departamento'] == "Recursos Humanos" :
                if j['empleados'] > 10 :
                    contador += 1 
    print("---------------------------------------------------------------------")
    print(" ")
    print(f" {contador} emresas tienen mas de 10 empleados en recursos humanos")
    print(" ")
    print("---------------------------------------------------------------------")
    
def promedio_empleados(x): 
    dic = dict(x)
    acumulador_rh = 0 
    acumulador_cont = 0 
    acumulador_venta = 0 
    acumulador_ope = 0 
    contador_rh = 0 
    contador_cont = 0 
    contador_vent = 0 
    contador_ope = 0 
    for i in dic.keys():
        for j in dic[i]:
            if j['departamento'] == "Recursos Humanos":
                acumulador_rh += j['empleados']
                contador_rh += 1
            elif j['departamento'] == "Contabilidad":
                acumulador_cont += j['empleados']
                contador_cont += 1
                
            elif j['departamento'] == "Ventas":
                acumulador_venta += j['empleados']
                contador_vent += 1
                
            elif j['departamento'] == "Operaciones":
                acumulador_ope += j['empleados']
                contador_ope += 1

    print(" ")            
    print("promedio de empleads : ")
    print("---------------------------------------------------------------------")
    print(" ")            
    print(f"recursos humanos : {acumulador_rh / contador_rh}")    
    print(" ")
    print("---------------------------------------------------------------------")
    print(" ")            
    print(f"contabilidad : {acumulador_cont/contador_cont}")    
    print(" ")
    print("---------------------------------------------------------------------")    
    print(" ")            
    print(f"ventas : {acumulador_venta/contador_vent}")    
    print(" ")
    print("---------------------------------------------------------------------")
    print(" ")            
    print(f"operaciones : {acumulador_ope/contador_ope}")    
    print(" ")
    print("---------------------------------------------------------------------")
    
def doble_ope_ventas(x):
    dic = dict(x)
    for i in dic.keys():
        empleados_ope = 0
        empleados_vent = 0
        for j in dic[i]:
            if j['departamento'] == "Ventas":
                empleados_vent = j['empleados']
            elif j['departamento'] == "Operaciones":
                empleados_ope = j['empleados']
        if empleados_ope >= (empleados_vent*2):
            print("---------------------------------------------------------------------")
            print(" ")            
            print(f"la {i} cumple con el requisito {empleados_vent} ")
        
while True : 
    opcion = menu()
    if opcion == "1":
        mostrar_recursos_humanos(Empresas)
    elif opcion == "2":
        promedio_empleados(Empresas)
    elif opcion == "3":
        doble_ope_ventas(Empresas)
    elif opcion == "5":
        print("saliste del programa")
        break
    else:
        print("opcion invalida")
            
    
    