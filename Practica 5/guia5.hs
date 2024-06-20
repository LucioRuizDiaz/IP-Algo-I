{-Ejercicio 1.1-}
longitud :: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

{-Ejercicio 1.2-}
ultimo :: [t] -> t 
ultimo (x:[]) = x
ultimo (x:xs) = ultimo xs

{-Ejercicio 1.3-}
--principio :: [t] -> [t]

{-Ejercicio 1.4-}
reverso :: [t] -> [t]
reverso [] = []
reverso (x:[]) = [x]
reverso (x:xs) = reverso xs ++ [x]


{- Ejercicio 2.1-}
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False 
pertenece t (x:xs)  | t == x = True
                    | otherwise = pertenece t (xs)

{-Ejercicio 2.2-}
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:[]) = True
todosIguales (x:xs) | pertenece x xs = todosIguales xs  
                    | otherwise = False

{-Ejercicio 2.3-}
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x:[]) = True
todosDistintos (x:xs)   | pertenece x xs = False
                        | otherwise = todosDistintos xs

{-Ejercicio 2.4-}
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs

{-Ejercicio 2.5-}
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (x:xs) | e == x = xs    
                |otherwise = x : quitar e xs

{-Ejercicio 2.6-}
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs) | e == x = quitarTodos e xs   
                     |otherwise = x : quitarTodos e xs

{-Ejercicio 2.7-}
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs)    | pertenece x (xs) = eliminarRepetidos(xs)    
                            | otherwise = x: eliminarRepetidos (xs)
 
{-Ejercicio 2.8 FALTA TERMINAR-}
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [x] [y] | x == y = True
                        | otherwise = False
    
mismosElementos (x:xs) (ys) | (longitud(eliminarRepetidos(x:xs)) == longitud(eliminarRepetidos(ys)) ) && pertenece x (eliminarRepetidos(ys)) = mismosElementos (xs) (ys)
                            | otherwise = False

{-Ejercicio 3.1-}
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria (xs)

{-Ejercicio 3.2-}
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria (xs)

{-Ejercicio 3.3-}
maximo :: (Ord t) => [t] -> t 
maximo [x] = x
maximo (x:y:xs)     |x >= y = maximo (x:xs) 
                    |otherwise = maximo (y:xs)  
                
{-Ejercicio 3.4-}
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:s) = [n+x] ++ sumarN n (s)

{-Ejercicio 3.5-}
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [s] = [s+s]
sumarElPrimero (x:s) = sumarN x (x:s)

{-Ejercicio 3.6-}
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [s] = [s+s]
sumarElUltimo (x:s) = reverso( sumarElPrimero (reverso(x:s)))

{-Ejercicio 3.7-}
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:s) | mod x 2 == 0 = x : pares (s)
            | otherwise = pares (s)

{-Ejercicio 3.8-}
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs)   | mod x n == 0 = x : multiplosDeN n (xs)
                        | otherwise = multiplosDeN n (xs)


{-Ejercicio 3.9-}
ordenar :: (Ord t) => [t] -> [t]
ordenar [x] = [x]
ordenar (x:y:xs)    | x == maximo(x:y:xs) = ordenar (y:xs) ++ [x]
                    | otherwise = ordenar (y:x:xs)

{-Ejercicio 4.1-}
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [s] = [s]
sacarBlancosRepetidos (x:y:xs)  | x == y && x == ' ' = sacarBlancosRepetidos(y:xs)
                                | otherwise = x : sacarBlancosRepetidos (y:xs)

{-Ejercicio 4.2-}
contarPalabras :: [Char] -> Integer
contarPalabras [s]  | s == ' ' = 0
                    | otherwise = 1
contarPalabras (x:s)  = contarPalabrasSinRepetidos(sacarBlancosRepetidos(sacarPrimerBlanco(sacarUltimoBlanco(x:s))))

sacarPrimerBlanco :: [Char] -> [Char]
sacarPrimerBlanco (x:xs)    | x == ' ' = (xs)
                            | otherwise = x : (xs)

sacarUltimoBlanco :: [Char] -> [Char]
sacarUltimoBlanco (x:xs) = reverso(sacarPrimerBlanco(reverso(x:xs)))

contarPalabrasSinRepetidos :: [Char] -> Integer
contarPalabrasSinRepetidos [s]  | s == ' ' = 0
                                | otherwise = 1
contarPalabrasSinRepetidos (x:xs)   | x == ' ' = 1 + contarPalabrasSinRepetidos (xs)
                                    | otherwise = contarPalabrasSinRepetidos (xs)

{-Ejercicio 4.3-}
palabras :: [Char] -> [[Char]]
palabras [] = [[]]
palabras [s] = [[s]]
palabras (x:s)  | x /= ' ' = [sacarBlancosRepetidos(sacarPrimerBlanco(sacarUltimoBlanco(x:s)))] 
                | otherwise =  palabras (s)


generarPalabras :: [Char] -> [[Char]]
generarPalabras [] = [[]]
generarPalabras [s] = [[s]] 
generarPalabras (x:y:s) | y /= ' '  = [(x:y:s)]
                        | otherwise = [[x]] ++ generarPalabras(s)
                        

{-Ejercicio 5.1-}
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [s] = [s]
sumaAcumulada (x:y:s) = [x] ++ sumaAcumulada(x+y:s)


{-Ejercicio 5.2-}
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos [x] | esPrimo (x) = [[x]]
                        | otherwise = [divisoresPrimos x 2]
descomponerEnPrimos (x:s)   | esPrimo(x) = [[x]] ++ descomponerEnPrimos(s)  
                            | otherwise = [divisoresPrimos x 2] ++ descomponerEnPrimos(s)

divisoresPrimos :: Integer -> Integer -> [Integer]
divisoresPrimos n y | y == n && esPrimo n = [n]
                    | (mod n y == 0) && y < n = y : divisoresPrimos (div n y) (sigPrimo y)
                    | (mod n y /= 0) && y < n = divisoresPrimos n (sigPrimo y)

{-Ejercicios Guia 4-}
{-Ejercicio 16a-}
sigPrimo :: Integer -> Integer
sigPrimo x | esPrimo (x+1) = x+1 
           | otherwise = sigPrimo (x+1)

menorDivisor :: Integer -> Integer
menorDivisor 1 = 1
menorDivisor n = menorDivisorHasta n 2

menorDivisorHasta :: Integer -> Integer -> Integer
menorDivisorHasta x y   | (mod x y == 0 ) = y
                        | otherwise = menorDivisorHasta x (y +1)

{-Ejercicio 16b-}
esPrimo :: Integer -> Bool
esPrimo 1 = True
esPrimo n   | menorDivisor n == n = True
            | otherwise = False

{-www.pastebin.com/RprbkzX2-}