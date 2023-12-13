import networkx as nx
import matplotlib.pyplot as plt

# # Crear un grafo vacío
# G = nx.Graph()

# # Agregar nodos
# G.add_node(1)
# G.add_nodes_from([2, 3, 4, 5, 6, 7, 8, 9, 10])

# # Agregar aristas
# G.add_edge(1, 2)
# G.add_edges_from([(1, 3), (2, 3), (7, 8), (7, 2)])

# # Verificar nodos y aristas
# print("Nodos:", G.nodes())
# print("Aristas:", G.edges())

# for i in G.nodes:
#     neighbors = list(G.neighbors(i))  # Obtener los vecinos de cada nodo
#     print(f"Los vecinos de {i} en G son: {neighbors}")

# nx.draw(G, with_labels=True, node_color='skyblue', font_weight='bold')
# plt.show()


# import networkx as nx

# def representar_3SAT_como_grafo(clausulas):
#     # Crear un grafo vacío
#     G = nx.Graph()

#     # Recorrer cada cláusula en el problema 3-SAT
#     for idx, clausula in enumerate(clausulas):
#         # Crear tres nodos para representar los literales en la cláusula
#         literal_nodes = [f"L{i}_{idx}" for i in range(3)]
        
#         # Agregar los nodos al grafo
#         G.add_nodes_from(literal_nodes)

#         # Conectar los nodos entre sí (cláusula 3-SAT)
#         G.add_edges_from([(literal_nodes[0], literal_nodes[1]), 
#                           (literal_nodes[1], literal_nodes[2]), 
#                           (literal_nodes[2], literal_nodes[0])])

#         # Conectar cada nodo de la cláusula con los nodos que representan la cláusula en el grafo
#         for literal_node in literal_nodes:
#             G.add_edge(literal_node, f"C{idx}")

#     nx.draw(G, with_labels=True, node_color='skyblue', font_weight='bold')
#     plt.show()
#     return G

# # Ejemplo de cláusulas (lista de literales)
# clausulas_ejemplo = [["a", "b", "~c"], ["~a", "~b", "c"]]
# grafo_3SAT = representar_3SAT_como_grafo(clausulas_ejemplo)

# # Mostrar nodos y aristas del grafo (opcional)
# print("Nodos del grafo:")
# print(grafo_3SAT.nodes())
# print("\nAristas del grafo:")
# print(grafo_3SAT.edges())

import matplotlib.pyplot as plt
import networkx as nx

G = nx.cubical_graph()
pos = nx.spring_layout(G, seed=3113794652)  # positions for all nodes

# nodes
options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
nx.draw_networkx_nodes(G, pos, nodelist=[0, 1, 2, 3], node_color="tab:red", **options)
nx.draw_networkx_nodes(G, pos, nodelist=[4, 5, 6, 7], node_color="tab:blue", **options)

# edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(0, 1), (1, 2), (2, 3), (3, 0)],
    width=8,
    alpha=0.5,
    edge_color="tab:red",
)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
    width=8,
    alpha=0.5,
    edge_color="tab:blue",
)


# some math labels
labels = {}
labels[0] = r"$a$"
labels[1] = r"$b$"
labels[2] = r"$c$"
labels[3] = r"$d$"
labels[4] = r"$\alpha$"
labels[5] = r"$\beta$"
labels[6] = r"$\gamma$"
labels[7] = r"$\delta$"
nx.draw_networkx_labels(G, pos, labels, font_size=22, font_color="whitesmoke")

plt.tight_layout()
plt.axis("off")
plt.show()