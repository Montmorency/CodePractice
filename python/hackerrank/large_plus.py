import os
import sys


# Find two 'plus signs' of 'G' characters in a grid 
# such that the multiple of the two areas is a maximum
# 5 6
#GGGGGG
#GBBBGB
#GGGGGG
#GGBBGB
#GGGGGG
# Max area is 5.
class Cell(object):
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.visited = False
        self.right = None
        self.left = None
        self.top = None
        self.bottom = None

class Graph(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = {}

def find_plus(start_cell, limit=float('Inf')):
    if start_cell == 'B':
        return 0
    area = 1
    start_cell.visited = True
    top = start_cell.top
    bottom = start_cell.bottom
    right = start_cell.right
    left = start_cell.left
    if all(map(bool, [top, bottom, left, right])):
        not_visited = all([not top.visited, not bottom.visited, not right.visited, not left.visited])
        all_good = all(map(lambda x : x.value =='G', [top,bottom,left,right]))
    while top and bottom and left and right and not_visited and all_good and area < limit:
        area += 4
        top.visited, bottom.visited, left.visited, right.visited = True, True, True, True
        top = top.top
        bottom = bottom.bottom
        right = right.right
        left = left.left
        if all(map(bool,[top,bottom,left,right])):
            not_visited = all([not top.visited, not bottom.visited, not right.visited, not left.visited])
            all_good = all(map(lambda x : x.value =='G', [top,bottom,left,right]))
    return area

def find_two_pluses(graph):
  #should find maximum of the grid.
    final_area = 0
    cells = graph.cells.values()
    final_area_plus_1 = 0
    large_cells = []
    large_areas=[]
    for cell in cells:
        for s_cell in cells:
            s_cell.visited = False
        area_plus_1 = find_plus(cell)        
        print cell.row, cell.col, area_plus_1
        large_areas.append(area_plus_1)
        large_cells.append(cell)
    final_area_plus_2 = 0
    for cell in cells:
        for l_cell, l_area in zip(large_cells, large_areas):
            sub_plus = l_area
            while sub_plus >= 0:#this loop allows us to consider what would maximize the area by taking a smaller plus
              for s_cell in cells:
                s_cell.visited = False
              print 'sp', sub_plus
              find_plus(l_cell, limit=sub_plus)
              area_plus_2 = find_plus(cell)
              final_area_plus_2 = area_plus_2
              print 'fa', final_area_plus_2
              final_area_tmp = sub_plus*final_area_plus_2
              if final_area_tmp > final_area:
                final_area = final_area_tmp
              sub_plus -= 4
    return final_area

m, n = map(int, raw_input().split(' '))
grid_array = []
graph = Graph(m,n)
for _ in range(m):
    grid_array.append(list(raw_input()))

for row in range(m):
    r = grid_array[row]
    for col in range(n):
        graph.cells[row*n+col] = Cell(row, col, r[col])

#set grid neighoburs
for row in range(m):
    for col in range(n):
        r_index = (row, col+1)
        if r_index[1] < n:
            graph.cells[row*n + col].right = graph.cells[r_index[0]*n + r_index[1]]
        l_index = (row, col-1)
        if l_index[1] >= 0:
            graph.cells[row*n + col].left = graph.cells[l_index[0]*n + l_index[1]]
        t_index = (row+1, col)
        if t_index[0] < m:
            graph.cells[row*n + col].top = graph.cells[t_index[0]*n + t_index[1]]
        b_index = (row-1, col)
        if b_index[0] >= 0:
            graph.cells[row*n + col].bottom = graph.cells[b_index[0]*n + b_index[1]]

print find_two_pluses(graph)



