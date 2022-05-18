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


def generateEmptyList(n):
    l = []
    for i in range(n):
        l.append([])
        
    return l


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


def tabooSearch(distance_matrix, taboo_length, before_jump_count, search_depth):
    permutation = generateRandomPermutation(len(distance_matrix))
    taboo_list = []
    
    # Add first permutation as best
    # improvements = [permutation, taboo_list, swap]
    improvements = [[permutation, generateEmptyList(taboo_length), []]]
    best_solution = [permutation, calculateDistance(permutation, distance_matrix)]
    for t in range(taboo_length):   # Create taboo list
        taboo_list.append([])
    
    got_worse_solution_count = 0
    for i in range(search_depth):
        new_permutation = getBestNeighbour(permutation, distance_matrix, taboo_list).copy()
        
        # Check if solution got same/worse
        if calculateDistance(new_permutation, distance_matrix) >= best_solution[1]:
            got_worse_solution_count += 1
        else:
            got_worse_solution_count = 0
        
        # Remove additional taboo element after returning
        if len(taboo_list) > taboo_length:
            taboo_list.pop()
        
        # Replace the last added taboo element
        taboo_list[i % taboo_length] = getPermutationDifference(permutation, new_permutation)
        
        if got_worse_solution_count >= before_jump_count:     # Should we return to last best solution
            # Returns solution before all swaps in taboo list
            new_permutation = improvements[-1][0].copy()   # Best recorded permutation
            taboo_list = improvements[-1][1].copy()    # Taboo list at that time
            taboo_list.append(improvements[-1][2].copy())  # Forbid going the same way, pop later
            if len(improvements) > 1:
                improvements.pop()                  # Don't return to that point again
            got_worse_solution_count = 0
        elif calculateDistance(new_permutation, distance_matrix) <\
                calculateDistance(improvements[-1][0], distance_matrix):    # Is new permutation best so far?
            where_to_next = getPermutationDifference(
                getBestNeighbour(
                    new_permutation, distance_matrix, taboo_list), new_permutation)
            improvements.append([new_permutation,
                                 taboo_list.copy(),
                                 where_to_next])
            if calculateDistance(new_permutation, distance_matrix) < best_solution[1]:
                best_solution[0] = new_permutation
                best_solution[1] = calculateDistance(new_permutation, distance_matrix)
                print('New best solution length', best_solution[1])
        
        permutation = new_permutation.copy()
    
    return best_solution

