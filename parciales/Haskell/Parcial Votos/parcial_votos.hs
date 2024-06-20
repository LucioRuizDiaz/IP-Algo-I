{-

﻿Introducción a la Programación
Primer Parcial - Turno Mañana
* El parcial se aprueba con 6 puntos
* Podrás utilizar las siguientes funciones del prelude
   * Listas: head, tail, last, init, length, elem, ++
   * Tuplas: fst, snd
   * Operaciones lógicas: &&, ||, not
   * Constructores de listas: (x:xs), []
   * Constructores de tuplas: (x,y)
* Si querés utilizar Hunit para testear tu código acá tenés un script de ejemplo.
Viva la democracia:
La elección periódica de los gobernantes es la base de los Estados Modernos. Este sistema, denominado "democracia" (término proveniente de la antigua Grecia), tiene diferentes variaciones, que incluyen diferentes formas de elección del/a máximo/a mandatario/a. Por ejemplo, en algunos países se eligen representantes en un colegio electoral (EEUU). En otros se vota a los/as miembros del parlamento (España). En nuestro país elegimos de forma directa la fórmula presidencial (Presidente/a y Vicepresidente/a) cada 4 años.
A continuación presentamos una serie de ejercicios que tienen como objetivo implementar funciones para sistema de escrutinio de una elección presidencial. Leer las descripciones y especificaciones e implementar las funciones requeridas en Haskell, utilizado sóĺamente las herramientas vistas en clase.
Las fórmulas presidenciales serán representadas por tuplas (String x String), donde la primera componente será el nombre del candidato a presidente, y la segunda componente será el nombre del candidato a vicepresidente.
En los problemas en los cuales se reciban como parámetro secuencias de fórmulas y votos, cada posición de la lista votos representará la cantidad de votos obtenidos por la fórmula del parámetro formulas en esa misma posición. Por ejemplo, si la lista de fórmulas es [("Juan Pérez","Susana García"), ("María Montero","Pablo Moreno")] y la lista de votos fuera [34, 56], eso indicaría que la fórmula encabezada por María Montero obtuvo 56 votos, y la lista encabezada por Juan Pérez obtuvo 34 votos.
________________


1) Porcentaje de Votos Afirmativos [1 punto]
problema porcentajeDeVotosAfirmativos (formulas: seq⟨String x String⟩,votos:seq< Z >, cantTotalVotos: Z) : R {
 requiere: {¬formulasInvalidas(formulas)}
 requiere: {|formulas| = |votos|}
 requiere: {Todos los elementos de votos son mayores o iguales a 0}
 requiere: {La suma de todos los elementos de votos es menor o igual a cantTotalVotos}
 asegura: {res es el porcentaje de votos no blancos (es decir, asociados a alguna de las fórmulas) sobre el total de votos emitidos}
}
Para resolver este ejercicio pueden utilizar la siguiente función que devuelve como Float la división entre dos números de tipo Int:


division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)
________________


2) Formulas Inválidas [3 puntos]
problema formulasInvalidas (formulas: seq⟨String x String⟩) : Bool {
 requiere: {True}
 asegura: {(res = true) <=> formulas contiene un candidato se propone para presidente y vicepresidente en la misma fórmula; o algún candidato se postula para presidente o vice en más de una fórmula }
________________


3) Porcentaje de Votos [3 puntos]
problema porcentajeDeVotos (vice: String, formulas: seq⟨String x String⟩,votos:seq< Z >) : R {
 requiere: {La segunda componente de algún elemento de formulas es vice}
 requiere: {¬formulasInvalidas(formulas)}
 requiere: {|formulas| = |votos|}
 requiere: {Todos los elementos de votos son mayores o iguales a 0}
 requiere: {Hay al menos un elemento de votos mayores estricto a 0}
 asegura: {res es el porcentaje de votos que obtuvo vice sobre el total de votos afirmativos}
}
Para resolver este ejercicio pueden utilizar la función division presentada en el Ejercicio 1.
________________


