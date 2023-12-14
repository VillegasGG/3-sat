import networkx as nx
import matplotlib.pyplot as plt

def lista_a_grafo(entrada):
    """
    Convierte de una lista a un grafo, donde cada nodo se nombra de forma vi,j
    v: vertice
    i: valor de 1 a n de acuerdo a la posicion de la clausula
    j: valor de 1 a n de acuerdo a la posicion del literal en la clausula
    """
    # Crear un grafo vacío
    G = nx.Graph()

    # Lista de clausulas literales
    lista_clausulas = []

    # Diccionario que relaciona los nombres de los nodos con su respectiva literal
    nodo_literal = {}

    # Para cada clausula 
    for i, clausula in enumerate(entrada):
        nodos = []
        lista_literales = []

        # Cada literal se convierte en un nodo de la forma vi,j
        for j, literal in enumerate(clausula):
            nuevo_nodo = f"v{i+1},{j+1}"     # Se construye el nombre del nodo
            nodos.append(nuevo_nodo)
            nodo_literal[nuevo_nodo] = literal
            lista_literales.append(literal.strip())
        
        # Agregar clausula a lista_clausulas
        lista_clausulas.append(lista_literales)

        # Agregar los nodos al grafo
        G.add_nodes_from(nodos)
        
        # Conectar cada nodo de la clausula
        G.add_edge(nodos[0], nodos[1], length = 5)
        G.add_edge(nodos[1], nodos[2], length = 5)
        G.add_edge(nodos[0], nodos[2], length = 5)
    
    # Agregar aristas entre nodos con conflictos
    G = formar_enlaces_conflictos(G, nodo_literal)

    grafica(G, "Graph.png")
    return(G, nodo_literal, lista_clausulas)

def formar_enlaces_conflictos(G, literales):
    """
    Forma los enlaces entre nodos con conflictos
    """
    for nodo in G.nodes():
        # Obtener el nombre y valor del nodo actual
        nombre_nodo = str(nodo).strip()
        valor_nodo = literales[nombre_nodo].strip()

        #Si el nodo es positivo
        if(valor_nodo[0]!='¬'):
            # Verificar si la negación del nodo esta en el grafo
            negacion_nodo = ('¬' + valor_nodo).strip()
            negaciones_nodo = []
            for llave, valor in literales.items():
                if(valor.strip() == negacion_nodo.strip()):
                    negaciones_nodo.append(llave)
                    # Si la negación está presente, formar un enlace
                    G.add_edge(nodo, llave, length = 200)
                
    return G


def grafica(G, nombre):
    """
    Representacion grafica del grafo obtenido
    """
    pos = nx.circular_layout(G)
    # nx.draw(G, with_labels=True, node_color="pink", font_size=7)
    nx.draw_networkx_edges(G, pos, width = 1, alpha = 0.5)
    nx.draw(G, pos, with_labels = True, node_color = "#F07081", edge_color='#85929E', node_size = 400, font_size=10)
    plt.savefig(nombre, format="PNG")
    plt.close()


def graficar_solucion(G, S):
    pos = nx.circular_layout(G)

    nx.draw_networkx_edges(G, pos, width = 1, alpha = 0.5)
    nx.draw(G, pos, with_labels = True, node_color = "#F07081", edge_color='#85929E', node_size = 400, font_size=10)
    
    options = {"edgecolors": "tab:gray", "node_size": 700, "alpha": 0.9}
    nx.draw_networkx_nodes(G, pos, nodelist=S.nodes, node_color="#7B68EE", **options)
    plt.savefig("independent_set.png", format="PNG")
    plt.close()