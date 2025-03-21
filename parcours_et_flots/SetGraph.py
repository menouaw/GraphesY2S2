from BaseGraph import BaseGraph

class SetGraph (BaseGraph) :
	
	def __init__(self) :
		self.vertices = set()
		self.edges = dict()
		
	def constructor(self) :
		return SetGraph()
	
	def add_edge(self, u, v, transition = 1) :
		if u not in self.vertices : return False
		if v not in self.vertices : return False
		self.edges[(u, v)] = transition
		return True
	
	def add_vertex(self, v) :
		self.vertices.add(v)
	
	def get_transition(self, u, v) :
		if (u, v) not in self.edges : return None
		return self.edges[(u, v)]
	
	def get_edges(self) :
		return self.edges
	
	def get_vertices(self) :
		return self.vertices
	
	def has_vertex(self, v) :
		return v in self.vertices
	
	def has_edge(self, u, v) :
		return (u, v) in self.edges
	
	def remove_edge(self, u, v) :
		if (u, v) not in self.edges : return False
		self.edges.pop((u, v))
		return True
	
	def remove_vertex(self, v) :
		if v not in self.vertices : return False
		self.remove_edges([(a, b) for a, b in self.edges if a == v or b == v])
		self.vertices.remove(v)
		return True
	
	def neighbors(self, v) :
		return {b for a, b in self.edges if a == v}
	
	def transpose(self) :
		graph = SetGraph()
		graph.add_vertices(self.get_vertices())
		graph.add_edges({(v, u) : self.get_transition(u, v) for (u, v) in self.get_edges()})
		return graph
