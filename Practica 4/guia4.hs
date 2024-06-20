{- Ejercicio 1 -}

fibonacci :: Integer -> Integer 
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2) 

{- Ejercicio 2-}

parteEntera :: Float -> Integer
parteEntera x   | 0 <= x && x < 1 = 0
                | -1 < x && x < 0 = -1
                | x >= 1 = 1 + parteEntera (x-1) 
                | otherwise = (-1) + parteEntera(x+1)

{-Ejercicio 3-}

--esDivisible :: Integer -> Integer -> Bool
--esDivisible x y = 

{-Factorial-}

factorial :: Integer -> Integer
factorial 0 = 1 
factorial n = n * factorial(n-1)

{-Ejercicio 4--}

sumaImpares :: Integer -> Integer

sumaImpares 1  = 1
sumaImpares n = (2*n - 1)+ sumaImpares (n-1)


{-Ejercicio 5-}
medioFact :: Integer -> Integer
medioFact 0 = 1 
medioFact 1 = 1
medioFact x = x * medioFact (x-2)


{-Ejercicio 6-}
sumaDigitos ::  Integer -> Integer
{-sumaDigitos x | x < 10 = mod x 10
              | x < 100 = sumaDigitos(x-10) + 1
              | x < 1000 = sumaDigitos(x-100) + 1
-}
sumaDigitos x   | x < 10 = x
                | otherwise =sumaDigitos (div x 10) + sumaDigitos (mod x 10)


{-Ejercicio 7-}
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n   | n < 10 = True
                        | otherwise = (digitoUnidades n == digitoUnidades(sacarUnidades n)) && todosDigitosIguales (sacarUnidades n)


digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10

sacarUnidades :: Integer -> Integer
sacarUnidades n = div n 10


{- Ejercicio 8-}
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i    | i == cantDigitos n = digitoUnidades n
                    | otherwise = iesimoDigito (sacarUnidades n) i



cantDigitos :: Integer -> Integer
cantDigitos n   | n < 10 = 1 
                | otherwise = cantDigitos (sacarUnidades n ) + 1




{- Ejercicio 9 FALTA TERMINAR 
esCapicua ::  Integer -> Bool 
esCapicua n | n < 10 = True
            | otherwise = compararPrimYUlt n

compararPrimYUlt :: Integer -> Bool
compararPrimYUlt x  | x <10 && x>0= False
                    | otherwise = (primerDigito x == digitoUnidades x) && compararPrimYUlt(sacarPrimerDigito(sacarUnidades x)) 

primerDigito :: Integer -> Integer
primerDigito n  | n < 10 = n
                | otherwise = primerDigito (sacarUnidades n)


sacarPrimerDigito :: Integer -> Integer 
sacarPrimerDigito n | n < 10 = n
                    | otherwise = mod n (10^(cantDigitos(n)-1))-}


{-Ejercicio 10a-}
potenciaIDe2 :: Integer -> Integer
potenciaIDe2 0 = 1
potenciaIDe2 n = 2^n + potenciaIDe2 (n-1)


{-Ejercicio 10b-}
potenciaIDeQ :: Integer -> Integer -> Integer
potenciaIDeQ 1 q= q
potenciaIDeQ n q= q^n + potenciaIDeQ (n-1) q

{-Ejercicio 10c-}
potencia2n :: Integer -> Integer -> Integer
potencia2n 0 q = 0 
potencia2n n q = q^(2*n) + potencia2n (n-1) q + q

{-Ejericio 10d-}
potencia2na :: Integer -> Integer -> Integer
potencia2na 0 q = 0 
potencia2na n q = q^(2*n) + potencia2na (2*(n-1)) q + q^n

{-Ejercicio 11a-}
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = (1 / fromIntegral(factorial n) ) + eAprox (n-1)

{-Ejercicio 11b-}
e :: Float 
e = eAprox 10

{-Ejercicio 12 -}
raizDe2Aprox :: Integer -> Float
raizDe2Aprox 1 = 1 
raizDe2Aprox n = sucesionAn n -1


sucesionAn :: Integer -> Float
sucesionAn 1 = 2
sucesionAn an = 2 + 1/(sucesionAn(an -1) )
{-Ejercicio 13-}
dobleSumaDePotencia :: Integer -> Integer -> Integer
dobleSumaDePotencia n m | n == 1 = simpleSuma 1 m 
                        | n > 1 = dobleSumaDePotencia (n-1) m + simpleSuma n m 

simpleSuma :: Integer -> Integer -> Integer
simpleSuma n m  | m == 1 = n 
                | m > 1 = simpleSuma n (m-1) + n^m

{- Ejercicio 14-}
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q 1 1 = q^2
sumaPotencias q 1 m = q^(1+m) + sumaPorPartes q 1 (m-1)
sumaPotencias q n 1 = q^(n+1) + sumaPorPartes q (n-1) 1
sumaPotencias q n m = q^(n+m) + sumaPorPartes q n m 


sumaPorPartes :: Integer -> Integer -> Integer -> Integer
sumaPorPartes q n m | n == 1 = sumaPotencias q 1 m 
                    | m == 1 = sumaPotencias q n 1
                    | n > 1 = sumaPotencias q (n-1) m 
           --         | n > 1 = sumaPotencias q n (m-1)


-- = q^(n+m) + sumaPotencias q n (m-1) + sumaPotencias q (n-1) m 




{-Ejercicio 15
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales    +-}
{- Ejercicio 16 a-}

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

{-
esFibonacci :: Integer -> Bool 
esFibonacci 0 = True
esFibonacci 1 = True 
esFibonacci f = comparacionFibonacci f 1

comparacionFibonacci :: Integer -> Integer -> Bool
comparacionFibonacci f i    | (f == (fibonacci i)) = True
                            | otherwise = comparacionFibonacci f (i + 1)-}
