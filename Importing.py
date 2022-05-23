import tsplib95
import networkx as nx
import re


def askUserForFilename():
    file_name = input("Podaj nazwę pliku\n")
    data_matrix = tsplib95.load('Problems/' + file_name)
    distance_matrix = get_distance_matrix(data_matrix)
    # print(distance_matrix)
    return distance_matrix


def getNumbersFromString(string):
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


def get_distance_matrix(problem):

    distance_matrix = []
    for i in list(problem.get_nodes()):
        distance_matrix.append([])
        for j in list(problem.get_nodes()):
            # print(str(i) + "    " + str(j))
            edge = i, j
            distance_matrix[i].append(problem.get_weight(*edge))
    print(distance_matrix)
    return distance_matrix
