import tsplib95
import networkx as nx
import re


def getNumbersFromString(string):
    # string += '.'
    new_array = []
    next_number = -1
    for c in string:
        if c.isdigit():
            if next_number == -1:
                next_number = 0
            next_number = next_number*10 + int(c)
        else:
            if next_number != -1:
                new_array.append(next_number)
                next_number = -1
    return new_array


def get_distance_matrix(name):
    problem = tsplib95.load(name)

    # convert into a networkx.Graph
    graph = problem.get_graph()
    
    data_matrix = nx.to_numpy_matrix(graph)
    distance_matrix = []
    for line in data_matrix:
        line = str(line)
        distance_line = getNumbersFromString(line)
        distance_matrix.append(distance_line)
    
    return distance_matrix


dm = get_distance_matrix('Tsp_problems/brazil58.tsp')
print(dm)
