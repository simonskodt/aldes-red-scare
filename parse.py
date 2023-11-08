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
    return files

def add_edge_to_graph(g, f, t):
    if f not in g:
        g[f] = {}
    g[f][t] = 0
    return g

def parse_graph(lines):
    graph = {}
    red_keys = []

    # n: number of vertices
    # m: number of edges
    # r: cardinaly of R
    n, m, r = map(int, lines[0].split())

    # s: start vertex, t: end vertex
    s, t = lines[1].split()

    for i in range(n):
        vertex = lines[i+2]
        name = re.search("[_a-z0-9]+", vertex).string
        
        # if vertex is red, insert in red keys
        if "*" in name:
            red_keys.append(name)
        
    for i in range(m):
        edge = lines[i+n+2]
        # Do not touch
        undirected_regex = r"(?P<from>[_a-z0-9])+\s\-\-\s(?P<to>[_a-z0-9]+)"
        directed_regex = r"(?P<from>[_a-z0-9])+\s\-\>\s(?P<to>[_a-z0-9]+)"
        undirected_search = re.search(undirected_regex, edge)
        directed_search = re.search(directed_regex, edge)
        if undirected_search is not None:
            from_v = undirected_search.group("from")
            to_v = undirected_search.group("to")
            graph = add_edge_to_graph(graph, from_v, to_v)
            graph = add_edge_to_graph(graph, to_v, from_v)
        elif directed_search is not None:
            from_v = undirected_search.group("from")
            to_v = undirected_search.group("to")
            graph = add_edge_to_graph(graph, from_v, to_v)
        else:
            print("Unknown edge", edge)
    return graph, red_keys, s, t