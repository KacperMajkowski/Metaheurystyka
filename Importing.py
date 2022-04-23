
def importFile(file_name):
    
    # TODO: Get distance matrix from tspLib
    #  return distance_matrix
    pass
    

def askUserForFilename():
    file_name = input("Podaj nazwę pliku")
    distance_matrix = importFile(file_name)
    return distance_matrix
