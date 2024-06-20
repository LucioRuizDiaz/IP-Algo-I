-- relacionesValidas
relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [x] | fst(x) == snd(x) = False
                        | fst(x) /= snd(x) = True
relacionesValidas (a:b:xs) | fst(a) == fst(b) && snd(a) == snd(b) = False
                                    | fst(a) == snd(a) || fst(b) == snd(b) = False
                                    | fst(a) == snd(b) && fst(b) == snd(a) = False
                                    | otherwise = relacionesValidas(a:xs) && relacionesValidas(b:xs)


-- personas
personas :: [(String,String)] -> [String]
personas [x] | perteneceRValidas([x]) = [fst(x),snd(x)]
personas (a:xs) | perteneceRValidas(a:xs) = eliminaRepetidos( [fst(a), snd(a)] ++ personas(xs) )


perteneceRValidas :: [(String,String)] -> Bool
perteneceRValidas (xs) | relacionesValidas(xs) == True = True
                       | otherwise = False
                                    
eliminaRepetidos :: [String] -> [String]
eliminaRepetidos [] = []
eliminaRepetidos [x] = [x]
eliminaRepetidos (x:xs) | pertenece x (xs) == False = x:(eliminaRepetidos (xs))
                        | pertenece x (xs) == True = eliminaRepetidos (xs)

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece x (y:xs) | x == y = True
                   | x /= y = pertenece x (xs)

-- amigosDe
amigosDe :: String -> [(String,String)] -> [String]
amigosDe a [b] | perteneceRValidas([b]) && esElemento a (b) == True = [fst(b), snd(b)]
                | perteneceRValidas([b]) && esElemento a (b) == False = []
amigosDe x (y:xs) | (esElemento x (y)) == True  && (perteneceRValidas(y:xs)) = [fst(y),snd(y)] ++ (amigosDe x (xs))
                  | (esElemento x (y)) == False && (perteneceRValidas(y:xs)) = (amigosDe x (xs))


esElemento :: String -> (String,String) -> Bool
esElemento x (y) = fst(y) == x || snd(y) == x

-- personaConMasAmigos
{-

personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos [x] = fst(x)
personaConMasAmigos (x:y:xs) | (cantVeces (fst(x)) (x:y:xs) >= cantVeces (fst(y)) (x:y:xs)) = personaConMasAmigos(x:xs)
                             | (cantVeces (fst(x)) (x:y:xs) <= cantVeces (fst(y)) (x:y:xs)) = personaConMasAmigos(y:xs)


cantVeces :: String -> [(String, String)] -> Int
cantVeces _ [] = 0
cantVeces x (a:xs) | esElemento x (a) == True && perteneceRValidas(a:xs) == True = 1 + cantVeces x (xs) 
                   | esElemento x (a) == False && perteneceRValidas(a:xs) == True = cantVeces x (xs) 

personasRepe :: [(String,String)] -> [String]
personasRepe [x] | perteneceRValidas([x]) = [fst(x),snd(x)]
personasRepe (a:xs) | perteneceRValidas(a:xs) = [fst(a), snd(a)] ++ personasRepe(xs)

elemMayor :: [Int] -> Int
elemMayor [] = 0
elemMayor [x] = x 
elemMayor (x:xs) | x >= head(xs) = elemMayor (x:tail(xs))
                 | x <= head(xs) = elemMayor (xs)
-}