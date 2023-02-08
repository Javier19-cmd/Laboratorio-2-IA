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
        # Se usará el método de eliminación.

        # Obteniendo la lista de nodos que hay en la red.
        nodos = list(self.probabilidades.keys())

        while len(nodos) > 1:

            # Seleccionando el nodo con menos padres.
            grado_conetividad = [len(self.probabilidades[nodo]) for nodo in nodos]
            indice = grado_conetividad.index(min(grado_conetividad))
            
            # Eliminando del diccionario el nodo con menos padres.
            vecinos = self.red_bayesiana[indice]
            del self.red_bayesiana[indice]
            nodos.pop(indice)

        #print(self.red_bayesiana)