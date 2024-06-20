import random
from queue import Queue as Cola

print("---------------------")

#EJERCICIO 1
def orden_de_atencion (urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:

  cola_final = Cola()

  lista_urgentes:list[int] = []
  lista_postergables:list[int] = []

  #Paso las colas como listas para comodidad de trabajo
  while(not(urgentes.empty())):
      lista_urgentes.append(urgentes.get())

  while(not(postergables.empty())):
      lista_postergables.append(postergables.get())

  print("Lista de urgentes: " + str(lista_urgentes))

  print("Lista de postergables: " + str(lista_postergables))

  if(len(lista_urgentes) > 0 and len(lista_postergables) > 0):
    for i in range(len(lista_urgentes)):
            cola_final.put(lista_postergables[i])
            cola_final.put(lista_urgentes[i])

  #En el caso de que haya vacios se mete la otra lista a cola_final
  elif(len(lista_urgentes) <= 0):
    for i in range(len(lista_postergables)):
            cola_final.put(lista_postergables[i])

  elif(len(lista_postergables) <= 0):
    for i in range(len(lista_urgentes)):
            cola_final.put(lista_urgentes[i])

  print("Cola final es de: ")
  print(cola_final.queue)

  return cola_final


def cola_from_list(lst):
        cola = Cola()
        for item in lst:
            cola.put(item)
        return cola

def cola_to_list(cola):
        lst = []
        while not cola.empty():
            lst.append(cola.get())
        return lst


urgentes = cola_from_list([1, -3])
postergables = cola_from_list([2, -4])

print(orden_de_atencion(urgentes, postergables))



def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:

  camas_piso:int = 0
  camas_ocupadas:int = 0
  camas_porcentaje:float = 0
  lista_camas:list[float] = []

  for i in range(len(camas_por_piso)):
        camas_porcentaje = 0
        camas_ocupadas = 0
        camas_piso = len(camas_por_piso[i])

        for j in range(len(camas_por_piso[i])):
            if(camas_por_piso[i][j] == False):
                camas_ocupadas += 1

        print("En el piso " + str(i) + " hay " + str(camas_ocupadas) + " camas ocupadas")

        #Calculo porcentaje cama ocupadas en dicho piso
        camas_porcentaje = camas_ocupadas * 100 / camas_piso

        lista_camas.append(camas_porcentaje)

  print(lista_camas)
  return lista_camas

camas_por_piso = [
            [False, True, False],
            [True, True, False],
            [False, False, False]
        ]
(nivel_de_ocupacion(camas_por_piso))