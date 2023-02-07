"""
Nombre: Javier Valle
Carnet: 20159
Fecha: 02/02/2023

Clase que se encarga de construir el modelo de Bayes para calcular las probabilidades que se ingresen en el programa.
"""

class Bayes(object): 

    # Recibe un diccionario con las probabilidades de cada evento.
    def __init__(self, red, probabilidades):
        self.red = red
        self.probabilidades = probabilidades

        print("Red Bayesiana: ", self.red)
        print("Probabilidades: ", self.probabilidades)