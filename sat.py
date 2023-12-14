import networkx as nx
from verificar import verificar_satisfactibilidad
from independent_set import independent_set_solver

def sat_solver(G, dicc_nodos, entrada, valores_asignados):
    """
    Acercamiento al problema 3-sat mediante un algoritmo Greedy para independent-set.
    """
    S = nx.Graph()
    k = len(entrada)

    if(verificar_satisfactibilidad(entrada, valores_asignados)):
        return valores_asignados

    S = independent_set_solver(G)

    if(S.number_of_nodes() > k):
        return("No hay solución")

    
    