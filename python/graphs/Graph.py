from collections import deque
class Vertex(object):
    def __init__(self, id_, parent=None):
        self.id_ = id_
        self.neighbours = []
        self.edges = []
        self.discovered = False
        self.completely_explored = False
        self.parent = parent
        self.distance = 0

class Edge(object):
  def __init__(self,x,y,w):
    self.x = x
    self.y = y
    self.weight = w

  def __repr__(self):
    return '({}, {})'.format(x,y)

class Graph(object):
    def __init__(self, N):
        self.vertices = {}
        self.distances = []
        self.edge_weight = 6
        self.distances = {}
        for i in range(N):
            self.vertices[i] = Vertex(i)

    def shortestpath(self, s, t):
      """
      Djikstra's algorithm
      """
      known = self.vertices[s]
      dist = {}
      for i = 1 to n: 
        dist[i] = float('Inf')
      for edge in s.edges:
        dist[edge.y] = edge.weight
      last = s 
      while last.id_ != t.id_:
        min_weight = min([edge.weight for edge in last.edges])
        edge = filter(min_weight, s.edges)
        v_next = self.vertices[edge[0].y]
        for edge in vnext.edges:
          dist[edge.y] = min(dist[edge.y], dist[v_next.id_] + edge.weight)
        last = v_next
      return dist[t]

    def connect(self, x, y):
        self.vertices[x].neighbours.append(self.vertices[y])
        self.vertices[y].neighbours.append(self.vertices[x])

    def bfs(self, s):
      #breadth first search starting at node s.
        vertices_to_find = [v for v in self.vertices.keys()]
        vertices_to_find.remove(s)
        for v in vertices_to_find:
            self.distances[v] = 0
        for vertex in self.vertices[s].neighbours: #no self directed edges
            vertex.discovered = False
            vertex.parent = self.vertices[s]
#Initialize the root search node:
        self.vertices[s].parent = None
        self.vertices[s].discovered = True
#set up FIFO queue
        vertices_to_search = deque()
        vertices_to_search.append(self.vertices[s])
        while vertices_to_search:
            root = vertices_to_search.popleft()
            #INSERT VERTED PROCESSING CODE HERE IF REQUIRED:
            #
            for search_vertex in root.neighbours:
                #PROCESS EDGE (root.id_, search_vertex.id_) IF REQUIRED
                if not search_vertex.discovered:
                    search_vertex.discovered = True
                    search_vertex.parent = self.vertices[root.id_]
                    vertices_to_search.append(search_vertex)
                    search_vertex.distance = self.vertices[search_vertex.parent.id_].distance 
                    self.distances[search_vertex.id_] = self.vertices[search_vertex.parent.id_].distance 

    def print_distances(self):
        distances = []
        for k,v in self.distances.items():
            distances.append((k,v))
        p_dist = []
        for v_d in sorted(distances, key=lambda x:x[0]):
            if v_d[1] == 0:
                distance = -1
            else:
                distance = v_d[1]
            p_dist.append(distance)
        print ' '.join(map(str, p_dist))

