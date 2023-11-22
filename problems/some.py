import parse as parse_util

def check_some_problem(g, red_keys, s, t, is_directed):
    if not is_directed:
        return undirected_solve(g, red_keys, s, t, is_directed)
    elif is_DAG():
        return bellman_ford()
    
    return "?" # NP-Hard

# ------------------ FORD-FULKERSON ------------------ #

def undirected_solve(g,red_keys,s,t, is_directed):
    graph = build_base_graph(g.copy())
    for red_key in red_keys:
        graph = parse_util.add_edge_to_graph(graph, red_key, "SINK-PRIME", 2)

def build_base_graph(graph, s,t):
    for v in graph:
       for (adjacentV, _) in graph[v].items():
           graph[v][adjacentV] = 1
    graph = parse_util.add_edge_to_graph(graph, "SOURCE-PRIME", s, 1)
    graph = parse_util.add_edge_to_graph(graph, "SOURCE-PRIME", s, 1)
    return graph

# ------------------ BELLMAN-FORD ------------------ #

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
    raise NotImplementedError("longest patimport parse as parseUtil

