import Test.HUnit
import Solucion
import Data.List
-- No está permitido agregar nuevos imports.

runCatedraTests = runTestTT allTests

allTests = test [
    "esMinuscula" ~: testsEjesMinuscula,
    "letraANatural" ~: testsEjletraANatural,
    "desplazar" ~: testsEjdesplazar,
    "cifrar" ~: testsEjcifrar,
    "descifrar" ~: testsEjdescifrar,
    "cifrarLista" ~: testsEjcifrarLista,
    "frecuencia" ~: testsEjfrecuencia,
    "cifradoMasFrecuente" ~: testsEjcifradoMasFrecuente,
    "esDescifrado" ~: testsEjesDescifrado,
    "todosLosDescifrados" ~: testsEjtodosLosDescifrados,
    "expandirClave" ~: testsEjexpandirClave,
    "cifrarVigenere" ~: testsEjcifrarVigenere,
    "descifrarVigenere" ~: testsEjdescifrarVigenere,
    "peorCifrado" ~: testsEjpeorCifrado,
    "combinacionesVigenere" ~: testsEjcombinacionesVigenere
    ]


testsEjesMinuscula = test [
    esMinuscula 'd' ~?= True,
    esMinuscula 'A' ~?= False,
    esMinuscula '0' ~?= False,
    esMinuscula '$' ~?= False
    ]

testsEjletraANatural = test [
    letraANatural 'b' ~?= 1,
    letraANatural 'h' ~?= 7,
    letraANatural 'z' ~?= 25,
    letraANatural 'a' ~?= 0
    ]

testsEjdesplazar = test [
    desplazar 'a' 3 ~?= 'd',
    desplazar 'z' 1 ~?= 'a',
    desplazar 'a' (-1) ~?= 'z',
    desplazar 'a' (-27) ~?= 'z',
    desplazar 'z' 27 ~?= 'a',
    desplazar '0' 1 ~?= '0',
    desplazar 'A' 5 ~?= 'A',
    desplazar '%' 1 ~?= '%'
    ]

testsEjcifrar = test [
    cifrar "computacion" 3 ~?= "frpsxwdflrq",
    cifrar "holis" 0 ~?= "holis",
    cifrar "abc0" (-27) ~?= "zab0",
    cifrar "x%yzB" 27 ~?= "y%zaB"
    ]

testsEjdescifrar = test [
    descifrar "frpsxwdflrq" 3 ~?= "computacion",
    descifrar "holis" 0 ~?= "holis",
    descifrar "zab0" (-27) ~?= "abc0",
    descifrar "y%zaB" 27 ~?= "x%yzB"
    ]

testsEjcifrarLista = test [
    cifrarLista ["compu", "labo", "intro"] ~?= ["compu", "mbcp", "kpvtq"],
    cifrarLista ["aaa","abcde0%","ABCyz"," "] ~?= ["aaa","bcdef0%","ABCab"," "],
    cifrarLista [] ~?= []
    ]

testsEjfrecuencia = test [
    frecuencia "taller" ~?= [16.666668,0.0,0.0,0.0,16.666668,0.0,0.0,0.0,0.0,0.0,0.0,33.333336,0.0,0.0,0.0,0.0,0.0,16.666668,0.0,16.666668,0.0,0.0,0.0,0.0,0.0,0.0], 
    frecuencia " " ~?= [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], 
    frecuencia "a" ~?= [100.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], 
    frecuencia "ComputaCion%" ~?= [11.111112,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11.111112,0.0,0.0,0.0,11.111112,11.111112,22.222223,11.111112,0.0,0.0,0.0,11.111112,11.111112,0.0,0.0,0.0,0.0,0.0]
    ]

testsEjcifradoMasFrecuente = test [
    cifradoMasFrecuente "taller" 3 ~?= ('o', 33.333336),
    cifradoMasFrecuente "a" 5 ~?= ('f', 100.0),
    cifradoMasFrecuente "computacion" 26 ~?= ('c', 18.181818),
    cifradoMasFrecuente "neuquEN%" (-5) ~?= ('p', 40.0)
    ]

testsEjesDescifrado = test [
    esDescifrado "taller" "compu" ~?= False,
    esDescifrado "zabc#" "bcde#" ~?= True,
    esDescifrado " " " " ~?= True,
    esDescifrado "abc0A" "zab0A" ~?= True,
    esDescifrado "hola" "asda" ~?= False,
    esDescifrado "hola" "mtqf" ~?= True
    ]

