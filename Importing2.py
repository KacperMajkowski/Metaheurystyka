import tsplib95
import networkx


def get_distance_matrix(name):
    problem = tsplib95.load(name)

    # convert into a networkx.Graph
    graph = problem.get_graph()

    # convert into a numpy distance matrix
    distance_matrix = networkx.to_numpy_matrix(graph)
    return distance_matrix


print(get_distance_matrix('Tsp_problems/berlin52.tsp'))
