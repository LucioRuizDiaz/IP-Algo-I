-- Ejercicio 5.2

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [x] | esPrimo x == True = [[x]]
                        | otherwise = [(factorizacion x 2)]
descomponerEnPrimos (x:xs) = [(factorizacion x 2)] ++ descomponerEnPrimos(xs)



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


factorizacion :: Integer -> Integer -> [Integer]
factorizacion x y | x == y && esPrimo x = [x]
                  | y >= 2 && mod x y == 0 = y:(factorizacion (div x y) y)
                  | y >= 2 && mod x y /= 0 = factorizacion x (sigPrimo y)


sigPrimo :: Integer -> Integer
sigPrimo x | esPrimo (x+1) == True = x+1 
           | otherwise = sigPrimo (x+1)