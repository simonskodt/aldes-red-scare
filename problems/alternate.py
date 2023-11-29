def check_alternate_problem(graph,red_keys,s,t):
    graph = remove_odd(graph, red_keys, s,t)
    path = bfs(graph,s,t)
    if path is None:
        return False
    else:
        return True
    
def remove_odd(g, red_keys, s,t):
    if s not in g:
        return None
    visited = {s}
    queue = [s]
    new_g = {}
    while queue:
        v = queue.pop(0)
        if v in g:
            is_red = v in red_keys
            for adjacentV, w in g[v].items():
                if (adjacentV in red_keys) != is_red:
                    if v not in new_g:
                        new_g[v] = {}
                    new_g[v][adjacentV] = 0
                    if adjacentV not in visited:
                        visited.add(adjacentV)
                        queue.append(adjacentV)

    return new_g

#Inspired by a previous assignment https://github.com/simonskodt/aldes-flow-behind-enemy-lines/blob/main/flow.py
def bfs(g, start, end):
    if g is None or start not in g or end not in g:
        return None
    queue = [(start, [start])]
    explored = [start]
    while len(queue) > 0:
        (v, path) = queue.pop(0)
        if v == end:
            return path
        if v in g:
            w = g[v]
            for (adjacentV, w) in w.items():
                if adjacentV not in explored:
                    explored.append(adjacentV)
                    queue.append((adjacentV, path + [adjacentV]))
    return None
