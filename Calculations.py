

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


def getNeighbors(permutation, taboo_swaps):
    neighbors = []
    for i in range(len(permutation) - 1):
        for j in range(i + 1, len(permutation)):
            if [i, j] not in taboo_swaps:
                neighbors.append(swapPermutation(permutation, i, j))
                
    return neighbors
