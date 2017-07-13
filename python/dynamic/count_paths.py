class Graph(object):
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.vertices = {}

  def build_graph(self,grid):
    pass

  def grid_index(self, row, col):
    return col*self.rows + row

  def valid_square(self, row, col):
    if self.vertices[col*self.rows + row] != 'X':
      return True
    else
      return False

def countPaths(graph, row, col, paths, target):
  if (!graph.validSquare(row,col)): return 0
  if isatend(row, col, target): return 1
  if paths[row][col] == 0:
    paths[row][col] = countPaths(graph, row+1,col) + countPaths(grid, row, col+1);
  return paths[row][col]
