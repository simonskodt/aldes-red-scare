def check_alternate_problem(graph,red_keys,s,t):
    graph = remove_odd(graph, red_keys, s,t)
    path = bfs(graph,s,t)
    if path is None:
        return -1
    else:
        return len(path)
    
def remove_odd(g, red_keys, s,t):
    if s not in g:
        return None
    visited = [s]
    queue = [s]
    new_g = {}
    while len(queue) > 0:
        v = queue.pop(0)
        if v in g[v]:
            w = g[v]
            visited.append(v)
            is_red = v in red_keys
            for (adjacentV, w) in w.items():
                if (adjacentV in red_keys) != is_red:
                    if v not in new_g:
                        new_g[v] = {}
                    new_g[v][adjacentV] = 0
                    if adjacentV not in visited:
                        queue.append(adjacentV)
    #print(new_g)
    return new_g

# Based on code from old Kattis exercise: https://github.com/PhilipFlyvholm/kattis/blob/main/Waif/Waif.py#L51
def bfs(g, start, end):
    if g is None or start not in g or end not in g:
        return None
    queue = [(start, [start])]
    explored = [start]
    while len(queue) > 0:
        (v, path) = queue.pop(0)
        if v == end:
            return path
        if v in g[v]:
            w = g[v]
            for (adjacentV, w) in w.items():
                if adjacentV not in explored:
                    explored.append(adjacentV)
                    localPath = path.copy()
                    localPath.append(adjacentV)
                    queue.append((adjacentV, localPath))
    return None
