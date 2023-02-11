"""
Nombre: Javier Valle
Carnet: 20159
Fecha: 02/02/2023
"""

import bayes

# Creando la estructura de la red bayesiana.
red = {
    "A": ["B", "C"],
    "B": [],
    "C": ["D"],
    "D": []
}

# Creando las probabilidades condicionales de la red bayesiana.
probabilidades = {
    "A": {"distribucion": [0.1, 0.9], "padres": []},
    "B": {"distribucion": [0.8, 0.2], "padres": [("A", 0), ("A", 1)]}, # 0.8 = P(B=0|A=0, C=0), 0.2 = P(B=0|A=0, C=1)
    "C": {"distribucion": [0.7, 0.3], "padres": [("A", 0), ("A", 1)]}, # 0.7 = P(C=0|A=0, C=0), 0.3 = P(C=0|A=0, C=1)
    "D": {"distribucion": [0.6, 0.4], "padres": [("C", 0), ("C", 1)]} # 0.6 = P(D=0|C=0), 0.4 = P(D=0|C=1)
}

bayes.Bayes(red, probabilidades) # Enviando los datos a la clase Bayes.

query = ('C', ('D', 1))

bayes.Bayes.inferencia(red, probabilidades, query)


#print(b.Bayes.inferencia(red, probabilidades, query))