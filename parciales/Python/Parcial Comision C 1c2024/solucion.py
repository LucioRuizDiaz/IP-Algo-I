from queue import Queue as Cola


def tiempo_mas_rapido (tiempos_salas: list[int])-> int:
  lista_tiempos_exitosos: list[(int, int)] = []

  for i in range(len(tiempos_salas)):
    if((tiempos_salas[i]>= 1) and (tiempos_salas[i] <= 60)):
      lista_tiempos_exitosos.append((tiempos_salas[i], i))

  menor_tiempo: int = lista_tiempos_exitosos[0]
  for i in range(len(lista_tiempos_exitosos)):
    if(menor_tiempo[0] <= lista_tiempos_exitosos[i][0]):
      menor_tiempo = menor_tiempo
    else:
      menor_tiempo = lista_tiempos_exitosos[i]


  return menor_tiempo[1]

tiempo_mas_rapido_final=[60,4,5,10,60,1,42]
(tiempo_mas_rapido(tiempo_mas_rapido_final))


def promedio_de_salidas (registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
  diccionario_salidas = {}
  for nombre, lista in registro.items():
    suma_tiempos: int = 0
    cant_salas: int = 0
    promedio: int = 0
    if(alguno_exitoso(lista)):
        for tiempo in lista:
            if (tiempo >= 1 and tiempo <= 60):
              suma_tiempos += tiempo
              cant_salas += 1
        promedio = suma_tiempos / cant_salas
        diccionario_salidas[nombre] = (cant_salas, promedio)
    else:
      diccionario_salidas[nombre] = (0, 0.0)

  return diccionario_salidas


def alguno_exitoso(tiempos: list[int]) -> bool:
  res: bool = False
  for tiempo in tiempos:
    if((tiempo > 0) and (tiempo < 61)):
      res = True
  return res

registro = {'lucio':[21, 12, 50],
           'jo':[0, 10, 11], 
            'lari':[45, 61, 10], 
             'caste': [0, 0, 61, 12, 12], 
              'lucio(bajo)': [0, 61]}

#print(promedio_de_salidas(registro))


def escape_en_solitario (amigos_por_salas: list[list[int]])-> list[int]:
    lista_filas_solo: list[int] = []
    longitud = len(amigos_por_salas)
    for filas in range(longitud):
      if ((amigos_por_salas[filas][0] == 0) and (amigos_por_salas[filas][1] == 0) and (amigos_por_salas[filas][2] != 0) and (amigos_por_salas[filas][3] == 0)):
        lista_filas_solo.append(filas)
    return lista_filas_solo

amigos_por_salas = [[0,0,1,0],
                                    [1,61,61,44],
                                    [6,1,2,4],
                                    [55,44,60,60],
                                    [0,0,60,0]]
print(escape_en_solitario(amigos_por_salas))


def racha_mas_larga (tiempos: list[int])-> tuple[int, int] :
  lista_rachas : list = []
  racha: int = 0
  inicio_racha: int = 0 
  fin_racha: int = 0
  for i in range(len(tiempos)):
    if((tiempos[i] >= 1) and (tiempos[i] <= 60)):
        if(racha == 0):
            racha+=1
            inicio_racha = i
        else: 
          racha += 1
    elif(racha>0):
        fin_racha = i -1
        lista_rachas.append((racha,(inicio_racha, fin_racha)))
        racha = 0

  if(racha > 0):
      if(inicio_racha > fin_racha):
         fin_racha = len(tiempos) - 1
      lista_rachas.append((racha,(inicio_racha, fin_racha)))

  racha_maxima = lista_rachas[0]
  for i in range(len(lista_rachas)):
     if(racha_maxima[0] >= lista_rachas[i][0]):
        racha_maxima = racha_maxima
     else:
        racha_maxima = lista_rachas[i]

  return racha_maxima[1]

tiempos = [1, 1, 2, 3, 0, 21, 0, 14, 13, 12, 61]
#print(racha_mas_larga(tiempos))
