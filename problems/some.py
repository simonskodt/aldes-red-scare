import parse as parse_util

def check_some_problem(g, red_keys, s, t, is_directed):
    if not is_directed:
        return undirected_solve(g, red_keys, s, t, is_directed)
    elif is_DAG(g, red_keys, s, t):
        graph = augment_graph(g, red_keys, s, t)
        return bellman_ford(graph)
    
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

def augment_graph(g, red_keys, s, t):
    graph = g.copy()
    red_keys = red_keys.copy()

    for key in red_keys:
        if key in graph:
            for adj in graph[key]:
                graph[key][adj] = 1

    return graph

def is_DAG(g):
    """
    Determines whether the given graph is a Directed Acyclic Graph (DAG).
    Inspired by psudo-implementation, found at this url:
    https://stackoverflow.com/questions/4168/graph-serialization/4577#4577

    Returns:
        bool: True if the graph is a DAG, False otherwise.
    """
    graph = g.copy()
    topological_order = []
    nodes_with_no_incoming_edge = {}
    # graph.

def bellman_ford(graph):
    return 0

