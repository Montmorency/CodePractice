# Complete the function below.
class ZombieVertex(object):
    def __init__(self, id_,x,y):
        self.id_ = id_
        self.x = x
        self.y = y
        self.value = 0 #value = 1 if zombie 0 otherwise
        self.neighbours = []
        self.discovered = False
        self.parent = None

class ZombieGraph(object):
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.vertices = {}
        for y in range(n):
            for x in range(m):
                self.vertices[y*m+x] = ZombieVertex(y*m+x,x,y)
    
    def build(self, grid):
        """
        Takes list of lists, each list gives column initialization
        then builds connectivity graph
        """
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                self.vertices[y*self.m+x].value = cell
  #build connectivity by appending all valid neighbours  
        for y in range(self.n):
            for x in range(self.m):
                for i in [-1,1]:#add left and write vertex connections
                    if (0 <= x+i < self.m):
                        self.vertices[y*self.m+x].neighbours.append(self.vertices[(y)*self.m+(x+i)])
                for j in [-1,1]:#add up and down vertex connections
                    if (0 <= y+j < self.n):
                        self.vertices[y*self.m+x].neighbours.append(self.vertices[(y+j)*self.m+(x)])
                        
    def dfs_nonrec(self,s):
        #depth first search non recursive. We take a zombie vertex
        #we look at its connections if they are zombies append to
        #the stack of ZombieVertices to search and continue when the connectivity
        #runs out we've searched the whole cluster any nonzero cluster will be a zombie cluster
        s.discovered = True
        region_size = 0
        if s.value == 0:
            return 0
        elif s.value == 1:
            region_size += 1
        vertex_stack = []
        vertex_stack.append(s)
        while vertex_stack:
            search_vertex = vertex_stack.pop()
            for v in search_vertex.neighbours:
                if not v.discovered:
                    v.discovered = True
                    if v.value == 1:
                        region_size += 1
                        vertex_stack.append(v)
                    elif v.value == 0:
                        region_size += 0
        return region_size

    def find_clusters(self):
        clusters = []
        for s in self.vertices.values():
            if not s.discovered:#only search diagonal?
                clusters.append(self.dfs_nonrec(s))#depth first search for each undiscovered cluster
        return clusters                                      

def  zombieCluster(zombies):
    n = len(zombies) #rows of zombie matrix
    m = len(zombies[0]) #columns of zombie matrix 
    z_build_list = []
    for z_string in zombies:
        z_build_list.append(map(int, list(z_string)))
    graph = ZombieGraph(n,m) 
    graph.build(z_build_list)
    clusters = graph.find_clusters()
    clusters = filter(lambda x: x > 0, clusters)
    print clusters
    return len(clusters)


