import parse as parse_util

def check_some_problem(g, red_keys, s, t, is_directed, has_no_incoming_edges):
    if not is_directed:
        return undirected_solve(g, red_keys, s, t, is_directed)
    elif is_DAG(g, has_no_incoming_edges):
        graph = augment_graph(g, red_keys, s, t)
        _, pre_nodes = bellman_ford(graph, s)
        
        curr = t
        while curr != None and curr != s:
            curr = pre_nodes[curr]

        return curr is not None
    
    return "?" # NP-Hard

# ------------------ FORD-FULKERSON ------------------ #

SOURCE = "SOURCE-PRIME"
SINK = "SINK-PRIME"

def undirected_solve(g,red_keys,s,t, is_directed):
    graph = build_base_graph(g, s,t)
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
    new_graph = graph.copy()
    for v in graph:
       items = graph[v].items()
       for (adjacentV, _) in items:
           new_graph[v][adjacentV] = 1
       if len(items) > 1:
           #Ensure that it only comes to a vertex once
           temp_node = "tmp-" + v
           new_graph[temp_node] = graph[v].copy()
           new_graph[temp_node][v] = 1
           new_graph[v] = {temp_node: 1}
           for (adjacentV, _) in items:
               del new_graph[adjacentV][v]
               new_graph[adjacentV][temp_node] = 1
    new_graph = parse_util.add_edge_to_graph(new_graph, SOURCE, s, 1)
    new_graph = parse_util.add_edge_to_graph(new_graph, SOURCE, t, 1)
    new_graph = parse_util.add_edge_to_graph(new_graph, s, SOURCE, 0)
    new_graph = parse_util.add_edge_to_graph(new_graph, t, SOURCE, 0)
    return new_graph


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
        print(graph[n2], n1,n2)
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

def is_DAG(g, has_no_incoming_edges):
    """
    Determines whether the given graph is a Directed Acyclic Graph (DAG).
    Inspired by psudo-implementation, found at this url:
    https://stackoverflow.com/questions/4168/graph-serialization/4577#4577

    Returns:
        bool: True if the graph is a DAG, False otherwise.
    """
    graph = g.copy()
    topological_order = []
    vertices_with_no_incoming_edge = has_no_incoming_edges.copy()
    while vertices_with_no_incoming_edge:
        vertex = vertices_with_no_incoming_edge.pop()
        topological_order.append(vertex)
        for key in graph[vertex]:
            graph[vertex][key] = None
            if has_no_incoming_edge(key, graph):
                vertices_with_no_incoming_edge.add(key)
        del graph[vertex]
    if len(graph) > 0:
        return False
    else:
        return True

def has_no_incoming_edge(vertex, graph):
    for key in graph:
        if graph[key][vertex]:
            return False
    return True

def bellman_ford(g, source):
    """
    Runs Bellman-Ford to find some path from s to t.
    Implementation found at this url:
    https://gist.github.com/ngenator/6178728

    Returns:
        bool: True if there exists at least one path from s to t, 
              False otherwise.
    """
    graph = g.copy()

    # Step 1: Prepare the distance and predecessor for each node
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    # Step 2: Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for adj in graph[node]:
                # If the distance between the node and the neighbour is lower than the current, store it
                if distance[adj] > distance[node] + graph[node][adj]:
                    distance[adj], predecessor[adj] = distance[node] + graph[node][adj], node

    # Step 3: Check for negative weight cycles
    for node in graph:
        for adj in graph[node]:
            assert distance[adj] <= distance[node] + graph[node][adj], "Negative weight cycle."
 
    return distance, predecessor
