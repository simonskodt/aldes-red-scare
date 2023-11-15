from queue import PriorityQueue 

def check_few_problem(g,red_keys,s,t):
    graph = g.copy()
    # update weights in graph. Outgoing edges from red vertices must be 1
    for key in red_keys:
        if key in graph:
            for adj in graph[key]:
                graph[key][adj] = 1

    # run dijkstra
    dist = dijkstra(graph, s, t)
    if t not in dist or dist[t] == float("inf"):
        return -1
    else:
        return dist[t]

def dijkstra(graph, s, t):
    # initialize distance to all vertices to infinity
    dist = {}
    visited = []

    for v in graph:
        dist[v] = float("inf")
    dist[s] = 0

    # initialize priority queue
    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        (d, v) = pq.get()
        if d > dist[v]:
            continue
        if v in graph:
            for (adj, w) in graph[v].items():
                if adj not in visited and adj in graph and dist[v] + w < dist[adj]:
                    visited.append(adj)
                    dist[adj] = dist[v] + w
                    pq.put((dist[adj], adj))
    return dist