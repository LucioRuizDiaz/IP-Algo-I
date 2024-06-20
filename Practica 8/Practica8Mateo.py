## GUÍA 8


#print(mi_archivo.readlines())


# Ejercicio 1

def contar_lineas(nombre_archivo:str)->int:
    mi_archivo = open(nombre_archivo,"r+")
    res : int = len(mi_archivo.readlines())
    return res

#print (contar_lineas("texto.txt"))


def mis_palabras(nombre_archivo:str):
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
    return palabras

#print(mis_palabras("texto.txt"))


def existe_palabra(palabra:str, nombre_archivo:str)->bool:
    ind: int
    res = False
    for ind in range(len(mis_palabras(nombre_archivo))):
        if mis_palabras(nombre_archivo)[ind] == palabra : 
            res = True
    return res

#print(existe_palabra('hola',"texto.txt"))

def es_comentario(frase:str)->bool:
    res:bool = False
    ind: int = 0
    aux: chr = ' '
    while aux == ' ':
            if frase[ind] == ' ' :
                ind = ind + 1
            if frase[ind] == '#' :
                aux = '#'
            if frase[ind] != ' ' and frase[ind] != '#':
                aux = frase[ind]
    if aux == '#': res = True
    return res

def clonar_sin_comentarios(nombre_archivo:str):
    arch = open(nombre_archivo, "r")
    nuevo_arch = open("nuevo_archivo.txt","w")
    lista_aux:list[str] = arch.readlines()
    ind: int
    for ind in range(contar_lineas(nombre_archivo)):
        if not es_comentario(lista_aux[ind]):
            nuevo_arch.writelines(lista_aux[ind])
    arch.close()
    nuevo_arch.close()

#print(clonar_sin_comentarios("prueba.txt"))









## PILAS

from queue import LifoQueue as Pila

import random

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int)->Pila[int]:
    p = Pila()
    i:int = 0
    for i in range(cantidad):
        p.put(random.randint(desde,hasta))
    return p

#print(generar_nros_al_azar(3,1,9).queue)


############################

def cant_elementos(p:Pila)->int:
    lista_elementos:list[int] = []
    elemento:int
    res:int
    ind: int
    while p.empty() == False:
        elemento = p.get()
        lista_elementos.append(elemento)
    res = len(lista_elementos)
    for ind in range(res):
        p.put(lista_elementos[res-ind-1])
    print(p.queue)
    return res

#print(cant_elementos(mi_pila()))


def mi_pila()->Pila:
    p = Pila()
    p.put(7)
    p.put(15)
    p.put(10)
    p.put(11)
    return p

############################

def maximo_lista(lista:list[int])->int:
    ind:int
    res:int = lista[0]
    for ind in range(len(lista)-1):
        if res < lista[ind] : res = lista[ind]
    return res


def buscar_el_maximo(p:Pila[int])->int:
    lista_elementos:list[int] = []
    elemento:int
    res:int
    ind:int
    while not p.empty():
        elemento = p.get()
        lista_elementos.append(elemento)
    res = maximo_lista(lista_elementos)
    for ind in range(len(lista_elementos)):
        p.put(lista_elementos[len(lista_elementos)-1-ind])
    print(p.queue)
    return res

############################

def es_operando(c:chr)->bool:
    res = False
    if ord(c) >= 48 and ord(c) <= 57 :
        res = True
    return res


def evaluar_expresion(s:str)->int:
    aux:Pila[int] = Pila()
    string_aux:str = ""
    res:int
    ind:int
    for ind in range(len(s)):
        if es_operando(s[ind]):
            string_aux += s[ind]
        if s[ind] == ' ':
            if aux.empty():
                res = int(string_aux)
                aux.put(res)
                string_aux = ""
            if string_aux == "":
                aux.put(res)
            else:
                aux.put(int(string_aux))
                string_aux = ""
        if s[ind] == '*':
            res = res * aux.get()
            aux.put(res)
        if s[ind] == '/':
            if aux.get() == 0:
                res = res
                aux.put(res)
                print("No se puede dividir por cero mamita, te devuelvo lo que tenías")
            else:
                res = res / aux.get()
                aux.put(res)
        if s[ind] == '+':
            res = res + aux.get()
            aux.put(res)
        if s[ind] == '-':
            res = res - aux.get()
            aux.put(res)
    return res

#print(evaluar_expresion("24 0 / 24 - 7 + 5 *"))




## COLAS

from queue import Queue as Cola

