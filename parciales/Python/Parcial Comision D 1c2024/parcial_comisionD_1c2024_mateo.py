## EJERCICIO 1

def ultimos_tres_digitos(numero:int)->int:
    return numero - (numero // 1000 * 1000 )

#print(ultimos_tres_digitos(1925005))

def es_primo(numero:int)->bool:
    ind:int = 1
    aux:int = 0
    res:bool

    while ind <= numero:
        if (numero % ind) == 0:
            aux = aux + 1
            ind = ind + 1
        else:
            ind = ind + 1
    
    if aux <= 2:
        res = True
    else:
        res = False

    return res

#print(es_primo())

def filtrar_codigos_primos(codigos_barra:list[int])->list[int]:
    ind: int
    res:list = []
    
    for ind in range(len(codigos_barra)):
        if es_primo(ultimos_tres_digitos(codigos_barra[ind])):
            res.append(codigos_barra[ind])
    
    return res

#print(filtrar_codigos_primos([1209491101,192492,9124912037,129051001,2819419248222]))

## EJERCICIO 2

def minimo_lista(lista:list[int])->int:
    ind_lista: int
    aux:int = lista[0]
    res:int
    for ind_lista in range(len(lista)):
        if aux > lista[ind_lista]:
            aux = lista[ind_lista]
    return aux

def maximo_lista(lista:list[int])->int:
    ind_lista: int
    aux:int = lista[0]
    res:int
    for ind_lista in range(len(lista)):
        if aux <= lista[ind_lista]:
            aux = lista[ind_lista]
    return aux

def primer_elemento(tupla:list):
    return tupla[0]

def segundo_elemento(tupla:list):
    return tupla[1]

def lista_productos(lista:list[str,int])->list[str]:
    ind: int
    res:list = []
    for ind in range(len(lista)):
        if not primer_elemento(lista[ind]) in res:
            res.append(primer_elemento(lista[ind]))
    return res


def stock_productos(stock_cambios:list)->dict:
    ind_cambios: int
    ind_productos:int
    lista_aux:list = []
    aux:int = 0
    productos = lista_productos(stock_cambios)
    tupla_aux:tuple = ()
    diccionario = dict()
    lista_productos_ya_cargados:list = []

    for ind_productos in range(len(productos)):
        if not productos[ind_productos] in lista_productos_ya_cargados:
            for ind_cambios in range(len(stock_cambios)):
                if primer_elemento(stock_cambios[ind_cambios]) == productos[ind_productos]:
                    aux = aux + segundo_elemento(stock_cambios[ind_cambios])
                    lista_aux.append(aux)
            
            tupla_aux = (minimo_lista(lista_aux),maximo_lista(lista_aux))
            lista_aux = []
            lista_productos_ya_cargados.append(productos[ind_productos])
            diccionario[productos[ind_productos]] = tupla_aux
            aux = 0
            tupla_aux = ()

    return diccionario
    
# print(stock_productos([('Shampoo',5),('Shampoo',10),('Correas',50),('Shampoo',-20),('Vacunas',10),('Vacunas',15)]))

## EJERCICIO 4

def tupla_con_maximo_segundo_elemento(lista:list[tuple])->tuple:
    ind: int
    aux: int = 0
    for ind in range(len(lista)-1):
        if segundo_elemento(lista[aux]) <= segundo_elemento(lista[ind+1]):
            aux = ind + 1
    res = lista[aux]
    return res


def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str])->int:
    res:int
    ind:int
    largo_subsecuencia:int = 0
    aux:int = 0
    lista_aux:list = []

   
    for ind in range(len(tipos_pacientes_atendidos)):
            if tipos_pacientes_atendidos[aux] == tipos_pacientes_atendidos[ind]:
                largo_subsecuencia = largo_subsecuencia + 1
            if tipos_pacientes_atendidos[aux] != tipos_pacientes_atendidos[ind]:
                lista_aux.append((aux,largo_subsecuencia))
                aux = aux + largo_subsecuencia
                largo_subsecuencia = 1
            if ind == len(tipos_pacientes_atendidos) - 1:
                lista_aux.append((aux,largo_subsecuencia))
    
    res = primer_elemento(tupla_con_maximo_segundo_elemento(lista_aux))
    
    return res

#print(subsecuencia_mas_larga(['gato','gato','perro','perro','perro','gato','gato','gato','gato','gato','gato','gato','gato','gato','gato','perro','perro','perro','perro','perro','perro']))

## EJERCICIO 3

def dia_de_fila(lista:list[str],dia:int):
    return lista[dia]


def un_responsable_por_turno(grilla_horaria:list[list[str]])->list[bool,bool]:

    ind_dia:int = 0
    ind_lista:int = 0

    primer_elemento_tupla_aux:bool = True
    segundo_elemento_tupla_aux:bool = True

    res:list = []
    
    while ind_dia < 7:

        while ind_lista < 3:
            if dia_de_fila(grilla_horaria[ind_lista],ind_dia) != dia_de_fila(grilla_horaria[ind_lista+1],ind_dia):
                primer_elemento_tupla_aux = False
            ind_lista = ind_lista + 1
        if ind_lista == 3:
            ind_lista = ind_lista + 1
        while ind_lista < 6:
            if dia_de_fila(grilla_horaria[ind_lista],ind_dia) != dia_de_fila(grilla_horaria[ind_lista+1],ind_dia):
                segundo_elemento_tupla_aux = False
            ind_lista = ind_lista + 1

        if ind_lista == 6:
            res.append((primer_elemento_tupla_aux,segundo_elemento_tupla_aux))
            ind_dia = ind_dia + 1
            ind_lista = 0
            primer_elemento_tupla_aux = True
            segundo_elemento_tupla_aux = True

    return res

'''
print(un_responsable_por_turno([['T','O','M','A','S','C','A'],
                                ['T','O','M','A','S','C','A'],
                                ['T','O','M','C','S','C','A'],
                                ['C','O','M','A','S','C','A'],
                                ['M','A','T','E','O','K','T'],
                                ['M','A','T','E','O','K','T'],
                                ['M','A','T','X','O','K','C'],
                                ['M','A','T','E','O','K','T']]
                                ))
                                '''