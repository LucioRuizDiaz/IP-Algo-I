import array
import random
import numpy as np


#Ejercicio 1.1
def pertenece(s:list[int], e:int) -> bool:
    res: bool = False
    i: int = 0
    long : int = len(s)
    while (i < long):
        if (e == s[i]):
            res = True
        i+=1
    return res


#Ejercicio 1.2
def divide_a_todos(s:list[int], e) -> bool:
    res : bool = True
    for i in range(len(s)):
        if(not(s[i]%e == 0)): res = False
    return res


#Ejercicio 1.3
def suma_total(s:list[int]) -> int:
    i: int = 0
    suma: int = 0
    long : int = len(s)
    while (i<long):
        suma = suma + s[i]
        i+=1
    return suma

def suma_total2(s:list[int]) -> int:
    suma: int = 0
    long: int = len(s)
    for i in range (long):
        suma= suma + s[i]
    return suma


#el FOR crea una lista de valores que recorre de principio a fin, entonces si ya tenemos en el input una lista podemos resumirlo de la siguiente manera y en i se guarda el valor de cada posicion de la lista a medida que la recorre
def suma_total3(s:list[int]) -> int:
    suma: int = 0
    for i in s:
        suma = suma + i
    return suma


#Ejercicio 1.4
def ordenados(s:list[int]) -> bool:
    long: int = len(s)
    i: int = 0
    res: bool = True
    while (i<long-1):
        if (s[i] >= s[i+1]): res = False
        i+=1
    return res


#Ejercicio 1.5
def longitud_listas(s:list[str]) -> bool:
    res: bool = False
    for i in range(len(s)):
        if (len(s[i]) > 7):
            res = True
    return res


#Ejercicio 1.6
def palindromo(text: list[chr]) -> bool:
    res : bool = False
    longitud: int = len(text)
    texto_nuevo: list[text] = list(text)
    for i in range(longitud):
        posicion: int = longitud - 1 - i 
        texto_nuevo[posicion] = text[i]
    if(texto_nuevo == list(text)):
        res = True
    return res

#Ejercicio 1.7
def al_menos_1_mayus(clave: str) -> bool:
    res: bool = False
    long: int = len(clave)
    for i in range (long):
        if((clave[i] >= 'A' and clave[i] <= 'Z') or clave[i] == 'Ñ'):  res = True
    return res

def al_menos_1_minus(clave: str) -> bool:
    res: bool = False
    long: int = len(clave)
    for i in range (long):
        if((clave[i] >= 'a' and clave[i] <= 'z') or clave[i] == 'ñ') :  res = True
    return res

def al_menos_1_num(clave: str) -> bool:
    res: bool = False
    long: int = len(clave)
    for i in range(long):
        if(clave[i] >= '0' and clave[i] <= '9'): res = True
    return res

def fuerza_contraseña(clave: str) -> str:
    res : str
    if(al_menos_1_num(clave) and al_menos_1_mayus(clave) and al_menos_1_minus(clave) and len(clave) > 8):
        res = "VERDE"
    elif(len(clave) < 5):
        res = "ROJA"
    else : res = "AMARILLA"
    return res


#Ejercicio 1.8
def historial_movimientos (movimientos: list[tuple]) -> int:
    saldo: int = 0
    for i in range(len(movimientos)):
        if(que_movimiento_es(movimientos[i]) == "R"):
            saldo = saldo - (valor_transaccion(movimientos[i]))
        elif(que_movimiento_es(movimientos[i]) == "I"):
            saldo = saldo + (valor_transaccion(movimientos[i]))
    return saldo

def que_movimiento_es(mov: tuple) -> str:
    res: str
    if (mov[0] == "R"): res = "R"
    elif(mov[0] == "I") : res = "I"
    return res 

def valor_transaccion(mov: tuple) -> int:
    res: int = mov[1]
    return res


#Ejercicio 1.9 preguntar!!!
def vocales_distintas(palabra: str) -> bool:
    res: bool = False
    vocales = list(juntar_vocales(palabra))
    for vocal in vocales:
        if (vocales.count(vocal) > 1):
            vocales.remove(vocal)
    if(len(vocales) >= 3):
        res = True
    return res

def es_vocal(letra: str) -> bool:
     res : bool = False
     if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u') : res = True
     return res

def juntar_vocales(palabra: list[chr]) -> list[chr]:
    lista_vocales: list[chr] = []
    for letra in palabra:
        if es_vocal(letra): 
            lista_vocales.append(letra)
    return lista_vocales


#Segunda Parte
#Ejercicio 2.1
def modificar_lista(lista: list):
    for i in range(len(lista)):
        if (i%2== 0): lista[i] = 0
    print(lista)


