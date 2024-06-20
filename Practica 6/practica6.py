import math

#Ejercicio 1.1
def imprimir_hola_mundo() :
    print("Hola Mundo")


#Ejercicio 1.2
def imprimir_un_verso() :
    print("Sol de Bahia - Amigo de lo Ajeno\n"
          "que cuando llegues y no te de la bienvenida\n"
          "el volver a vernos queda en vos\n"
          "si la suerte quiere y yo te encuentro en otra vida\n"
          "creo que va a ser para peor"
)
    

#Ejercicio 1.3
def raizDeDos() -> float:
    return round(math.sqrt(2), 4) 

#Ejercicio 1.4
def factorial_de_dos() -> int:
    return math.factorial(2)


#Ejercicio 1.5
def perimetro() -> float :
    return  2 * math.pi


#Ejercicio 2.1
def imprimir_saludo(nombre:str):
    print("Hola", nombre )


#Ejercicio 2.2
def raiz_cuadrada_de(n: int) -> float:
    return math.sqrt(abs(n))


#Ejercicio 2.3
def fahrenheit_a_celsius(temp: float) -> float:
    return ((temp - 32)*5) /9


#Ejercicio 2.4
def imprimir_dos_veces(estribo: str):
    print(estribo * 2)


#Ejercicio 2.5
def es_multiplo_de(n:int, m:int) -> bool :
    return n%m == 0


#Ejercicio 2.6
def es_par (n:int) -> bool:
    return es_multiplo_de(n, 2)


#Ejercicio 2.7
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    cant_porciones: int = comensales * min_cant_de_porciones
    return math.ceil(cant_porciones / 8)


#Ejercicio 3.1
def alguno_es_0(num1: int, num2: int) -> bool:
    return (num1 == 0 or num2 == 0)


#Ejercicio 3.2
def ambos_son_0(num1: int, num2: int) -> bool:
    return (num1 == 0 and num2 == 0)


#Ejercicio 3.3
def es_nombre_largo(nombre:str) -> bool:
    res: bool = len(nombre) >= 3 and len(nombre) <= 8
    return res


#Ejercicio 3.4
def es_bisiesto(año: int) -> bool:
    res : bool = (es_multiplo_de(año, 400) or (es_multiplo_de(año, 4) and not(es_multiplo_de(año, 100))))
    return res


#Ejercicio 4 
def peso_pino(centimetros: int) -> int:
    peso: int
    if (centimetros < 300):
        peso = centimetros * 3
    if (centimetros >= 300):
        peso = 900 + ((centimetros-300) * 2)
    return peso

def es_peso_util(peso: int) -> bool:
    res: bool
    if((peso >= 400) and (peso <= 1000)):
        res = True
    else: res = False
    return res

def sirve_pino(altura: int) -> bool:
    return es_peso_util(peso_pino(altura))


#Ejercicio 5.1 
def devolver_el_doble_si_es_par (n:int) -> int:
    res : int
    if(n%2==0): res = 2*n
    else: res = n
    return res


#Ejercicio 5.2
def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    res : int
    if(es_par(numero)) : res = numero
    else: res = numero + 1 
    return res


#Ejercicio 5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    res: int
    if(es_multiplo_de(numero, 3)) : res = numero * 2
    elif(es_multiplo_de(numero, 9)) : res = numero * 3
    else: res = numero
    return res


#Ejercicio 5.4
def lindo_nombre(nombre: str):
    if(len(nombre) >= 5): print("Tu nombre tiene muchas letras!")
    else : print("Tu nombre tiene menos de 5 caracteres")


#Ejercicio 5.5
def elRango(numero: int):
    if(numero < 5): print("Menor a 5")
    if(numero >= 10 and numero <= 20): print("Entre 10 y 20")
    if(numero > 20): print("Mayor a 20")


#Ejercicio 5.6
def hay_que_laburar(genero: str, edad: int):
    if (edad < 18): print("Andá de vacaciones.")
    elif(genero == "F" and edad < 60): print("Te toca trabajar.")
    elif(genero == "F" and edad >= 60): print("Andá de vacaciones.")
    elif(genero == "M" and edad < 65): print("Te toca trabajar.") 
    elif(genero == "M" and edad >= 65): print("Andá de vacaciones")


#Ejercicio 6.1
def numeros_hasta_10():
    i:int = 1
    while (i<=10):
        print(i)
        i+=1

#Ejercicio 6.2
def numeros_pares() :
    n:int = 10
    while (n<=40):
        if(n%2==0): 
            print(n)
        n=n+1


#Ejercicio 6.3
def eco_10_veces():
    n:int = 0
    while (n<10):
        print("eco")
        n+=1


#Ejercicio 6.4
def cuenta_regresiva(num:int):
    while num >= 1:
        print(num)
        num = num-1
    print("Despegue")


#Ejercicio 6.5
def viaje_en_el_tiempo(año_partida: int, año_llegada: int):
    año_partida= año_partida - 1
    while (año_partida>= año_llegada):
        print("Viajó un año al pasado, estamos en el año:", año_partida)
        año_partida-=1


#Ejercicio 6.6
def viaje_aristoteles(año_partida: int):
    año_partida= año_partida - 20
    while(año_partida >= (-384)):
        print("Viajo 20 años en el pasado, estamos en el año:", año_partida)
        año_partida-=20
    print("Conocimos a Aristoteles!")

viaje_aristoteles(1987)
#Ejercicio 7.2
def numeros_pares7():
    for n in range (10, 41, 1):
         if(n%2==0): 
            print(n)

#Ejercicio 7.4
def cuenta_regresiva7():
    for num in range (100, 0, -1):
        print(num)
    print("Despegue!!")
        



