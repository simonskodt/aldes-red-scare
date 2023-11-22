import parse as parseUtil

def check_some_problem(g,red_keys,s,t, is_directed):
    if not is_directed:
        return undirected_solve(g, red_keys, s,t, is_directed)
    return "?"
        
def undirected_solve(g,red_keys,s,t, is_directed):
    graph = build_base_graph(g.copy())
    for red_key in red_keys:
        graph = parseUtil.add_edge_to_graph(graph, red_key, "SINK-PRIME", 2)

def build_base_graph(graph, s,t):
    for v in graph:
       for (adjacentV, _) in graph[v].items():
           graph[v][adjacentV] = 1
    graph = parseUtil.add_edge_to_graph(graph, "SOURCE-PRIME", s, 1)
    graph = parseUtil.add_edge_to_graph(graph, "SOURCE-PRIME", s, 1)
    return graph

