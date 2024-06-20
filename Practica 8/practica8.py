import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

#Ejercicio 1.1
def contar_lineas(nombre_archivo:str) -> int:
    mi_archivo = open(nombre_archivo, "r+")
    archivo_string = mi_archivo.readlines()
    i: int = len(archivo_string)
    return i


#Ejercicio 1.2
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    res: bool = False
    lista_palabras: list[str] = mis_palabras(nombre_archivo)
    for palabra_lista in lista_palabras:
        if (palabra == palabra_lista):
            res = True
    return res

def mis_palabras(nombre_archivo:str) -> list[str]:
    arch = open(nombre_archivo,"r+")
    letra = arch.read(1)
    palabra = ""
    palabras : list = []
    while (letra != ""):
        if (letra != " " and letra != "\n"):
            palabra = palabra + letra
        else: 
            palabras.append(palabra)
            palabra = ""
        letra = arch.read(1)
    arch.close()
    return palabras


#Ejercicio 1.3
def cantidad_aparciciones(palabra: str, nombre_archivo: str) -> int:
    res: int = 0
    lista_palabras: list[str] = mis_palabras(nombre_archivo)
    for palabra_lista in lista_palabras:
        if (palabra == palabra_lista):
            res += 1
    return res




#PILAS
#Ejercicio 8
def generar_nros_al_azar(cantidad: int, desde:int, hasta:int):
    p = Pila()
    i: int = 0
    while i < cantidad:
        num: int = random.randint(desde, hasta) 
        p.put(num)
        i+= 1
    print (p.queue)
    return p

#Construir Pila
def construir_pila(p: Pila) -> list:
    lista_elementos: list = []
    while(not(p.empty())):
        elemento = p.get()
        lista_elementos.append(elemento)
    return lista_elementos


#Ejercicio 9
def cantidad_elementos(p: Pila) -> int:
    lista_elementos: list = []
    while(not(p.empty())):
        elemento = p.get()
        lista_elementos.append(elemento)
    cantidad: int = len(lista_elementos)
    for i in range(cantidad):
        p.put(lista_elementos[cantidad - i -1]) 
    return cantidad


#Ejercicio 10
def buscar_el_maximo(p: Pila[int]) -> int:
    lista_elementos: list = []
    while(not(p.empty())):
        elemento = p.get()
        lista_elementos.append(elemento)

    cantidad: int = len(lista_elementos)
    maximo: int = lista_elementos[0]

    for i in range(cantidad):
        p.put(lista_elementos[cantidad - i -1])
    print(p.queue)

    for i in range (cantidad - 1):
        if (maximo >= lista_elementos[i+1]):
            maximo = maximo
        else: 
            maximo = lista_elementos[i+1]

    return maximo
    
#Ejercicio 11
def esta_bien_balanceada(s: str) -> bool:
    res: bool
    parentesis_abierto = Pila()
    
    for caracter in s:
        if (caracter == "(" or caracter == ")"):
            parentesis_abierto.put(caracter)
    
    cantidad_original: int = cantidad_elementos((parentesis_abierto))
    if(( cantidad_original % 2 )!= 0):
        res= False
    
    mitad: int = cantidad_original
    parentesis_cerrado = Pila() 
    
    while(mitad != (cantidad_original / 2)):
        parentesis_cerrado.put(parentesis_abierto.get())
        mitad = mitad - 1

    if(son_todos_iguales(parentesis_abierto) and son_todos_iguales(parentesis_cerrado)):
        res= True
    else: 
        res = False

    
    return res


def son_todos_iguales(pila: Pila[int]) -> bool:
    lista_parentesis = []
    res: bool = False
    while(not(pila.empty())):
        lista_parentesis.append(pila.get())
    for i in range(len(lista_parentesis) - 1):
        if (lista_parentesis[i] == lista_parentesis[i+1]):
            res = True
        else:
            res = False
            break
    for i in range(len(lista_parentesis)):
        pila.put(lista_parentesis[len(lista_parentesis) - i - 1])
    return res


