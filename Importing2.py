import tsplib95
import networkx

def get_distance_matrix(name):
    problem = tsplib95.load(name)

    # convert into a networkx.Graph
    graph = problem.get_graph()

    # convert into a numpy distance matrix
    distance_matrix = networkx.to_numpy_matrix(graph)
    print(distance_matrix)
    return distance_matrix