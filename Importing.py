import tsplib95


def importFile():
    problem = tsplib95.load('Tsp_problems/att48.tsp')
    return problem
    

def askUserForFilename():
    file_name = input("Podaj nazwę pliku\n")
    distance_matrix = importFile()
    return distance_matrix


print(askUserForFilename())
