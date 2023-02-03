"""
Nombre: Javier Valle
Carnet: 20159
Fecha: 02/02/2023
"""

import bayes as b

# Definiendo la estructura de la red bayesiana.


# El usuario ingresa las probabilidades de cada evento.
probabilidades = {
    'A': 0.5,
    'B': 0.5,
    'C': 0.5,
    'D': 0.5,
    'E': 0.5,
    'F': 0.5,
    'G': 0.5
}

bayes = b.Bayes(probabilidades)