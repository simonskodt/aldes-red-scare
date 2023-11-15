# First networkx library is imported  
# along with matplotlib 
import networkx as nx 
import matplotlib.pyplot as plt 

def get_graph_type(directed):
    if directed:
        return nx.DiGraph()
    else:
        return nx.Graph()
  
# Driver code
def visualize(graph, red_keys, s, t, directed=False):
    G = get_graph_type(directed)
    labels = {}

    for key in red_keys:
        G.add_node(key, color="red")

    for key in graph:
        labels[key] = key
        if key not in red_keys:
            G.add_node(key, color="blue")

        for adj in graph[key]:
            if key in red_keys:
                G.add_edge(key, adj)
            else:
                G.add_edge(key, adj)
        
    labels[s] = "s:" + s
    labels[t] = "t:" + t

    nx.draw(G, labels=labels, node_color=nx.get_node_attributes(G, 'color').values())
    plt.show()
