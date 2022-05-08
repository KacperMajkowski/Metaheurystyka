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


def tabooSearch(distance_matrix, taboo_length, before_jump_count, search_depth):
    permutation = generateRandomPermutation(len(distance_matrix))
    print('random perm', permutation, 'len', calculateDistance(permutation, distance_matrix))
    taboo_list = []
    improvements = []   # improvements = [permutation, taboo_list, swap]
    for t in range(taboo_length):   # Create taboo list
        taboo_list.append([])
    
    got_worse_solution_count = 0
    for i in range(search_depth):
        new_permutation = getBestNeighbour(permutation, distance_matrix, taboo_list).copy()
        
        # At first permutation as best
        if len(improvements) == 0:
            improvements.append([new_permutation, taboo_list, getPermutationDifference(new_permutation, permutation)])
        
        print('swapped ', getPermutationDifference(permutation, new_permutation))
        print('new_permutation', new_permutation, 'length', calculateDistance(new_permutation, distance_matrix),
              'vs permutation', permutation, 'length', calculateDistance(permutation, distance_matrix))
        
        # Check if solution got worse
        if calculateDistance(new_permutation, distance_matrix) > calculateDistance(permutation, distance_matrix):
            got_worse_solution_count += 1
            print('Got worse solution', got_worse_solution_count, 'times')
        else:
            got_worse_solution_count = 0
        
        # Remove additional taboo element after returning
        if len(taboo_list) > taboo_length:
            taboo_list.pop()
        
        # Replace the last added taboo element
        taboo_list[i % taboo_length] = getPermutationDifference(permutation, new_permutation)
        print('taboo list:', taboo_list)
        
        if got_worse_solution_count >= before_jump_count:     # Should we return to last best solution
            # Returns solution before all swaps in taboo list
            new_permutation = improvements[-1][0]   # Best recorded permutation
            taboo_list = improvements[-1][1]    # Taboo list at that time
            taboo_list.append(improvements[-1][2])  # Forbid going the same way, pop later
            improvements.pop()                  # Don't return to that point again
            print('returned to', new_permutation)
            got_worse_solution_count = 0
        elif calculateDistance(new_permutation, distance_matrix) <\
                calculateDistance(improvements[-1][0], distance_matrix):    # Is new permutation best so far?
            improvements.append([new_permutation, taboo_list, getPermutationDifference(new_permutation, permutation)])
        
        permutation = new_permutation
        print('improvements:', improvements)
    
    print('new perm len', calculateDistance(permutation, distance_matrix))
    return permutation


print(tabooSearch([[1, 2, 3, 4], [44, 55, 66, 77], [10, 20, 30, 40], [100, 101, 102, 103]], 3, 3, 10))
