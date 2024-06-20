
{-Primer Ejercicio-}
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas [relaciones] | fst (relaciones) == snd (relaciones) = False 
relacionesValidas (x:relaciones)    | hayRepetidos x (relaciones) = False
                                    | otherwise = relacionesValidas (relaciones) 


hayRepetidos :: (String, String) -> [(String, String)] -> Bool
hayRepetidos _ [] = False
hayRepetidos e (x:xs)   | fst(e) == fst(x) && snd(e) == snd(x) = True
                        | fst(e) == snd (x) && snd (e) == fst(x) = True
                        | otherwise = hayRepetidos e xs


{-Segundo Ejercicio-}
personas :: [(String, String)] -> [String]
personas [relaciones]   | relacionesValidas([relaciones]) = [fst(relaciones), snd(relaciones)]
personas (x:relaciones) | relacionesValidas(x:relaciones)  = eliminarRepetidos ( [fst(x), snd(x)] ++ personas(relaciones) ) 


eliminarRepetidos :: [String] -> [String]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs)    | pertenece x (xs) = eliminarRepetidos (xs)
                            | otherwise = x : eliminarRepetidos (xs)

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs)  | e == x = True
                    | otherwise = pertenece e (xs)

{-Simulacro de Parcial-}
{-Tercer ejercicio-}
amigosDe :: String -> [(String, String)] -> [String]
amigosDe persona [relaciones]   | perteneceAmigos persona [(relaciones)] && relacionesValidas([relaciones]) =   primerOSegundo persona [relaciones]
                                | otherwise = []
amigosDe persona (x:relaciones) | relacionesValidas(x:relaciones) = amigosDe persona [(x)] ++ amigosDe persona (relaciones)

primerOSegundo :: String -> [(String, String)] -> [String]
primerOSegundo persona [relaciones] | persona == fst (relaciones) = [snd(relaciones)]
                                    | persona == snd (relaciones) = [fst(relaciones)]

perteneceAmigos :: String -> [(String, String)] -> Bool
perteneceAmigos persona [relaciones]    | persona == fst (relaciones) || persona == snd (relaciones) = True
                                        | otherwise = False


{-Cuarto Ejercicio-}                        

personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos [relaciones] = fst(relaciones)
personaConMasAmigos (x:relaciones)  = contarLosAmigos [x] (relaciones)
             

contarLosAmigos :: [(String , String)] -> [(String , String)] -> String
contarLosAmigos [x] _ = fst(x)
contarLosAmigos [x] (y:relaciones)  | longitud (amigosDe (fst(x)) (x:y:relaciones)) >= longitud (amigosDe (fst(y)) (x:y:relaciones)) = contarLosAmigos [x] (relaciones)
                                    | otherwise = contarLosAmigos [y] (relaciones)


longitud :: [String] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

