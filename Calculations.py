

def swapPermutation(permutation, i, j):
    new_permutation = permutation.copy()
    new_permutation[i] = permutation[j]
    new_permutation[j] = permutation[i]
    return new_permutation


def calculateDistance(permutation, distance_matrix):
    
    total_distance = 0
    for i in range(len(permutation) - 1):
        total_distance += distance_matrix[permutation[i]][permutation[(i + 1) % len(permutation)]]
    return total_distance


def getNeighbours(permutation, taboo_swaps):
    neighbours = []
    for i in range(len(permutation) - 1):
        for j in range(i + 1, len(permutation)):
            if [i, j] not in taboo_swaps:
                neighbours.append(swapPermutation(permutation, i, j))
                
    return neighbours


def getBestNeighbour(permutation, distance_matrix, taboo_list):
    neighbours = getNeighbours(permutation, taboo_list)
    
    bestNeighbour = neighbours[0]
    bestDistance = calculateDistance(bestNeighbour, distance_matrix)
    for n in neighbours:
        if calculateDistance(n, distance_matrix) < bestDistance:
            bestNeighbour = n
            bestDistance = calculateDistance(bestNeighbour, distance_matrix)
            
    return bestNeighbour

