import copy
from problems import some
def check_many_problem(g, red_keys, s, t, is_directed, has_no_incoming_edges):
    """
    Check if the given graph is able to be solved.

    Args:
        g (Graph): The input graph.
        red_keys (list): List of red keys.
        s (int): Source node.
        t (int): Target node.

    Returns:
        int: The length of the longest path from source to target if the graph 
            is a DAG, -1 otherwise.
    """
    graph = g.copy()
    if is_directed and some.is_DAG(graph, has_no_incoming_edges):
        graph = copy.deepcopy(g)
        return longest_path(graph, red_keys, s, t)
    return "?" # NP-Hard


def longest_path(g, red_keys, s, t):
    graph = some.augment_graph(g, red_keys, s, t)
    distances, _ = some.bellman_ford(graph, s)
    dist = distances[t]
    if t in red_keys:
        dist -= 1
    return -dist