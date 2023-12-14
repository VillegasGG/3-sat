from input import read_cnf_from_file
from representacion_grafo import lista_a_grafo
from sat import sat_solver
import time

def main():
    # Leer cláusulas
    doc_input = "entrada.txt"
    entrada = read_cnf_from_file(doc_input)

    # Pasar lista a grafo
    empezar = time.time_ns()
    G, dicc_nodos, lista_entrada = lista_a_grafo(entrada)

    # SAT
    sat_solver(G, dicc_nodos, lista_entrada)
    terminar = time.time_ns()

    print("\nDuración: " + str((terminar-empezar)/1e9) + " segundos")

if __name__ == "__main__":
    main()
