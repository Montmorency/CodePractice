from collections import deque

class Vertex(object):
    def __init__(self, id_, parent=None):
        self.id_ = id_
        self.neighbours = []
        self.discovered = False
        self.parent = parent
        self.distance = 0

class Graph(object):
    def __init__(self, N):
        self.vertices = {}
        self.distances = []
        self.edge_weight = 6
        self.distances = {}
        for i in range(N):
            self.vertices[i] = Vertex(i)

    def connect(self, x, y):
        self.vertices[x].neighbours.append(self.vertices[y])
        self.vertices[y].neighbours.append(self.vertices[x])

    def find_all_distances(self, s):
        #initialize search queue:
        vertices_to_find = [v for v in self.vertices.keys()]
        vertices_to_find.remove(s)
        for v in vertices_to_find:
            self.distances[v] = 0
        for vertex in self.vertices[s].neighbours: #no self directed edges
            vertex.discovered = False
            vertex.parent = self.vertices[s]
        self.vertices[s].discovered = True
        vertices_to_search = deque()
        vertices_to_search.append(self.vertices[s])
        while vertices_to_search:
            root = vertices_to_search.popleft()
            for search_vertex in root.neighbours:
                if not search_vertex.discovered:
                    search_vertex.discovered = True
                    search_vertex.parent = self.vertices[root.id_]
                    vertices_to_search.append(search_vertex)
                    search_vertex.distance = self.vertices[search_vertex.parent.id_].distance + 6
                    self.distances[search_vertex.id_] = self.vertices[search_vertex.parent.id_].distance + 6
        self.print_distances()

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

with open('input.txt','r') as f:
  raw_lines = f.read().split('\n')

t = int(raw_lines[0])
for i in range(t):
    n,m = map(int, raw_lines[1].split(' '))
    print n,m
    graph = Graph(n)
    for i in xrange(m):
        for line in raw_lines[2:-2]:
          x,y = [int(x) for x in line.split()]
          graph.connect(x-1,y-1) 
    s = int(raw_lines[-2])
    graph.find_all_distances(s-1)
    
