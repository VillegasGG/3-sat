"""
Modulo del algoritmo independent set
"""
from representacion_grafo import grafica

def menor_grado(G):
    """
    Devuelve el vertice con menor grado de un grafo
    """
    min_value = float('inf')  # Inicializa con infinito
    nodo = ""
    for node in G.nodes():
        grado = G.degree[node]
        if(grado<min_value):
            min_value = grado
            nodo = node
    
    return nodo

def grafo_inducido(G, vx):
    """
    Genera el grafo inducido dado por G-S
    Donde S es el conjunto de vertices adyacentes a vx con sus aristas
    """
    g = G.copy()
    g0 = g.copy()
    adyacentes = g0.neighbors(vx)
    for key in adyacentes:
        g.remove_node(str(key))

    g.remove_node(str(vx))
    print(list(g.nodes))
    nombre_grafo = "G-N(" + str(vx) + ").png"
    grafica(g, nombre_grafo)
    return g
    