"""1. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre 
su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""
def simbolo_divisa():
    divisas = [
    {'nombre': 'Euro', 'simbolo': '€'},
    {'nombre': 'Dollar', 'simbolo': '$'},
    {'nombre': 'Yen', 'simbolo': '¥'}
    ]

    nombre_divisa = input("Ingrese una divisa: ")
    
    encontrada = False
    
    for divisa in divisas:
        if divisa['nombre'].lower() == nombre_divisa.lower():
            print(f"nombre de la divisa {divisa['nombre']} el simbolo es  {divisa['simbolo']}")
            encontrada= True
            break
    if not encontrada:
        print("divisa no encontrada")

# simbolo_divisa()

"""2. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla 
el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
def cliente():
    usuario = {}
    
    try:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        direccion = input("Ingrese su dirección: ")
        telefono = int(input("Ingrese su número de teléfono: "))
        
        if not (isinstance(edad, int) and isinstance(telefono, int)):
            raise ValueError("La edad y el teléfono deben ser valores numéricos.")
        
        usuario['nombre'] = nombre
        usuario['edad'] = edad
        usuario['direccion'] = direccion
        usuario['telefono'] = telefono
        
    except Exception as e:
        print("Error:", e)
        cliente()
        
    else:
        print(f"{usuario['nombre']} \ntiene {usuario['edad']} años \n vive en {usuario['direccion']} \nnúmero de teléfono es {usuario['telefono']}.")
        
# cliente()

"""3. Escribir un programa que guarde en un diccionario los precios de las verduras de la tabla, pregunte al usuario por una verdura, un número de kilos y
muestre por pantalla el precio a pagar. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Verdura               Precio (Kg)
Brócoli                2500 COP
Pimentón           1250 COP
Arveja                 3500 COP
"""
def caja_mercado():
    precios_verduras = {'brocoli': 2500, 'pimenton': 1250, 'arveja': 3500}
    verdura = input("Ingrese el nombre de la verdura: ")
    
    if verdura in precios_verduras:
        kilos = float(input("Ingrese el número de kilos: "))
        precio_por_kilo = precios_verduras[verdura]
        precio_total = kilos * precio_por_kilo
        print(f"El precio a pagar de {kilos} kilos de {verdura} es: {precio_total} COP")
    else:
        print("La verdura no está en el diccionario")
        
# caja_mercado()

"""4. Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono,
correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
"""persona ={}

nombre= input("ingrese su nombre : ")
persona['nombre']=nombre
print("--------------------------------------")
print(f"nombre : {persona['nombre']}")
print("--------------------------------------")

edad= input("ingrese su edad : ")
persona['edad']=edad
print("--------------------------------------")
print(f"edad : {persona['edad']}")
print("--------------------------------------")

genero= input("ingrese su genero : ")
persona['genero']=genero
print("--------------------------------------")
print(f"genero : {persona['genero']}")
print("--------------------------------------")

telefono= input("ingrese su telefono : ")
persona['telefono']=telefono
print("--------------------------------------")
print(f"telefono : {persona['telefono']}")
print("--------------------------------------")

email= input("ingrese su email : ")
persona['email']=email
print("--------------------------------------")
print(f"email : {persona['email']}")
print("--------------------------------------")
"""
#-----------------------------------------------------
def persona_n ():
    persona = {}
    while True:
        clave = input("Ingrese el nombre del dato: ")
        valor = input("Ingrese el valor del dato: ")
        print("inserte el 0 para salir")
        if valor == '0':
            break
        persona[clave] = valor
        print(persona)

# persona_n()

"""5. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par
al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total
"""
def cesta():
    cesta = {}

    while True:
        articulo = input("Ingrese el nombre del artículo (o 'terminar' para salir): ")
        if articulo == 'terminar':
            break
        precio = float(input("Ingrese el precio del artículo: "))
        cesta[articulo]=precio

        costo_total = sum(cesta.values())
        for articulo , precio in cesta.items():
            print(f"articulo : {articulo} precio : {precio} ")
            print(f" costo total : {costo_total}")

"""6. Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde 
la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir
una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá
al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación 
el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""
def factura():
    facturas={}
    cobrado = 0
    pendiente = 0

    while True:
        print(":::::::::MENU:::::::::")
        print("ingrese la opcion que desea realizar")
        opcion = input("1. añadir factura \n2. pagar factura \n3.terminar\n")
        if opcion == '1':
            numero_factura= int(input("ingrese el numero de factura : "))
            coste_factura = int(input("ingrese coste de factura : "))
            facturas[numero_factura]=coste_factura
            pendiente +=  coste_factura 
        elif opcion == '2':
            numero_factura= int(input("ingrese el numero de factura a pagar: "))
            if numero_factura in facturas:
                coste_factura = facturas.pop(numero_factura)
                cobrado += coste_factura
                pendiente -= coste_factura 
            else:
                print("factura no encontrada")
        elif opcion == '3':
            break
        else:
            print("opcion invalida")
    
    print(f" cantidad cobrada hasta el momento : {cobrado}")
    print(f" cantidad pendiente de cobro : {pendiente}")
    
# factura()

        
"""7. Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el 
que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función 
de la opción elegida el programa tendrá que hacer lo siguiente:Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base
de datos.Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.Preguntar por el NIF del cliente y mostrar sus datos.Mostrar lista de
todos los clientes de la base datos con su NIF y nombre.Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.Terminar el programa."""

def cliente ():

    clientes = {}

    while True:
        print("::::::::::::::::::::MENU::::::::::::::::::::")
        print("1. Añadir cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar cliente")
        print("4. Listar todos los clientes")
        print("5. Listar clientes preferentes")
        print("6. Terminar")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            nif = input("Ingrese el NIF del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            preferente = input("¿Es cliente preferente? (True/False): ").lower() == "true"

            cliente = {
                "nombre": nombre,
                "dirección": direccion,
                "teléfono": telefono,
                "correo": correo,
                "preferente": preferente
            }

            clientes[nif] = cliente

        elif opcion == "2":
            nif = input("Ingrese el NIF del cliente que deseaa eliminar: ")
            if nif in clientes:
                del clientes[nif]
            else:
                print("nif no encontrado")
        elif opcion == "3":
            nif = input("Ingrese el NIF del cliente que deseaa mostrar: ")
            if nif in clientes:
                print("datos del cliente:")
                print(clientes[nif])
            else:
                print("nif no encontrado")
        elif opcion == "4":
            for nif in clientes:
                print("datos del cliente:")
                print(clientes[nif])
        elif opcion == "5":
            for nif in clientes:
                print("datos del cliente:")
                if clientes[nif]["preferente"]:
                    print(clientes[nif])
            """print("Lista de clientes preferentes:")
                    for nif, cliente in clientes.items():
                        if cliente["preferente"]:
                            print(f"NIF: {nif}, Datos: {cliente}")"""
        elif opcion == "6":
            break
        else:
            print("opcion invalida")
            
# cliente()