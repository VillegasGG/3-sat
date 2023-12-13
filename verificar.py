def verificar_satisfactibilidad(entrada, valores_asignados):
    """
    Verifica si el resultado de la expresion completa es True o False
    Si alguna clausula es Falso, la expresión no se satisface
    """
    for clausula in entrada:
        verificacion = verificar_clausula(clausula, valores_asignados)
        if verificacion is False:
            return False
    return True

def verificar_clausula(clausula, valores_asignados):
    """
    Verifica si el resultado de la clausula es True o False
    Si alguna literal en la clausula es True, la clausula se satisface
    """
    for literal in clausula:
        if verificar_literal(literal, valores_asignados):
            return True
    return False

def verificar_literal(literal, valores_asignados):
    """Verifica si la literal es positiva o negativa (True o False)"""
    if literal[0] == '¬':
        return valores_asignados.get(literal[1:], False) is False
    return valores_asignados.get(literal, False) is True

asig = {'X1' : True,
        'X2' : True,
        'X3' : True,
        }

# print(verificar_literal("X1", asig))

# print(verificar_clausula(["¬X1", "X2", "¬X3"], asig))
# print(verificar_clausula(["¬X1", "¬X2"], asig))

# print(verificar_satisfactibilidad([["X1", "X2", "X3"],["¬X1", "¬X2"],["X1", "X2", "X3"]], asig))
