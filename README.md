# Explicación de la funcionalidad de la librería.

La presente librería permite crear y analizar redes bayesianas. Para lo mismo, se necsita crear lo siguiente: 

1. Una red que contenga los nodos y las aristas que se desean analizar de la siguiente forma: 

red = {
    "A": ["B", "C"],
    "B": [],
    "C": ["D"],
    "D": []
}

2. Una red de probabildades que contenga las probabilidades de cada nodo de la siguiente forma:

probabilidades = {
    "A": {"distribucion": [0.1, 0.9], "padres": []},
    "B": {"distribucion": [0.8, 0.2], "padres": [("A", 0), ("A", 1)]}, # 0.8 = P(B=0|A=0, C=0), 0.2 = P(B=0|A=0, C=1)
    "C": {"distribucion": [0.7, 0.3], "padres": [("A", 0), ("A", 1)]}, # 0.7 = P(C=0|A=0, C=0), 0.3 = P(C=0|A=0, C=1)
    "D": {"distribucion": [0.6, 0.4], "padres": [("C", 0), ("C", 1)]} # 0.6 = P(D=0|C=0), 0.4 = P(D=0|C=1)
}

3. Estas dos redes se deben pasar a la librería de Bayes de la siguiente forma: 

bayes = Bayes(red, probabilidades)

Esto devolverá un texto que indica si la red está completamente descrita o no.

4. Para calcular la probabilidad de una variable, se debe llamar a la función de la siguiente forma:

Crear un query de la siguiente forma:
query = ("A", ("B", 0), ("C", 1), ("D", 0))

Luego, llamar a la función de inferencia de la siguiente forma:
bayes.inferencia(red, probabilidades, query)

Con lo anterior se obtiene la probabilidad de la variable A, dada la evidencia de que B=0, C=1 y D=0.