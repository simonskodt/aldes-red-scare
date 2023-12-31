def check_none_problem(g, red_keys, s, t):
    graph = g.copy()
    graph = remove_red(graph, red_keys)
    path = bfs(graph,s,t)
    if path is None:
        return -1
    else:
        return len(path)-1

def remove_red(graph, red_keys):
    for key in red_keys:
        graph[key] = {}
    return graph

# Based on code from old Kattis exercise: https://github.com/PhilipFlyvholm/kattis/blob/main/Waif/Waif.py#L51
def bfs(g, start, end):
    if start not in g or end not in g:
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
                    localPath = path.copy()
                    localPath.append(adjacentV)
                    queue.append((adjacentV, localPath))
    return None