#Ejercicio 12
def evaluar_expresion(s: str) -> bool:
    pila = Pila()
    for token in s:
        if (token >= "0" and token <= "9"):
            pila.put(int(token))

        elif(es_operador(token)):
            if(token == "+"):
                operando1: int = pila.get()
                operando2: int = pila.get()
                suma: int = operando1 + operando2
                pila.put(suma)
            if(token == "-"):
                operando1: int = pila.get()
                operando2: int = pila.get()
                resta: int = operando2 - operando1
                pila.put(resta)
            if(token == "*"):
                operando1: int = pila.get()
                operando2: int = pila.get()
                prod: int = operando1 * operando2
                pila.put(prod)
            if(token == "/"):
                operando1: int = pila.get()
                operando2: int = pila.get()
                div: int = operando2 / operando1
                pila.put(div)
    
    return pila.queue

def es_operador(s:str) -> bool:
    res: bool
    if(s == "+" or s == "-" or s== "*" or s == "/"):
        res = True
    else:
        res = False
    return res


#COLAS
#Ejercicio 13
def generar_nros_al_azar_cola(cantidad: int, desde: int, hasta: int) -> Cola:
    c = Cola()
    i: int = 0
    while i < cantidad:
        num: int = random.randint(desde, hasta)
        c.put(num)
        i+=1
    return c


#Ejercicio 14
def cantidad_elementos_cola(c: Cola) -> int:
    lista_cola = []
    while(not(c.empty())):
        lista_cola.append(c.get())
    cantidad: int = len(lista_cola)
    for elemento in lista_cola:
        c.put(elemento)
    return cantidad


#Ejercicio 15
def buscar_el_maximo(c: Cola[int]) -> int:
    lista_maximo = []
    print(c.queue)
    while(not(c.empty())):
        lista_maximo.append(c.get())
    
    maximo: int = lista_maximo[0]
    for i in range(len(lista_maximo) - 1):
        if (maximo >= lista_maximo [i+1]):
            maximo = maximo
        else:
            maximo = lista_maximo[i+1]
    
    for elemento in lista_maximo:
        c.put(elemento)
    
    print(c.queue)
    return maximo


#Ejercicio 17

#Ejercicio 18
def atencion_a_clientes_lista() -> Cola[(str, int, bool, bool)]:
    cola_clientes = Cola()
    lista_clientes: list[(str, int, bool, bool)] = []
    nombre : str = input("Ingrese su nombre:")

    while (nombre != "X"):
        dni: int = int(input("Ingrese su DNI:"))
        tipo_de_cuenta_in = input("Es su cuenta preferencial?:")
        if(tipo_de_cuenta_in == "si"):
            tipo_de_cuenta: bool = True
        elif(tipo_de_cuenta_in == "no"):
            tipo_de_cuenta : bool = False

        prioridad_in = input("Necesita prioridad?(Adulto +65 años, embaraxada o movilidad reducida):")
        if(prioridad_in == "si"):
            prioridad: bool = True
        elif(prioridad_in == "no"):
            prioridad: bool = False
            
        lista_clientes.append((nombre, dni, tipo_de_cuenta, prioridad))
        nombre = input("Ingrese su nombre:")
    
    for cliente in lista_clientes:
        cola_clientes.put(cliente)
    
    return cola_clientes


