from queue import LifoQueue as Pila
from queue import Queue as Cola


#Ejercicio 1
def reordenar_cola_priorizando_vips(filaClientes: Cola[(str, str)]) -> Cola[str]:
    #print(filaClientes.queue)
    lista_clientes: list = []
    cola_vip = Cola()
    cola_comun = Cola()
    cola_final = Cola()
    
    while(not(filaClientes.empty())):
        cliente = filaClientes.get()
        lista_clientes.append(cliente)
    #print(filaClientes.queue)

    for cliente in lista_clientes:    
        
        if(cliente[1] == "vip"):
            cola_vip.put(cliente[0])
        else:
            cola_comun.put(cliente[0])
        
        filaClientes.put(cliente)
    #print(filaClientes.queue)

    while(not(cola_vip.empty())):
        vip = cola_vip.get()
        cola_final.put(vip)

    while(not(cola_comun.empty())):
        comun = cola_comun.get()
        cola_final.put(comun)

    return cola_final


def crear_cola(lista_clientes: list[(str, str)]) -> Cola[(str, str)]:
    filaClientes = Cola()
    for cliente in lista_clientes:
        filaClientes.put(cliente)
    return filaClientes

#print(reordenar_cola_priorizando_vips(crear_cola([("lucio", "comun"), ("jochi", "vip"), ("lari","vip"), ("lucio(bajo)","comun"), ("caste","vip")])))

#Ejercicio 2
def torneo_de_gallinas(estrategias:dict[str, str]) -> dict[str, int]:
    jugadores_estrategias: list[(str, str)] = []
    jugadores_puntos: dict[str, int] = {}
    for nombre, estrategia in estrategias.items():
        jugadores_estrategias.append((nombre, estrategia))
        jugadores_puntos[nombre] = 0
    
    for i in range(len(jugadores_estrategias) - 1):
        estrategia_actual = jugadores_estrategias[i][1]
        for j in range(len(jugadores_estrategias) - i - 1):
            estrategia_siguiente = jugadores_estrategias[j+i+1][1]
            if(estrategia_actual == estrategia_siguiente):
                if(estrategia_actual == "me la banco y no me desvio"):
                    jugadores_puntos[jugadores_estrategias[i][0]] = jugadores_puntos[jugadores_estrategias[i][0]] - 5
                    jugadores_puntos[jugadores_estrategias[i+j+1][0]] = jugadores_puntos[jugadores_estrategias[i+j+1][0]] - 5
                elif(estrategia_actual == "me desvio siempre"):
                    jugadores_puntos[jugadores_estrategias[i][0]] = jugadores_puntos[jugadores_estrategias[i][0]] - 10
                    jugadores_puntos[jugadores_estrategias[i+j+1][0]] = jugadores_puntos[jugadores_estrategias[i+j+1][0]] - 10
            elif(estrategia_actual == "me desvio siempre"):
                jugadores_puntos[jugadores_estrategias[i][0]] = jugadores_puntos[jugadores_estrategias[i][0]] - 15
                jugadores_puntos[jugadores_estrategias[i+j+1][0]] = jugadores_puntos[jugadores_estrategias[i+j+1][0]] + 10
            else:
                jugadores_puntos[jugadores_estrategias[i][0]] = jugadores_puntos[jugadores_estrategias[i][0]] + 10
                jugadores_puntos[jugadores_estrategias[i+j+1][0]] = jugadores_puntos[jugadores_estrategias[i+j+1][0]] - 15
    return jugadores_puntos
                


estrategias = {
    'lucio':'me la banco y no me desvio', 
    'jochi':'me la banco y no me desvio', 
    'lari':'me desvio siempre', 
    'lucio(bajo)':'me desvio siempre', 
    'caste':'me la banco y no me desvio'
}

#print(torneo_de_gallinas(estrategias))

#Ejercicio 3
def quien_gano_el_tateti_facilito(tablero:list[list[str]]) -> int:
    res: int
    gano_ana: bool = False
    gano_beto: bool = False
    for filas in range(len(tablero)):
        suma_ana: int = 0
        suma_beto: int = 0
        for columnas in range(len(tablero[filas])):
            if (tablero[columnas][filas] == "X"):
                suma_ana +=1
                suma_beto = 0
                if(suma_ana == 3):
                    gano_ana = True
            if(tablero[columnas][filas] == "O"):
                suma_ana = 0
                suma_beto += 1
                if(suma_beto == 3):
                    gano_beto = True
    if((gano_ana) and (not(gano_beto))):
        res = 1
    elif((not(gano_ana)) and (gano_beto)):
        res = 2
    elif((not(gano_ana)) and (not(gano_beto))):
        res = 0
    elif((gano_ana) and (gano_beto)):
        res = 3
    return res
             
#print(quien_gano_el_tateti_facilito(tablero))

#Ejercicio 4

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    res: int = 0
    sufijos : list[str] = generar_sufijos(texto)
    for sufijo in sufijos:
        if(es_palindromo(sufijo)):
            res += 1
    return res


def es_palindromo(texto:str) -> bool:
    res: bool = False
    texto_original: list[str] = list(texto)
    texto_al_reves: list[str] = list(texto)
    longitud: int = len(texto)

    for i in range(longitud):
        texto_al_reves[longitud - 1 -i] = texto_original[i]

    if(texto_al_reves == texto_original):
        res = True
    return res
        

def generar_sufijos(texto: str) -> list[str]:
    texto_original: list[str] = list(texto)
    sufijos: list[str] = [texto]
    for i in range (len(texto_original) -1):
        sufijo = ""
        for j in range(len(texto_original) - i -1):
            sufijo = sufijo + texto_original[j+1]
        sufijos.append(sufijo)
            
    return sufijos

#print(cuantos_sufijos_son_palindromos("neuquen"))

