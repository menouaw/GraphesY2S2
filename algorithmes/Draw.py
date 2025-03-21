import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from AllGraphs import *

def draw_graph(graph, colors = "cyan") :
	g = nx.DiGraph()
	g.add_nodes_from(graph.get_vertices())
	for k in graph.get_edges() :
		g.add_edge(*k, weight = graph.get_transition(*k))
	pos = nx.circular_layout(g)
	nx.draw_networkx_nodes(g, pos, node_color = colors)
	nx.draw_networkx_edges(g, pos, connectionstyle="arc3,rad=0.2")
	edge_labels = nx.get_edge_attributes(g, "weight")
	nx.draw_networkx_labels(g, pos)
	nx.draw_networkx_edge_labels(g, pos, edge_labels)
	plt.show()