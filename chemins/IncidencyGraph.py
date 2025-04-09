from BaseGraph import BaseGraph

class IncidencyGraph (BaseGraph) :
	
	def __init__(self) :
		self.vertices = dict()
		
	def constructor(self) :
		return IncidencyGraph()
	
	def add_vertex(self, v) :
		self.vertices[v] = dict()
	
	def add_edge(self, u, v, transition = 1) :
		if u not in self.vertices : return False
		if v not in self.vertices : return False
		self.vertices[u][v] = transition
		return True
	
	def get_transition(self, u, v) :
		if u not in self.vertices : return None
		if v not in self.vertices[u] : return None
		return self.vertices[u][v]
	
	def get_edges(self) :
		return {(u, v) for u in self.vertices for v in self.vertices[u]}
	
	def get_vertices(self) :
		return self.vertices
	
	def has_vertex(self, v) :
		return v in self.vertices
	
	def has_edge(self, u, v) :
		return u in self.vertices and v in self.vertices[u]
	
	def remove_edge(self, u, v) :
		if not self.has_edge(u, v) : return False
		self.vertices[u].pop(v)
		return True
	
	def remove_vertex(self, v) :
		if not self.has_vertex(v) : return False
		for u in self.vertices :
			if v in self.vertices[u] :
				self.vertices[u].pop(v)
		self.vertices.pop(v)
		return True
	
	def neighbors(self, v) :
		return set(self.vertices[v].keys())
	
	def degree(self, v) :
		return len(self.vertices[v])
	
	def transpose(self) :
		graph = IncidencyGraph()
		graph.add_vertices(self.get_vertices())
		graph.add_edges({(v, u) : self.vertices[u][v] for u in self.vertices for v in self.vertices[u]})
		return graph