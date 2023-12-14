from input import read_cnf_from_file
from representacion_grafo import lista_a_grafo
from sat import sat_solver

def main():
    # Leer cláusulas
    doc_input = "entrada.txt"
    entrada = read_cnf_from_file(doc_input)

    # Pasar lista a grafo
    G, dicc_nodos, lista_entrada = lista_a_grafo(entrada)

    # SAT
    sat_solver(G, dicc_nodos, lista_entrada)

if __name__ == "__main__":
    main()
