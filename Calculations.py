
def calculateDistance(permutation, distance_matrix):
    
    total_distance = 0
    for i in range(len(permutation) - 1):
        total_distance += distance_matrix[permutation[i]][permutation[(i + 1) % len(permutation)]]
    return total_distance


p = [2, 0, 1]
dm = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

print(calculateDistance(p, dm))
