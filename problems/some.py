def check_many_problem(g, red_keys, s, t):
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
    if (is_DAG):
        return longest_path(graph)
    
    return -1 # NP-Hard


def is_DAG():
    """
    Determines whether the given graph is a Directed Acyclic Graph (DAG).
    Inspired by psudo-implementation, found at this url:
    https://stackoverflow.com/questions/4168/graph-serialization/4577#4577

    Returns:
        bool: True if the graph is a DAG, False otherwise.
    """
    raise NotImplementedError("longest path")

def longest_path(g, ):
    raise NotImplementedError("longest path")