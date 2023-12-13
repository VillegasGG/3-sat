from verificar import verificar_satisfactibilidad
from independent_set import *

def sat_solver(G, dicc_nodos, entrada, valores_asignados):
    k = len(entrada)
    print("El tamaño de la entrada es: " + str(k))
    if(verificar_satisfactibilidad(entrada, valores_asignados)):
        return valores_asignados

    print("No se satisface ... aún")
    menor = menor_grado(G)
    print(menor)
    G = grafo_inducido(G, menor)
    
    return("No hay solución")