from verificar import verificar_satisfactibilidad
from independent_set import independent_set_solver

def sat_solver(G, dicc_nodos, entrada, valores_asignados):
    k = len(entrada)
    print("El tamaño de la entrada es: " + str(k))
    if(verificar_satisfactibilidad(entrada, valores_asignados)):
        return valores_asignados

    print("No se satisface ... aún")
    independent_set_solver(G)
    
    return("No hay solución")