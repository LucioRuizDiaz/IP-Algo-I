{-Ejercicio 1a-}
type Punto2D = (Float, Float)
prodInt :: Punto2D -> Punto2D -> Float
prodInt (a,b) (c,d) = (a*c)+(b*d)

{-Ejercicio 1b-}
todoMenor :: Punto2D -> Punto2D -> Bool
todoMenor (a,b) (c,d) = a < c && b < d

{-Ejercicio 1c-}
distanciaPuntos :: Punto2D -> Punto2D -> Punto2D
distanciaPuntos (a,b) (c,d) = ((a-c), (b-d))

{-Ejercicio 1d-}
type Coordenada = (Float, Float)
crearPar :: Float -> Float -> Punto2D
crearPar a b = (a,b)


{-Ejercicio 2-}
type Año = Integer
type EsBisiesto = Bool
bisiesto :: Año -> EsBisiesto
bisiesto año = not((mod año 4 /= 0) || ((mod año 100 == 0) && (mod año 400 /= 0))) 

{-Ejercicio 3-}
type Coordenada3d = (Float, Float, Float)
distanciaManhattan :: Coordenada3d -> Coordenada3d -> Float
distanciaManhattan (a,b,c) (d,e,f) = abs(a-d) + abs(b-e) + abs(c-f)


{-Ejercicio 4a-}
type Nombre = String
type ContactosTel1 = [String]
enLosContactos :: Nombre -> ContactosTel1 -> Bool
enLosContactos _ [] = False
enLosContactos nombre (c:contactos) | nombre == c = True
                                    | otherwise = enLosContactos nombre (contactos)


{-Ejercicio 4b
type Contacto = (String, String)
type ContactosTel = [(String, String)]
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto _ [] = []
agregarContacto contacto (c:contactos) | enLosContactos contacto (c:contactos) = -}
