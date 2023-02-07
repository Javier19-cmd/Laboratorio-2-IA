# Definiendo la estructura de la red bayesiana.
network = {
    'A': ['B', 'C'],
    'B': [],
    'C': ['D'],
    'D': []
}

# Definiendo las probabilidades condicionales de la red bayesiana.
cpds = {
    'A': {'distribution': [0.1, 0.9], 'parents': []},
    'B': {'distribution': [0.8, 0.2], 'parents': [('A', 0), ('A', 1)]}, # 0.8 = P(B=0|A=0, C=0), 0.2 = P(B=0|A=0, C=1)
    'C': {'distribution': [0.7, 0.3], 'parents': [('A', 0), ('A', 1)]}, # 0.7 = P(C=0|A=0, C=0), 0.3 = P(C=0|A=0, C=1)
    'D': {'distribution': [0.6, 0.4], 'parents': [('C', 0), ('C', 1)]} # 0.6 = P(D=0|C=0), 0.4 = P(D=0|C=1)
}

# Function to perform Bayesian inference
def infer_probability(network, cpds, query):
    """
    network: the structure of the Bayesian network
    cpds: the conditional probability distributions for each variable
    query: a tuple of the form (variable, value) representing the query variable and its desired value
    """
    # Initialize the probability to 1
    probability = 1
    
    # Viendo quienes son los padres de la variable.
    parents = network[query[0]]

   # print("Papás: ", parents)
    
    # Multiplicando la probabilidad de la variable con la de sus padres.
    for parent in parents:
        parent_value = None
        
        # Buscando el valor de la variable padre en la consulta.
        for q in query[1:]:
            if q[0] == parent:
                parent_value = q[1]
                
        # Si no se encuentra el valor de la variable padre en la consulta, se retorna None.
        if parent_value is None:
            return None
        
        # Buscando el índice de la variable padre en la consulta.
        parent_index = cpds[parent]['parents'].index((query[0], parent_value))
        
        # Multiplicando la probabilidad de la variable con la de sus padres.
        probability *= cpds[parent]['distribution'][parent_index]
        
    # Retornando la probabilidad de la variable.
    return probability


a = infer_probability(network, cpds, ('A', ('B', 1), ('C', 1), ('D', 1)))

print(a)