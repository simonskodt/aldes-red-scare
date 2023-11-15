def check_none_problem(g,red_keys,s,t):
    graph = g.copy()
    graph = remove_red(graph, red_keys)
    path = bfs(graph,s,t)
    if path is None:
        return -1
    else:
        return len(path)

def remove_red(graph, red_keys):
    for key in red_keys:
        graph[key] = {}
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

