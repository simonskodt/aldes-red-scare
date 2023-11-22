import parse as parse_util

def check_some_problem(g, red_keys, s, t, is_directed, has_no_incoming_edges):
    if not is_directed:
        return undirected_solve(g, red_keys, s, t, is_directed)
    elif is_DAG(g, has_no_incoming_edges):
        graph = augment_graph(g, red_keys, s, t)
        return bellman_ford(graph)
    
    return "?" # NP-Hard

# ------------------ FORD-FULKERSON ------------------ #

def undirected_solve(g, red_keys, s, t, is_directed):
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

    # Nodes have a default weight of 0, so we only need to change the weights
    # of the red vertices.
    for key in red_keys:
        if key in graph:
            for adj in graph[key]:
                # set outgoing edges from red vertices to -1
                graph[key][adj] = -1
            
    return graph

def is_DAG(g, has_incoming_edge):
    """
    Determines whether the given graph is a Directed Acyclic Graph (DAG).
    Inspired by psudo-implementation, found at this url:
    https://stackoverflow.com/questions/4168/graph-serialization/4577#4577

    Returns:
        bool: True if the graph is a DAG, False otherwise.
    """
    graph = g.copy()
    topological_order = []
    nodes_with_no_incoming_edge = has_incoming_edge.copy()
    # while nodes_with_no_incoming_edge:
        # nodes_with_no_incoming_edge:dict.pop
    

def bellman_ford(graph):
    return 0

