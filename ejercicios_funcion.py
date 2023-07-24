"""
1. Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""

def factorial():
    numero = int(input("ingrese un numero "))
    
    if numero == 0:
        return  1  
    else:
        resultado = 1
        for i in range(1,numero+1):
            resultado = resultado*i
    return resultado

# resultado = factorial()

# print(f"el resultado factorial es : {resultado}")

#::::::::::::::::::::::::::::::::::::::::

def factorial(numero):
    if numero == 0:
        return  1  
    else:
        resultado = 1
        for i in range(1,numero+1):
            resultado = resultado*i
    return resultado

# resultado = factorial(10)

# print(f"el resultado factorial es : {resultado}")    

   
"""
2. Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y
el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""
# def calcular_factura(cantidad, porcentaje_iva=21):
#     if cantidad <= 0:
#         raise ValueError("La cantidad de la factura debe ser un número positivo mayor que cero.")
    
#     iva = cantidad * porcentaje_iva / 100
#     factura_total = cantidad + iva
#     return factura_total 


# factura_total = None

# try:
#     cantidad = float(input("Digite la cantidad de su factura: "))
#     factura_total = calcular_factura(cantidad)
# except ValueError as ve:
#     print(f"Error: {ve}")
# finally:
#     print(f"Su factura total junto con el IVA es: {factura_total}")
#     print(":::::::GRACIAS POR SU COMPRA:::::::")


"""
3. Escribir una función que calcule el área de un cuadrado y otra que calcule el volumen de un cubo usando la primera función.
"""
# def calcular_area_cuadrado(lado):
#     if lado <= 0:
#         raise ValueError("por favor ingresa valores positivos")
#     area= lado * lado
#     return area

# def calcular_volumen_cubo(lado):
#     if lado <= 0:
#         raise ValueError("por favor ingresa valores positivos")
#     area= calcular_area_cuadrado(lado)
#     volumen = area * lado
#     return volumen

# area = None
# volumen = None

# try:
#     lado = float(input("Ingrese la longitud del lado del cuadrado y del cubo: "))
#     area = calcular_area_cuadrado(lado)
#     volumen= calcular_volumen_cubo(lado)
#     print(f"El área de un cuadrado con lado {lado} es: {area}")
#     print(f"El volumen de un cubo con lado {lado} es: {volumen}")
# except Exception as e:
#     print(f"Error : {e}")
# finally:
#     print(f"el area de un cuadrdado es: {area}\n con un volumen de : {volumen}")
"""
4. Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""
def calcular_media(numeros):
    suma= 0
    cont = 0
    
    for numero in numeros:
        suma += numero
        cont += 1
    
    calcular= suma / cont
    
    return calcular

muestra_numeros = [2, 5, 8, 10]
resultado_media = calcular_media(muestra_numeros)
print(f"La media de la muestra {muestra_numeros} es: {resultado_media}")

"""
5. Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
"""

def calcular_cuadrados(muestra):
    cuadrados = [numero ** 2 for numero in muestra]
    return cuadrados

muestra_numeros = [1, 2, 3, 4, 5]
cuadrados_resultado = calcular_cuadrados(muestra_numeros)
print(f"Cuadrados de la muestra {muestra_numeros}: {cuadrados_resultado}")



