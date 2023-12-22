"""
Leer el documento de entrada
read_cnf_from_file recibe una formula booleana en forma normal conjuntiva (CNF)
y regresa una lista con las literales de las clausulas
"""
def read_cnf_from_file(filename):
    """Lee la fórmula en su forma normal conjuntiva de un txt"""
    cnf = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                clausulas_string = line.strip().split('∧')

            for i in clausulas_string:
                literales = (i.replace('(', '').replace(')', '').strip()).split(' ')
                cnf.append(literales)

            return cnf

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return None