testsEjtodosLosDescifrados = test [
    todosLosDescifrados ["compu", "frpsx", "mywza"] ~?= [("compu", "frpsx"), ("frpsx", "compu")],
    todosLosDescifrados ["compu", "frpsx", "mywze"] ~?= [("compu","frpsx"),("frpsx","compu"),("compu","mywze"),("mywze","compu"),("frpsx","mywze"),("mywze","frpsx")], 
    todosLosDescifrados ["hola", "pwtq", "iemb", "ryvb"] ~?= [],
    todosLosDescifrados ["neu#uen","ofv#vfo", "tka#akt", "ypf#fpy"] ~?= [("neu#uen","ofv#vfo"),("ofv#vfo","neu#uen"),("neu#uen","tka#akt"),("tka#akt","neu#uen"),("neu#uen","ypf#fpy"),("ypf#fpy","neu#uen"),("ofv#vfo","tka#akt"),("tka#akt","ofv#vfo"),("ofv#vfo","ypf#fpy"),("ypf#fpy","ofv#vfo"),("tka#akt","ypf#fpy"),("ypf#fpy","tka#akt")], 
    todosLosDescifrados ["d4t0S", "hexsS", "qngbS", "y4ojS"] ~?= [("hexsS","qngbS"),("qngbS","hexsS")]
    ]


testsEjexpandirClave = test [
    expandirClave "compu" 8 ~?= "compucom",
    expandirClave "conquista" 3 ~?= "con",
    expandirClave "oso" 15 ~?= "osoosoosoosooso"
    ]

testsEjcifrarVigenere = test [
    cifrarVigenere "computacion" "ip" ~?= "kdueciirqdv",
    cifrarVigenere "computacion" "a" ~?= "computacion", 
    cifrarVigenere "laboM$a7" "labo" ~?= "waccM$b7", 
    cifrarVigenere "labo" "labos" ~?= "wacc",
    cifrarVigenere " " "no" ~?= " "  
    ]

testsEjdescifrarVigenere = test [
    descifrarVigenere "kdueciirqdv" "ip" ~?= "computacion",
    descifrarVigenere "computacion" "a" ~?= "computacion", 
    descifrarVigenere "toeunpm" "presupuesto" ~?= "exactas"
    ] 

testsEjpeorCifrado = test [
    peorCifrado "computacion" ["ip", "asdef", "ksy"] ~?= "asdef", 
    peorCifrado "pabe" ["pabe", "cero", "uno", "exactas"] ~?= "uno"
    ]

testsEjcombinacionesVigenere = test [
    combinacionesVigenere ["hola", "mundo"] ["a", "b"] "ipmb" ~?= [("hola", "b")],
    combinacionesVigenere ["hola", "mundo"] ["a", "b"] "mundo" ~?= [("mundo", "a")] ,
    combinacionesVigenere ["compu", "zompu", "oompu"] ["ratos", "gatos", "datos"] "fofdm" ~?= [("compu","datos"),("zompu","gatos"),("oompu","ratos")], 
    combinacionesVigenere ["A", "compu"] ["tomate", "n"] "A" ~?= [("A", "tomate"),("A","n")],
    combinacionesVigenere [" ", "compu"] ["hola","chau"] "asdasd" ~?= [] 
    ]

-- Funciones útiles

-- margetFloat(): Float
-- asegura: res es igual a 0.00001
margenFloat = 0.00001

-- expectAny (actual: a, expected: [a]): Test
-- asegura: res es un Test Verdadero si y sólo si actual pertenece a la lista expected
expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- expectlistProximity (actual: [Float], expected: [Float]): Test
-- asegura: res es un Test Verdadero si y sólo si:
--                  |actual| = |expected|
--                  para todo i entero tal que 0<=i<|actual|, |actual[i] - expected[i]| < margenFloat()
expectlistProximity:: [Float] -> [Float] -> Test
expectlistProximity actual expected = esParecidoLista actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esParecidoLista :: [Float] -> [Float] -> Bool
esParecidoLista actual expected = (length actual) == (length expected) && (esParecidoUnaAUno actual expected)

esParecidoUnaAUno :: [Float] -> [Float] -> Bool
esParecidoUnaAUno [] [] = True
esParecidoUnaAUno (x:xs) (y:ys) = (aproximado x y) && (esParecidoUnaAUno xs ys)

aproximado :: Float -> Float -> Bool
aproximado x y = abs (x - y) < margenFloat


-- expectAnyTuplaAprox (actual: CharxFloat, expected: [CharxFloat]): Test
-- asegura: res un Test Verdadero si y sólo si:
--                  para algun i entero tal que 0<=i<|expected|,
--                         (fst expected[i]) == (fst actual) && |(snd expected[i]) - (snd actual)| < margenFloat()

expectAnyTuplaAprox :: (Char, Float) -> [(Char, Float)] -> Test
expectAnyTuplaAprox actual expected = elemAproxTupla actual expected ~? ("expected any of: " ++ show expected ++ "\nbut got: " ++ show actual)

elemAproxTupla :: (Char, Float) -> [(Char, Float)] -> Bool
elemAproxTupla _ [] = False
elemAproxTupla (ac,af) ((bc,bf):bs) = sonAprox || (elemAproxTupla (ac,af) bs)
    where sonAprox = (ac == bc) && (aproximado af bf)



-- expectPermutacion (actual: [T], expected[T]) : Test
-- asegura: res es un Test Verdadero si y sólo si:
--            para todo elemento e de tipo T, #Apariciones(actual, e) = #Apariciones(expected, e)

expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)