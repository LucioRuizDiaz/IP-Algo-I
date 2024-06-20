-- Ejercicio 1a
f :: Integer -> Integer

f 1 = 8
f 4 = 131 
f 16 = 16

-- Ejercicio 1b
g :: Integer -> Integer

g 8 = 16
g 131 = 1
g 16 = 4

-- f o g
h ::  Integer -> Integer
h x = f (g x)

-- g o f
k :: Integer -> Integer
k x = g (f x)


--Ejercicio 2a
absoluto :: Float -> Float
absoluto num| num < 0 = -num
            | otherwise = num



-- Ejercicio 2c 
maximo3 :: Int -> Int -> Int -> Int
--maximo3 x y z
--            |    x > y > z = x
--            |    y > z = y
--            |    otherwise = z

maximo3 x y z  | x > y && x > z = x
               | y > z = y
               | otherwise = z

-- Ejercicio 2g (I)

sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | x /= y && x /= z && y /= z = x + y +z 
                    | x == y && x /= z = x + z
                    | x == z && x /= y = y + z
                    | y == z && x /= y = x + y
                    | otherwise = x
  
-- Ejercicio 2g (II)
sumaDistintosExc :: Int -> Int -> Int -> Int
sumaDistintosExc x y z  | x /= y && x /= z && y /= z = x + y +z 
                        | x == y && x /= z = z
                        | x == z && x /= y = y 
                        | y == z && x /= y = x
                        | otherwise = 0


-- Ejercicio 2i
digitoUnidades :: Float -> Float
digitoUnidades x  = rem (absoluto x) 10

-- Ejercicio 2j 
digitoDecenas :: Float -> Float
digitoDecenas x  =  div ( rem (absoluto x) 100 - rem (mod (absoluto x) 100) 10 ) 10


--Ejercicio 4b

todoMenor :: (Float, Float) -> (Float, Float) -> Bool

todoMenor a b = ((fst a) < (fst b) && (snd a < snd b)) == True



--todoMenor3 :: (Int, Int, Int) -> (Int, Int, Int) -> Bool




--Ejercicio 4f

posPrimerPar :: (Int, Int, Int) -> Int

posPrimerPar (x, y , z) | mod x 2 == 0 = 1
                        | mod y 2 == 0 = 2
                        | mod z 2 == 0 = 3
                        | otherwise = 4


--Ejercicio 6   
bisiesto :: Int -> Bool

bisiesto año | mod año 4 /= 0 || (mod año 100 == 0 && mod año 400 /= 0) = False
             | otherwise = True

--Ejercicio 7
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float

distanciaManhattan (a0, b0, c0) (a1, b1, c1) =  absoluto(a0 - a1) + absoluto(b0 - b1) + absoluto(c0 - c1)                                         


--Ejercicio 8

comparar :: Float -> Float -> Float

comparar x y    | digitoUnidades x + digitoDecenas x < digitoUnidades y + digitoDecenas y = 1
                | digitoUnidades x + digitoDecenas x > digitoUnidades y + digitoDecenas y = -1
                | (digitoUnidades x + digitoDecenas x) == (digitoUnidades y + digitoDecenas y) = 0


--Ejercicio 9
--A partir de las siguientes implementaciones en
--Haskell, describir en lenguaje natural qu´e hacen y
--especificarlas.
--  d) f4 :: Float -> Float -> Float
--     f4 x y = (x+y)/2

--  e) f5 :: (Float, Float) -> Float
--     f5 (x, y) = (x+y)/2


-- la implementación d) toma dos numeros en R, los suma y saca un promedio mientras que la implementación e) toma una tupla en R y saca un promedio de
-- los dos numeros que la componen

-- f4 (x, y : R) -> R
--      