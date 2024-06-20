-- Ejercicio 1

votosEnBlanco :: [(String, String)] -> [Int] -> Int -> Int
votosEnBlanco [(a,b)] [c] t | a /= b && c >= 0 && c <= t = t - c 
votosEnBlanco (x:xs) (ys) t | formulasValidas(x:xs) == True && cantElementosVotos(ys) == cantElementosFormulas(x:xs) && elementosVotosMayoresCero(ys) == True && sumaCantVotos(ys) <= t = t - sumaCantVotos(ys)

-------
elementosVotosMayoresCero :: [Int] -> Bool
elementosVotosMayoresCero [x] | x >= 0 = True
                              | x < 0 = False
elementosVotosMayoresCero (x:xs) | x >= 0 = elementosVotosMayoresCero(xs)
                                 | x < 0 = False

sumaCantVotos :: [Int] -> Int
sumaCantVotos [] = 0
sumaCantVotos [x] = x
sumaCantVotos (x:xs) = x + sumaCantVotos(xs)

cantElementosFormulas :: [(String, String)] -> Int
cantElementosFormulas [] = 0
cantElementosFormulas (x:xs) = 1 + cantElementosFormulas(xs)

cantElementosVotos :: [Int] -> Int
cantElementosVotos [] = 0
cantElementosVotos (x:xs) = 1 + cantElementosVotos(xs)

-- Ejercicio 2

formulasValidas :: [(String, String)] -> Bool
formulasValidas [(a,b)] | a /= b = True
                        | otherwise = False
formulasValidas (x:y:xs) | fst(x) /= fst(y) && fst(x) /= snd(x) && snd(x) /= snd(y) && fst(y) /= snd(y) && snd(x) /= fst(y) = formulasValidas(x:xs) && formulasValidas(y:xs)
                        | otherwise = False

-- Ejercicio 3

porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos p [(a,b)] [v] | p == a && a /= b && v > 0  =  (division v v) * 100
porcentajeDeVotos a (x:xs) (y:ys) | formulasValidas(x:xs) == True && cantElementosFormulas(x:xs) == cantElementosVotos(y:ys) && elementosVotosMayoresCero(y:ys) == True && unoMayorCero(y:ys) = division (votosCandPresidente a (x:xs) (y:ys)) (sumaCantVotos(y:ys)) * 100

unoMayorCero :: [Int] -> Bool
unoMayorCero [x] | x > 0 = True
                | otherwise = False
unoMayorCero (x:xs) | x > 0 = True
                    | x <= 0 = unoMayorCero(xs) 

votosCandPresidente :: String -> [(String, String)] -> [Int] -> Int
votosCandPresidente p [(a,b)] [v] | p == a = v
votosCandPresidente p (x:xs) (y:ys) | p == fst(x) = y 
                                    | otherwise = votosCandPresidente p (xs) (ys)

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

-- Ejercicio 4

masVotado :: [(String, String)] -> [Int] -> String
masVotado [(a,b)] [v] | a /= b && v > 0 = a
masVotado (x:w:xs) (y:z:ys) | mayorVotos(y:z:ys) == y = fst(x)
                            | otherwise = masVotado (w:xs) (z:ys)

mayorVotos :: [Int] -> Int
mayorVotos [x] = x 
mayorVotos (x:y:xs) | x >= y = mayorVotos(x:xs)
                    | x < y = mayorVotos(y:xs)

proximoPresidente :: [(String,String)] -> [Int] -> String
proximoPresidente [(a,b)] [v] | a /= b && v > 0 = a
proximoPresidente (x:w:xs) (y:z:ys) | formulasValidas(x:w:xs) == True && cantElementosFormulas(x:w:xs) == cantElementosVotos(y:z:ys) && elementosVotosMayoresCero(y:z:ys) == True && unoMayorCero(y:z:ys) == True = masVotado (x:w:xs) (y:z:ys)