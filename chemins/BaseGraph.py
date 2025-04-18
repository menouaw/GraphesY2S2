class BaseGraph :
	
	def __init__(self) :
		raise TypeError("Unable to instantiate BaseGraph : must override it.")
	
	def add_vertices(self, iterable) :
		for v in iterable :
			self.add_vertex(v)
	
	def add_edges(self, dictionary) :	
		for k in dictionary :
			if not self.add_edge(*k, dictionary[k]) :
				return False
		return True
	
	def remove_edges(self, iterable) :
		for e in iterable :
			if not self.remove_edge(*e) : return False
		return True
	
	def remove_vertices(self, iterable) :
		for v in iterable :
			if not self.remove_vertex(v) : return False
		return True
	
	def degree(self, v) :
		return len(self.neighbors(v))
	
	def constructor(self) :
		raise TypeError("Unable to instantiate BaseGraph : must override it.")

	def get_subgraph(self, vertices) :
		graph = self.constructor()
		vertices = {v for v in vertices if self.has_vertex(v)}
		graph.add_vertices(vertices)
		graph.add_edges({(a, b) : self.get_transition(a, b) for a, b in self.get_edges() if a in vertices and b in vertices})
		return graph