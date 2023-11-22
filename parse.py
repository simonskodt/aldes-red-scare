import sys, os, re

def parse_file(file_name):
  # Open file in data/file_name
    if ".txt" not in file_name:
        file_name += ".txt"

    with open(f"data/{file_name}", 'r') as file:
        lines = file.readlines()
        return parse_graph(lines)

def find_files(prefix_file_name):

    files = [file for file in os.listdir("data/") if file.startswith(prefix_file_name)]
    if len(files) == 0:
        return None
    else:
        return files
    
def find_all_files():
    files = [file for file in os.listdir("data/") if file.endswith(".txt")]
    sorted_files = sorted(files)
    return sorted_files

def add_edge_to_graph(g, f, t, w=0):
    if f not in g:
        g[f] = {}
    g[f][t] = w
    return g

def parse_graph(lines):
    graph = {}
    red_keys = []
    is_directed = False
    has_incoming_edges = set()

    # n: number of vertices
    # m: number of edges
    # r: cardinaly of R
    n, m, r = map(int, lines[0].split())

    # s: start vertex, t: end vertex
    s, t = map(str, lines[1].split())

    for i in range(n):
        vertex = lines[i+2]
        (regFrom, regTo) = re.search("[_a-z0-9]+", vertex).span()
        name = vertex[regFrom:regTo]
        # if vertex is red, insert in red keys
        if "*" in vertex:
            red_keys.append(name)
        
    for i in range(m):
        edge = lines[i+n+2]
        # Do not touch
        undirected_regex = r"(?P<from>[_a-z0-9]+)\s\-\-\s(?P<to>[_a-z0-9]+)"
        directed_regex = r"(?P<from>[_a-z0-9]+)\s\-\>\s(?P<to>[_a-z0-9]+)"
        undirected_search = re.search(undirected_regex, edge)
        directed_search = re.search(directed_regex, edge)
        if undirected_search is not None:
            from_v = str(undirected_search.group("from"))
            to_v = str(undirected_search.group("to"))
            graph = add_edge_to_graph(graph, from_v, to_v)
            graph = add_edge_to_graph(graph, to_v, from_v)
        elif directed_search is not None:
            is_directed = True
            from_v = str(directed_search.group("from"))
            to_v = str(directed_search.group("to"))
            has_incoming_edges:set.add(to_v) 
            graph = add_edge_to_graph(graph, from_v, to_v)
        else:
            print("Unknown edge", edge)
    has_no_incoming_edges = has_incoming_edges.difference(set(graph.keys))
    return graph, red_keys, s, t, is_directed, has_no_incoming_edges