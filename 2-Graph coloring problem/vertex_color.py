import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

colors = {0:"red", 1:"green", 2:"blue"}

G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2), (1,3), (2,4), (3,5), (4,5)])

d = nx.coloring.greedy_color(G, strategy = "largest_first")
node_colors = []
for i in sorted (d.keys()):
    node_colors.append(colors[d[i]])

nx.draw(G, node_color = node_colors, with_labels = True, width = 5)

plt.show()