4) Menos Votado [3 puntos]
problema menosVotado (formulas: seq⟨String x String⟩, votos:seq< Z >) : String {
 requiere: {¬formulasInvalidas(formulas)}
 requiere: {|formulas| = |votos|}
 requiere: {Todos los elementos de votos son mayores o iguales a 0}
 requiere: {Hay al menos un elemento de votos mayores estricto a 0}
 requiere: {|formulas| > 0}
 asegura: {res es el candidato a presidente de formulas menos votado de acuerdo a los votos contabilizados en votos}
}
A continuación te dejamos una estructura básica para resolver los ejercicios. Este código no pretende resolver ningun caso de los ejercicios planteados, es sólo una plantilla.


module Solucion where
-}

-- Ejercicio 1
porcentajeDeVotosAfirmativos :: [(String, String)] -> [Int] -> Int -> Float
porcentajeDeVotosAfirmativos [] [] _ = 0
porcentajeDeVotosAfirmativos (x:formulas) (y:votos) cantTotalVotos | not(formulasInvalidas(x:formulas)) = (division (sumaDeVotos(y:votos)) cantTotalVotos) * 100


division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)


-- Ejercicio 2
formulasInvalidas :: [(String, String)] -> Bool
formulasInvalidas [] = True
formulasInvalidas [formulas]    | fst(formulas) == snd(formulas) = True
                                | otherwise = False
formulasInvalidas (f:formulas)  = pertenece f (formulas) || formulasInvalidas (formulas)


pertenece :: (String, String) -> [(String, String)] -> Bool
pertenece _ [] = False
pertenece persona (f:formulas)  | fst(persona) == snd(persona) = True
                                | fst(persona) == fst(f) || fst(persona) == snd(f) = True
                                | snd(persona) == fst(f) || snd (persona) == snd(f) = True
                                | otherwise = pertenece persona (formulas)

-- Ejercicio 3
porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos _ [] [] = 0.0
porcentajeDeVotos vice [formulas] (votos) | not(formulasInvalidas[formwulas])  && vice == snd(formulas) =  100
porcentajeDeVotos vice (f:formulas) (v:votos) | not(formulasInvalidas(f:formulas)) && esVice vice (f:formulas) = (division (elementoEn (v:votos) (posicionVice  vice (f:formulas))) (sumaDeVotos (v:votos)))*100


esVice :: String -> [(String, String)] -> Bool
esVice _ [] = False
esVice vice (f:formulas)    | vice == snd (f) = True
                            | otherwise = esVice vice (formulas)

posicionVice :: String -> [(String, String)] -> Int
posicionVice _ [] = 0
posicionVice vice (f:formulas)  | esVice vice [f] = 0
                                | otherwise = 1 + posicionVice vice (formulas)

elementoEn :: [Int] -> Int -> Int
elementoEn (x:xs) n | n == 0 = x
                    | otherwise = elementoEn xs (n-1)

sumaDeVotos :: [Int] -> Int
sumaDeVotos [] = 0
sumaDeVotos (x:votos) = x + sumaDeVotos(votos) 


--Parcial Votos
-- Ejercicio 4

menosVotado :: [(String, String)] -> [Int] -> String
menosVotado [formulas] [votos] = fst(formulas)
menosVotado (f:formulas) (v:votos)  | not(formulasInvalidas(f:formulas)) = ultimoVotado (f:formulas) (v:votos)


ultimoVotado :: [(String, String)] -> [Int] -> String
ultimoVotado [formulas] [votos] = fst(formulas)
ultimoVotado (f:formulas) (v:votos) | menorVotos (v:votos) == v = fst (f)
                                    | otherwise = ultimoVotado (formulas) (votos)
menorVotos :: [Int] -> Int
menorVotos [] = 0
menorVotos [votos] = votos
menorVotos (v:y:votos)  | v <= y = menorVotos (v:votos)
                        | otherwise =  menorVotos (y:votos) 