def generar_nros_al_azar_cola(cantidad:int, desde:int, hasta:int)->Cola[int]:
    c = Cola()
    i:int = 0
    lista_aux:list[int] = []
    for i in range(cantidad):
        lista_aux.append(i)
    random.shuffle(lista_aux)
    for ind in range(len(lista_aux)):
        c.put(lista_aux[ind])
    return c

#print(generar_nros_al_azar_cola(3,1,9).queue)

def mi_cola():
    res = Cola()
    res.put(2)
    res.put(6)
    res.put(7)
    res.put(3)
    return res

#print(mi_cola().queue)

def cantidad_elementos(c:Cola)->int:
    lista_aux:list[int] = []
    ind_lista:int
    while not c.empty():
        lista_aux.append(c.get())
    res:int = len(lista_aux)
    for ind_lista in range(len(lista_aux)):
        c.put(lista_aux[ind_lista])
    print(c.queue)
    return res

#print(cantidad_elementos(mi_cola()))

def buscar_el_maximo(c:Cola)->int:
    lista_aux:list[int] = []
    ind_lista:int
    while not c.empty():
        lista_aux.append(c.get())
    res:int = maximo_lista(lista_aux)
    for ind_lista in range(len(lista_aux)):
        c.put(lista_aux[ind_lista])
    print(c.queue)
    return res

#print(buscar_el_maximo(mi_cola()))




def armar_secuencia_de_bingo()->Cola[int]:
     c = generar_nros_al_azar_cola(15,0,15)
     return c

#print(armar_secuencia_de_bingo().queue)

def jugar_carton_de_bingo(carton:list[int],bolillero:Cola[int])->int:
    carton_aux:list[int] = []
    bolillero_aux:list[int] = []
    ind_carton:int
    jugadas:int = 0

    #print(bolillero.queue)

    while len(carton_aux) < 12:
        bolillero_aux.append(bolillero.get())
        jugadas = jugadas + 1
        for ind_carton in range(12):
            if bolillero_aux[len(bolillero_aux)-1] == carton[ind_carton]:
                carton_aux.append(carton[ind_carton])

    i: int
    for i in range(len(bolillero_aux),15) :
        bolillero_aux.append(bolillero.get())
    

    ind_bolillero:int
    for ind_bolillero in range(len(bolillero_aux)):
        bolillero.put(bolillero_aux[ind_bolillero])

    #print(bolillero.queue)
    #print(carton)
    return jugadas

#print(jugar_carton_de_bingo([1,2,3,4,5,6,7,8,9,10,11,12],armar_secuencia_de_bingo()))




## DICCIONARIOS

def agrupar_por_longitud(nombre_archivo:str)->dict:
    arch = open(nombre_archivo,"r")
    diccionario:dict = {}
    lista_palabras:list = mis_palabras(nombre_archivo)
    ind: int
    lista_aux:int = []
    for ind in range(len(lista_palabras)):
            aux:int = len(lista_palabras[ind])
            if not aux in lista_aux:
                diccionario[aux] = 1
                lista_aux.append(aux)
            else:
                diccionario[aux] = diccionario[aux] + 1
    return diccionario

print(agrupar_por_longitud("archivo.txt"))

def elemento_tupla(elemento:int,tupla:tuple):
    return tupla[elemento]

def mayor_tupla(lista:list[tuple]):
    ind: int = 0
    res: str = elemento_tupla(0,lista[0])
    cant_mayor:int = elemento_tupla(1,lista[0])
    for ind in range(len(lista)-1):
        if cant_mayor < elemento_tupla(1,lista[ind]) : 
            cant_mayor = elemento_tupla(1,lista[ind])
            res = elemento_tupla(0,lista[ind])
    return res


def la_palabra_mas_frecuente(nombre_archivo:str):
    arch = open(nombre_archivo,"r")
    diccionario:dict = {}
    lista_palabras:list = mis_palabras(nombre_archivo)
    ind:int
    lista_aux:str = []
    res:str

    for ind in range(len(lista_palabras)):
        palabra:str = lista_palabras[ind]
        if not palabra in lista_aux:
            diccionario[palabra] = 1
            lista_aux.append(palabra)
        else:
            diccionario[palabra] = diccionario[palabra] + 1

    lista_tuplas:list[tuple] = []
    ind_aux:int
    for ind_aux in range(len(lista_aux)):
        lista_tuplas.append((lista_aux[ind_aux],diccionario.pop(lista_aux[ind_aux])))

    
    res = mayor_tupla(lista_tuplas)

    return res

