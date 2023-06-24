# Graph class to represent a graph
class Graph:
  def __init__(self):
    self.graph = {}

  def add_edge(self, vertex, edge):
    if (vertex in self.graph):
      print("1")
      self.graph[vertex].append(edge)
    else:
      print("2")
      self.graph[vertex] = [edge]
# Create a graph
graph = Graph()

# Add edges to the graph
graph.add_edge(0, 1)

