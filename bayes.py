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

    def inferencia(red, probs, query): 

        # Inicializando la probabilidad a 1.
        prob = 1

        # Viendo quienes son los padres de la variable.
        padres = red[query[0]]

        # Multiplicando la probabilidad de la variable con la de sus padres.
        for padre in padres:
            valor_padre = None

            # Buscando el valor de la variable padre en la consulta.
            for q in query[1:]:
                if q[0] == padre:
                    valor_padre = q[1]

            # Si no se encuentra el valor de la variable padre en la consulta, se retorna None.
            if valor_padre is None:
                return None

            # Buscando el índice de la variable padre en la consulta.
            indice_padre = probs[padre]['padres'].index((query[0], valor_padre))

            # Multiplicando la probabilidad de la variable con la de sus padres.
            prob *= probs[padre]['distribucion'][indice_padre]

        # Retornando la probabilidad de la variable.
        return prob