def atencion_a_clientes(c: Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    lista_cola: list = []
    cola_prioridad = Cola()
    cola_preferencia = Cola()
    cola_resto = Cola()
    cola_final = Cola()
    while(not(c.empty())):
        cliente = c.get()
        lista_cola.append(cliente)
        if(cliente[3] == True):
            cola_prioridad.put(cliente)
        elif(cliente[2] == True):
            cola_preferencia.put(cliente)
        else:
            cola_resto.put(cliente)
    
    for cliente in lista_cola:
        c.put(cliente)

    while(not(cola_prioridad.empty())):
        prioridad = cola_prioridad.get()
        cola_final.put(prioridad)

    while(not(cola_preferencia.empty())):
        preferencia = cola_preferencia.get()
        cola_final.put(preferencia)

    while(not(cola_resto.empty())):
        resto = cola_resto.get()
        cola_final.put(resto)

    return cola_final.queue


#DICCIONARIOS 
def pertenece(lista: list, x) -> bool:
    res: bool = False
    i: int = 0
    while (i<(len(lista))):
        if (x == lista[i]):
            res = True
        i+= 1
    return res

#Ejercicio 19
def agrupar_por_longitud(nombre_archivo: str) -> dict:
    diccionario = {}
    lista_palabras = mis_palabras(nombre_archivo)
    lista_longitudes = []
    for palabra in lista_palabras:
        longitud: int = len(palabra)
        if (not(pertenece(lista_longitudes, longitud))):
            diccionario[longitud] = 1
            lista_longitudes.append(longitud)
        else:
            diccionario[longitud] = diccionario[longitud] + 1
    return diccionario

#Ejercicio 21
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    diccionario = cantidad_de_apariciones(nombre_archivo)
    lista_tuplas = []
    for palabra, cantidad in diccionario.items():
        lista_tuplas.append((palabra, cantidad))
    
    maximo: int = lista_tuplas[0][1] 
    res: str = lista_tuplas[0][0]
    for i in range((len(lista_tuplas)) -1):
        if(maximo < lista_tuplas[i+1][1]):
            maximo = lista_tuplas[i+1][1]
            res = lista_tuplas[i+1][0]
    return res


def cantidad_de_apariciones(nombre_archivo: str) -> dict:
    diccionario = {}
    lista_palabras = mis_palabras(nombre_archivo)
    lista_agregar = []
    for palabra in lista_palabras:
        if (not(pertenece(lista_agregar, palabra))):
            diccionario[palabra] = 1
            lista_agregar.append(palabra)
        else:
            diccionario[palabra] = diccionario[palabra] + 1
    return diccionario


#Ejercicio 22


def visitar_sitio(historiales:dict[str, Pila[str]], usuario:str, sitio:str) -> dict[str, Pila[str]]:
    if(not(pertenece(lista_usuarios, usuario))):
        pila_usuario = Pila()
        lista_usuarios.append(usuario)
        pila_usuario.put(sitio)
        historiales[usuario] = pila_usuario

    else:
        historiales[usuario].put(sitio)

    return historiales

historiales = {}
lista_usuarios: list = []
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
visitar_sitio(historiales, "Usuario1", "youtube.com")
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario2", "instagram.com")
visitar_sitio(historiales, "Usuario2", "tiktok.com")
visitar_sitio(historiales, "Usuario3", "twitch.tv")
visitar_sitio(historiales, "Usuario2", "twitch.tv")
visitar_sitio(historiales, "Usuario1", "playback.tv")
visitar_sitio(historiales, "Usuario3", "wikipedia.com")

def navegar_atras(historiales: dict[str, Pila[str, Pila[str]]], usuario:str) -> dict[str, Pila[str, Pila[str]]]:
    lista_sitios: list = []
    for i in range (2):
        lista_sitios.append(historiales[usuario].get())
    sitio_actual = lista_sitios[0]
    sitio_anterior = lista_sitios[1]
    historiales[usuario].put(sitio_anterior)
    historiales[usuario].put(sitio_actual)
    historiales[usuario].put(sitio_anterior)
    return historiales

def navegar_atras2(historiales: dict[str, Pila[str, Pila[str]]], usuario:str) -> dict[str, Pila[str, Pila[str]]]:
    sitio_actual = historiales[usuario].get()
    sitio_anterior = historiales[usuario].get()

    historiales[usuario].put(sitio_anterior)
    historiales[usuario].put(sitio_actual)
    historiales[usuario].put(sitio_anterior)

    return historiales

#Ejercicio 23
def agregar_producto(inventario: dict[str, dict[float, int]], nombre:str, precio: float, cantidad:int) -> dict[str, dict[float, int]]:
    informacion_adicional = {}
    informacion_adicional = {'Precio': precio, 'Cantidad': cantidad}
    inventario[nombre] = informacion_adicional
    return inventario

def actualizar_stock(inventario: dict[str, dict[float, int]], nombre: str, cantidad: int) -> dict[str, dict[float, int]]:
    inventario[nombre]["Cantidad"] = cantidad
    return inventario

def actualizar_precios(inventario: dict[str, dict[float, int]], nombre: str, precio: float) -> dict[str, dict[float, int]]:
    inventario[nombre]["Precio"] = precio
    return inventario

def calcular_valor_inventario(inventario: dict[str, dict[float, int]]) -> float:
    valor: int = 0
    for nombre, info in inventario.items():
        valor = valor + (info["Precio"] * info["Cantidad"])
    return valor

inventario = {}

