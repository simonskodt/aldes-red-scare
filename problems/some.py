import parse as parse_util

def check_some_problem(g, red_keys, s, t, is_directed, has_no_incoming_edges):
    if not is_directed:
        return undirected_solve(g, red_keys, s, t, is_directed)
    elif is_DAG(g, has_no_incoming_edges):
        graph = augment_graph(g, red_keys, s, t)
        # return bellman_ford(graph)
    
    return "?" # NP-Hard

# ------------------ FORD-FULKERSON ------------------ #

SOURCE = "SOURCE-PRIME"
SINK = "SINK-PRIME"

def undirected_solve(g,red_keys,s,t, is_directed):
    graph = build_base_graph(g.copy(), s,t)
    for red_key in red_keys:
        graph = parse_util.add_edge_to_graph(graph.copy(), red_key, SINK, 2)
        graph = parse_util.add_edge_to_graph(graph.copy(), SINK, red_key, 0)
        total_flow = 0
        path, flow = bfs(graph)
        
        while path:
            total_flow += flow
            augment(path, flow, graph)
            path, flow = bfs(graph)

        if(total_flow == 2):
            return True
    return False

def build_base_graph(graph, s,t):
    for v in graph:
       for (adjacentV, _) in graph[v].items():
           graph[v][adjacentV] = 1
    graph = parse_util.add_edge_to_graph(graph, SOURCE, s, 1)
    graph = parse_util.add_edge_to_graph(graph, SOURCE, t, 1)
    graph = parse_util.add_edge_to_graph(graph, s, SOURCE, 0)
    graph = parse_util.add_edge_to_graph(graph, t, SOURCE, 0)
    return graph


#Taken from previous assignment https://github.com/simonskodt/aldes-flow-behind-enemy-lines/blob/main/flow.py
def bfs(graph):
    """
    Perform a breadth-first search on a graph to find the shortest path from 
    SOURCE to SINK. If min_cut is True, return the minimum cut of the graph 
    instead.
    
    Args:
        graph: a Graph object representing the graph to search
        min_cut: a boolean indicating whether to return the minimum cut of the 
                 graph
    
    Returns:
        if min_cut is False: a tuple containing the shortest path from SOURCE 
            to SINK and its flow
        if min_cut is True: a tuple containing the visited nodes and the 
            endpoints of the minimum cut
    """
    queue = [(SOURCE, [SOURCE], float("inf"))]
    visited, endpoints = [SOURCE], []
    
    while queue:
        node, path, cur_flow = queue.pop(0)
        adj_nodes = graph[node]
        for adj_node, capacity in adj_nodes.items():
            if adj_node not in visited and capacity > 0:
                flow = min(capacity, cur_flow)
                queue.append((adj_node, path + [adj_node], flow))
                visited.append(adj_node)

                if adj_node == SINK:
                    return path + [SINK], flow
            elif capacity == 0 and adj_node not in visited:
                original_capacity = graph[adj_node][node]
                endpoints.append((node, adj_node, original_capacity//2))
    
    return ([], 0)

def augment(path, flow, graph):
    """
    Augments the flow along a given path in a graph.

    Args:
        path (list): A list of nodes representing the path.
        flow (int): The amount of flow to augment.
        graph (Graph): The graph object.

    Returns:
        None
    """
    for i in range(len(path)-1):
        n1, n2 = path[i], path[i+1]
        forward_edge_new_cap  = graph[n1][n2] - flow
        backward_edge_new_cap = graph[n2][n1] + flow
        graph = parse_util.add_edge_to_graph(graph, n1, n2, forward_edge_new_cap)
        graph = parse_util.add_edge_to_graph(graph, n2, n1, backward_edge_new_cap)

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

def is_DAG(g, has_no_incoming_edge):
    """
    Determines whether the given graph is a Directed Acyclic Graph (DAG).
    Inspired by psudo-implementation, found at this url:
    https://stackoverflow.com/questions/4168/graph-serialization/4577#4577

    Returns:
        bool: True if the graph is a DAG, False otherwise.
    """
    graph = g.copy()
    topological_order = []
    vertecis_with_no_incoming_edge = has_no_incoming_edge.copy()
    while vertecis_with_no_incoming_edge:
        vertex = vertecis_with_no_incoming_edge.pop()
        topological_order.append(vertex)
        for key in graph[vertex]:
            return 0
def has_incoming_edge(vertex, graph):
    for key in graph:
        if graph[key][vertex] is None:
            # no incoming
def bellman_ford(graph):
    return 0

