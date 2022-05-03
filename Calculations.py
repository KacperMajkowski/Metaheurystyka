import random


def generateRandomPermutation(length):
    permutation = []
    for i in range(length):
        permutation.append(i)
    
    random.shuffle(permutation)
    return permutation


def getPermutationDifference(perm1, perm2):
    diff = []
    for i in range(len(perm1)):
        if perm1[i] != perm2[i]:
            diff.append(i)
    
    return diff


def swapPermutation(permutation, i, j):
    new_permutation = permutation.copy()
    new_permutation[i] = permutation[j]
    new_permutation[j] = permutation[i]
    return new_permutation


def calculateDistance(permutation, distance_matrix):
    
    total_distance = 0
    for i in range(len(permutation)):
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
    if len(neighbours) == 0:
        print('No possible neighbours')
    
    bestNeighbour = neighbours[0]
    bestDistance = calculateDistance(bestNeighbour, distance_matrix)
    for n in neighbours:
        if calculateDistance(n, distance_matrix) < bestDistance:
            bestNeighbour = n
            bestDistance = calculateDistance(bestNeighbour, distance_matrix)
            
    return bestNeighbour


def tabooSearch(distance_matrix, taboo_length, search_depth):
    permutation = generateRandomPermutation(len(distance_matrix))
    print('random perm', permutation, 'len', calculateDistance(permutation, distance_matrix))
    taboo_list = []
    for t in range(taboo_length):
        taboo_list.append([])
    
    for i in range(search_depth):
        new_permutation = getBestNeighbour(permutation, distance_matrix, taboo_list).copy()
        taboo_list[i % taboo_length] = getPermutationDifference(permutation, new_permutation)
        print('new permutation =', new_permutation)
        print('swapped ', getPermutationDifference(permutation, new_permutation))
        print('taboo list =', taboo_list)
        permutation = new_permutation.copy()
    
    print('new perm len', calculateDistance(permutation, distance_matrix))
    return permutation


print(tabooSearch([[1, 2, 3, 4], [4, 5, 6, 7], [10, 20, 30, 40], [100, 101, 102, 103]], 3, 10))
