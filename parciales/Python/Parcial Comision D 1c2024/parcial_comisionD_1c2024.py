from queue import Queue as Cola

#Ejercicio 1
def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    numeros_primos: list[int] = codigos_barra
    numeros_tres_digitos: list[int] = []
    numeros_final: list[int] = []
    
    for numero in codigos_barra:
        numero_3= numero%1000
        numeros_tres_digitos.append(numero_3)
            
    for i in range(len(numeros_tres_digitos)):
        if (es_primo(numeros_tres_digitos[i])):
            numeros_final.append(numeros_primos[i])
                
    return numeros_final

                
def es_primo(numero: int) -> bool:
    res: bool = True
    for i in range(2, numero):
        if(numero%i == 0):
            res = False
    if(numero == 1):
        res = True
    
    return res

#print(filtrar_codigos_primos([1230101, 54685007, 68759006, 65485017, 46879008, 65485103, 64885005, 6489532022]))

#Ejercicio 2
def pertenece(lista:list, x) -> bool:
    res: bool = False
    for i in range (len(lista)):
        if (lista[i][0] == x):
            res = True
    return res


def stock_productos(stock_cambios: list[(str,int)]) -> dict[str, (int, int)]:
    res = {}
    lista_historica = []
    for producto in stock_cambios:
        if (not(pertenece(lista_historica, producto[0]))):
            elemento = producto[0], [producto[1]]
            lista_historica.append(elemento)
        else:
            for i in range(len(lista_historica)):
                if(lista_historica[i][0] == producto[0]):
                    lista_historica[i][1].append(producto[1])

    for producto in lista_historica:
        res[producto[0]] = (minimo(producto), maximo(producto))

    return res

def maximo(tupla:list) -> int:
    maximo: int = 0
    lista_stock = tupla[1]
    for i in range(len(lista_stock)):
        if( maximo >= lista_stock[i]):
            maximo = maximo
        else: 
            maximo = lista_stock[i]
    return maximo

def minimo(tupla:list) -> int:
    lista_stock = tupla[1]
    minimo: int = lista_stock[0]

    for i in range(len(lista_stock)):
        if( minimo < lista_stock[i]):
            minimo = minimo
        else: 
            minimo = lista_stock[i]
    return minimo


#print(stock_productos([("pan", 90), ("carne", 500), ("milanesa", 350), ("pan", 40), ("carne", 550), ("milanesa", 250), ("pan", 42), ("carne", 600), ("milanesa", 352)]))

def un_responsable_por_turno(grilla_horaria:list[list[str]]) -> list[(bool, bool)]:
    responsables_mañana: list[str] = []
    responsables_tarde: list[str] = []
    responsable_mañana: str = ""
    responsable_tarde: str = ""
    lista_booleana: list[(bool, bool)] = []

    for fila in range(len(grilla_horaria) -1):
        for columna in range(len(grilla_horaria)):

            if(columna <= 3):
                responsable_mañana = grilla_horaria[columna][fila]
                responsables_mañana.append(responsable_mañana)
            else:
                responsable_tarde = grilla_horaria[columna][fila]
                responsables_tarde.append(responsable_tarde)
        
        lista_booleana.append(((son_todos_iguales(responsables_mañana)), (son_todos_iguales(responsables_tarde))))
        responsables_mañana.clear()
        responsables_tarde.clear()
    
    return lista_booleana


def son_todos_iguales(responsables: list[str]) -> bool:
    res: bool = True
    longitud = len(responsables)
    for i in range(longitud - 1):
        if(responsables[i] != responsables[i+1]):
            res = False
    return res






grilla_horaria = [["jorge", "lucas", "jochi", "jochi", "lari", "jorge", "mateo"],
                  ["jorge", "lucas", "jochi", "jochi", "lari", "jorge", "mateo"],
                  ["jorge", "lucas", "jochi", "jochi", "lari", "jorge", "caste"],
                  ["jorge", "lucas", "caste", "jochi", "lari", "jorge", "caste"],
                  ["lucas", "nico", "caste", "jochi", "lucio", "mica", "caste"],
                  ["lucas", "nico", "caste", "caste", "lucio", "mica", "caste"],
                  ["nico", "nico", "caste", "caste", "lucio", "mica", "mateo"],
                  ["nico", "nico", "caste", "caste", "lucio", "mica", "mateo"]]

#print(un_responsable_por_turno(grilla_horaria))

def subsecuencia_mas_larga2(tipos_pacientes_atendidos:list[str]) -> int:
    res: int = 0
    perro_gato: list[str] =["perro", "gato"]
    subsecuencias: list[tuple[list[str], int]] = []
    aux_list: list[str] = []
    aux_index: int = 0
    contador: int =  0
    for animal in tipos_pacientes_atendidos:
        if animal in perro_gato:
            aux_list.append(animal)
        else:
            subsecuencias.append((aux_list, aux_index))
            aux_index = contador + 1
            aux_list = []

    
    return subsecuencias


def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str]) -> int:
    subsecuencias: list[list[(str, int)]] = []
    consecutivos: list[(str, int)] = []
    cola = Cola()
    i : int = 0
    for animal in tipos_pacientes_atendidos:
        if animal == "gato" or animal == "perro":
            consecutivos.append((animal, i))

        else:
            subsecuencias.append(consecutivos)
            consecutivos = []
        i+=1
    subsecuencias.append()
    return subsecuencias
            


def es_gato_o_perro(animal:str) -> bool:
    if ((animal == "gato") or (animal == "perro")):
        res = True
    else:
        res = False
    return res

#print(subsecuencia_mas_larga(["tortuga", "perro", "gato", "perro", "elefenate", "jigrafa", "perro", "gato", "loro", "perro", "hamster", "perro", "gato", "gato", "gato"]))

def capital_indexes(palabra:str) -> list[int]:
    lista_palabras: list[str] = list(palabra)
    lista_indices: list[int] = []
    
    print(palabra[2])
    for i in range(len(lista_palabras)):
        if (lista_palabras[i].isupper()):
            lista_indices.append(i)
    
    return lista_indices
    
print(capital_indexes("HeLlO"))

