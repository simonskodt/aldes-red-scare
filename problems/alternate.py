def check_none_problem(graph,red_keys,s,t):
    graph = remove_odd(graph, red_keys, s,t)
    path = bfs(graph,s,t)
    if path is None:
        return -1
    else:
        return len(path)
    
def remove_odd(graph, red_keys, s,t):
    visited = [s]
    queue = [s]
    while len(queue) > 0:
        v = queue.pop(0)
        w = g[v]
        is_red = v in red_keys
        for (adjacentV, w) in w.items():
            if adjacentV in red_keys == is_red:
                del graph[adjacentV]
                del graph[v][adjacentV]
            elif adjacentV not in visited:
                queue.append(adjacentV)



    return graph

# Based on code from old Kattis exercise: https://github.com/PhilipFlyvholm/kattis/blob/main/Waif/Waif.py#L51
def bfs(g, start, end):
    queue = [(start, [start])]
    explored = [start]
    while len(queue) > 0:
        (v, path) = queue.pop(0)
        if v == end:
            return path
        w = g[v]
        for (adjacentV, w) in w.items():
            if adjacentV not in explored:
                explored.append(adjacentV)
                localPath = path.copy()
                localPath.append(adjacentV)
                queue.append((adjacentV, localPath))
    return None
