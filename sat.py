import networkx as nx
from verificar import verificar_satisfactibilidad
from independent_set import independent_set_solver

def sat_solver(G, dicc_nodos, entrada):
    """
    Acercamiento al problema 3-sat mediante un algoritmo Greedy para independent-set.
    """
    s_graph = nx.Graph()
    k = len(entrada)
    
    s_graph = independent_set_solver(G)

    if(s_graph.number_of_nodes() > k):
        return("No hay solución")

    valores_asignados = asignar_valores(s_graph, dicc_nodos)

    if(verificar_satisfactibilidad(entrada, valores_asignados)):
        print("Valores asignados a las literales: ")
        for key, value in valores_asignados.items():
            print(str(key) + ": " + str(value))
    else:
        print("No se encuentra solución")
    
def asignar_valores(S, dicc_nodos):
    valores_asignados = {}
    literales = []              # Literales en el independent set

    for nodo in S.nodes:
        literal = dicc_nodos[nodo]
        literales.append(literal.strip())
    
    literales = list(set(literales))
   
    for literal in literales:
        if(literal[0] == "¬"):
            valores_asignados[literal[1:]] = False
        else:
            valores_asignados[literal] = True

    return valores_asignados