#Ejercicio 2.2
def modificar_lista_in(lista: list[int]) -> list:
    nueva_lista: list[int] = []
    for i in range(len(lista)):
        if(i%2 == 0): nueva_lista.append(0)
        else : nueva_lista.append(lista[i])
    return nueva_lista


#Ejercicio 2.3 preguntar!!!!
def borar_vocales(palabra: list[str]) -> list[str]:
    lista_palabra: list = list(palabra)
    for letra in palabra:
        if es_vocal(letra):
            lista_palabra.remove(letra)
    return lista_palabra        


#Ejercicio 2.4
def reemplaza_vocales(s: list[chr]) -> list[chr]:
    lista_palabra: list = list(s)
    for i in range(len(s)):
        if (es_vocal(s[i])):
            lista_palabra[i] = "-"            
    return lista_palabra  


#Ejercicio 2.5
def da_vuelta_str(s: list[chr]) -> list[chr]:
    s_al_reves: str = list(s)
    for i in range(len(s)):
        s_al_reves[(len(s)) - 1 - i] = s[i]
    al_reves_str = ""
    for letra in s_al_reves:
        al_reves_str = al_reves_str + letra
    return al_reves_str


#Ejercicio 2.6
def eliminar_repetidos(palabra: list[chr]) -> list[chr]:
    i: int = len(palabra) - 1
    

#Ejercicio 3
def promedio(notas:list[int]) -> int:
    res: int
    suma: int = 0
    for nota in notas:
        suma = suma + nota
    res = (suma / len(notas))
    return res

def aprobado(notas: list[int]) -> int:
    res: int
    for nota in notas:
        if (nota < 4):
            res = 3
        elif(promedio(notas) >= 4 and promedio(notas) < 7):
            res = 2
        elif(promedio(notas) >= 7):
            res = 1
    print("el promedio es", promedio(notas))
    return res


#Ejercicio 4.1
def lista_nombres():
    lista: list[str] = []
    nombre = input("Que nombre queres agregar? :")
    while (nombre != "listo"):
        lista.append(nombre)
        nombre = input("Que nombre queres agregar? :")
    return lista


#Ejercicio 4.2
def historial_sube():
    saldo: int = 0
    lista_movimientos: list[(tuple)] = []
    movimiento = input("Que movimiento desea hacer?:")
    while (movimiento != "X"):

        if(movimiento == "C"):
            saldo_add = int(input("Cuanto desea cargar?:"))
            lista_movimientos.append((movimiento, saldo_add))
            saldo = saldo + saldo_add

        if(movimiento == "D"):
            saldo_descontar = int(input("Cuanto desea descontar?:"))
            lista_movimientos.append((movimiento, saldo_descontar))
            saldo = saldo - saldo_descontar

        movimiento = input("Que movimiento desea hacer?:")

    print("El saldo total de tu SUBE es:", saldo)
    return lista_movimientos


#Ejercicio 4.3
def siete_y_medio():
    cartas: list = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    carta_actual: float = random.choice(cartas)
    suma: float = carta_actual
    cartas_sacadas: list = []

    cartas_sacadas.append(carta_actual)
    print("Tu carta es:", carta_actual)
    
    while(suma <= 7.5):
        seguir_jugando = input("Queres sacar otra carta?: ")
        if (seguir_jugando == "si"):
            carta_actual = random.choice(cartas)
            if(carta_actual >= 10 and carta_actual <= 12):
                suma = suma + 0.5
            else:
                suma = suma + carta_actual
            print("Tu carta es:", carta_actual)
            cartas_sacadas.append(carta_actual)

        if(seguir_jugando == "no"):
            break
    
    if(suma > 7.5):
        print("PERDISTE, tus cartas dieron:", suma)
    else:
        print("GANASTE, tus cartas dieron:", suma)
    
    return cartas_sacadas

    
#Ejercicio 5.1
def pertenece_a_cada_uno_version_1(s:list[list[int]], e: int) -> list[bool]:
    res = 0
    return res


#Ejercicio 5.2
def pertenece_a_cada_uno_version_2(lista:list[list[int]], e: int) -> list[bool]:
    for i in range(len(lista)):
        if(pertenece (lista[i], e)): lista[i] = True
        else: lista[i] = False
    return lista


#Ejercicio 5.3
def es_matriz(s:list[list[int]]) -> bool:
    res: bool
    if(len(s) < 1):
        res = False
    elif(len(s[0]) < 1):
        res = False
    else:
        for i in range(len(s)):
            if(len(s[0]) != len(s[i])):
                res = False
            else:
                res = True
    return res


#Ejericio 5.5
def matriz_a_la_p(d: int, p:int):
    matriz = np.random.random((d, d))
    print("La matriz original es:", matriz)
    i: int = 0
    while(i < p):
        matriz = matriz * matriz
        i += 1
    return matriz

print(matriz_a_la_p(2, 2))

