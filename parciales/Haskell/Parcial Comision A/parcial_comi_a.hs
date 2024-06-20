{-Primer Ejercicio-}

hayQueCodificar :: Char -> [(Char, Char)] -> Bool
hayQueCodificar _ [] = False
hayQueCodificar c (m:mapeo) | perteneceAlPrimero c (m:mapeo) = True
                            | otherwise = hayQueCodificar c (mapeo)

perteneceAlPrimero :: Char -> [(Char, Char)] -> Bool
perteneceAlPrimero _ [] = False
perteneceAlPrimero c (m:mapeo)  | c == fst (m) = True
                                | otherwise  = perteneceAlPrimero c (mapeo)


{-Segundo Ejericio-}
cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char, Char)] -> Int
cuantasVecesHayQueCodificar c [frase] [mapeo]   | hayQueCodificar c [mapeo] == False = 0
                                                | hayQueCodificar c [mapeo] && c == frase = 1
cuantasVecesHayQueCodificar c (f:frase) (m:mapeo)   | hayQueCodificar c (m:mapeo) == False || apareceEnFrase c (f:frase) == False = 0
                                                    | hayQueCodificar c (m:mapeo) && apareceEnFrase c (f:frase) =  cuantasVecesAparece c (f:frase)

apareceEnFrase :: Char -> [Char] -> Bool
apareceEnFrase _ [] = False
apareceEnFrase c (f:frase)  | c == f = True
                            | otherwise = apareceEnFrase c (frase)

cuantasVecesAparece :: Char -> [Char] -> Int
cuantasVecesAparece _ [] = 0
cuantasVecesAparece c (f:frase) | c == f = 1 + cuantasVecesAparece c (frase)
                                | otherwise = cuantasVecesAparece c (frase)

{-Tercer Ejercicio-} 
laQueMasHayQueCodificar :: [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificar [frase] _ = frase
laQueMasHayQueCodificar (f:f1:frase) (m:mapeo)  | cuantasVecesHayQueCodificar f (f:f1:frase)  (m:mapeo) >= cuantasVecesHayQueCodificar f1  (f:f1:frase) (m:mapeo) = laQueMasHayQueCodificar (f:frase) (m:mapeo)
                                                | otherwise = laQueMasHayQueCodificar (f1:frase) (m:mapeo) 

{-Parcial Comision A-}
{-Cuarto Ejercicio-}
codificarFrase :: [Char] -> [(Char, Char)] -> [Char]
codificarFrase [] _ = []
codificarFrase (f:frase) (m:mapeo)  | hayQueCodificar f (m:mapeo) = [snd(m)] ++ codificarFrase frase mapeo
                                    | otherwise = [f] ++ codificarFrase frase mapeo