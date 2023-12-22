import networkx as nx
from verificar import verificar_satisfactibilidad
from independent_set import independent_set_solver
from representacion_grafo import graficar_solucion

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
        graficar_solucion(G, s_graph)
    else:
        print("No se encuentra solución")
    
def asignar_valores(S, dicc_nodos):
    valores_asignados = {}
    literales = []              # Literales de entrada (positivas)
    literales_true = []           # Literales del independent set

    for key, value in dicc_nodos.items():
        literal = value.strip()
        literales.append(literal.strip())

    for literal in literales:
        valores_asignados[literal] = False

    for nodo in S.nodes:
        literal_true = dicc_nodos[nodo]
        literales_true.append(literal_true.strip())

    for literal in literales_true:
        if(literal[0] == "¬"):
            valores_asignados[literal[1:]] = False
        valores_asignados[literal] = True

    diccionario_filtrado = {llave: valor for llave, valor in valores_asignados.items() if not llave.startswith('¬')}
    

    return diccionario_filtrado

