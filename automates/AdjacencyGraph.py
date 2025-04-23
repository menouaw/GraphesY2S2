from BaseGraph import BaseGraph

class AdjacencyGraph(BaseGraph) :
	
	def __init__(self) :
		self.vertices = list()
		self.verticesSet = set()
		self.matrix = None
		
	def constructor(self) :
		return AdjacencyGraph()
	
	def add_vertex(self, v) :
		self.vertices.append(v)
		self.verticesSet.add(v)
		if self.matrix == None :
			self.matrix = [[None]]
		else :
			n = len(self.vertices) - 1
			self.matrix = [[self.matrix[i][j] if i < n and j < n else None for j in range(n + 1)] for i in range(n + 1)]
	
	def add_edge(self, u, v, transition = 1) :
		if u not in self.verticesSet : return False
		if v not in self.verticesSet : return False
		self.matrix[self.vertices.index(u)][self.vertices.index(v)] = transition
		return True
	
	def get_transition(self, u, v) :
		if u not in self.verticesSet : return None
		if v not in self.verticesSet : return None
		return self.matrix[self.vertices.index(u)][self.vertices.index(v)]
	
	def get_edges(self) :
		return {(self.vertices[i], self.vertices[j]):self.matrix[i][j] for i in range(len(self.vertices)) for j in range(len(self.vertices)) if self.matrix[i][j] != None}
	
	def get_vertices(self) :
		return self.verticesSet
	
	def has_vertex(self, v) :
		return v in self.verticesSet
	
	def has_edge(self, u, v) :
		if u not in self.verticesSet : return None
		if v not in self.verticesSet : return None
		return self.matrix[self.vertices.index(u)][self.vertices.index(v)] != None
	
	def remove_edge(self, u, v) :
		if not self.has_edge(u, v) : return False
		self.matrix[self.vertices.index(u)][self.vertices.index(v)] = None
		return True
	
	def remove_vertex(self, v) :
		if v not in self.verticesSet : return False
		pos = self.vertices.index(v)
		self.matrix = [[self.matrix[i][j] for j in range(len(self.vertices)) if j != pos] for i in range(len(self.vertices)) if i != pos]
		self.vertices.pop(pos)
		self.verticesSet.remove(v)
		return True
	
	def neighbors(self, v) :
		pos = self.vertices.index(v)
		return {self.vertices[i] for i in range(len(self.vertices)) if self.matrix[pos][i] != None}
	
	def transpose(self) :
		graph = AdjacencyGraph()
		graph.vertices = [e for e in self.vertices]
		graph.verticesSet = {e for e in self.verticesSet}
		graph.matrix = [[self.matrix[j][i] for j in range(len(self.get_vertices()))] for i in range(len(self.get_vertices()))]
		return graph