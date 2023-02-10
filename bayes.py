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
        # Copia de la red bayesiana.
        self.red_bayesiana = list(probabilidades.copy())

        # print("Red Bayesiana: ", self.red)
        # print("Probabilidades: ", self.probabilidades)

        self.descrita() # Verificando que la red sea descrita.
        self.compacta() # Devolviendo la red compacta.
        self.enumeracion() # Realizando el algoritmo de enumeración sobre la red bayesiana.

    def inferencia(red, probs, query): # Método para calcular las probabilidades dadas en el query.

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

    def enumeracion(self): # Método para realizar el algoritmo de enumeración sobre la red bayesiana.
    
        # Verificando que la suma de las probabilidades sea 1 en el diccionario.
        for node, values in self.probabilidades.items():
            if sum(values["distribucion"]) != 1:
                print("La suma de las probabilidades no es 1.")
                return False
            else: 
                print("La suma de las probabilidades es 1.")
                return True

    def descrita(self): #Método para verificar que la red sea descrita.
        
        nodos = self.probabilidades.keys()

        print("Nodos: ", nodos)

        for node in nodos: # Verificando que no haya dependencias circulares.
            if node in self.probabilidades[node]["padres"]:
                print("Existen dependencias circulares.")
                return False
        
            # Verificando que todos los papás del nodo estén en la red.
            for padre in self.probabilidades[node]["padres"]:
                if padre[0] not in nodos: 
                    print("Hay padres que no existen")
                    return False

            # Verificando que los nodos tengan distribuciones válidas de probabilidades.
            if not isinstance(self.probabilidades[node]["distribucion"], list):
                print("La distribución no es válida.")

        print("La red está completamente descrita")

        return True

    def compacta(self): # Devolviendo la red compacta.
        # Devolver un string como P(A)P(B|A)P(C|A)P(D|C) de la red bayesiana.

        # Inicializando la red bayesiana.
        red_c = ""

        # Recorriendo la primera red bayesiana.
        for nodo, valores in self.red.items():
            # Verificando que el nodo no tenga padres.
            if len(valores) == 0:
                red_c += "P(" + nodo + ")"
            # Verificando que el nodo tenga padres.
            else:
                red_c += "P(" + nodo + "|"
                for padre in valores:
                    red_c += padre
                red_c += ")"

        print("Red Bayesiana Compacta: ", red_c)
        return red_c

    def devolver_red(self): # Devolviendo la red bayesiana.
        return self.red_bayesiana