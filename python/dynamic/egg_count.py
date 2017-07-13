import numpy as np

def build_egg_matrix(m_ij, eggs, floors):
  for floor in range(1, floors+1):
    m_ij[1][floor] = floor
  for egg in range(2, eggs+1):
    for floor in range(1, floors+1):
      if egg > floor:
        m_ij[egg][floor] = m_ij[egg-1][floor]
      else:
        m_ij[egg][floor] = 1 + min([max(m_ij[egg-1][k-1], m_ij[egg][floor-k]) for k in range(1,floor)])

eggs = 2
floors = 100
m_ij = np.zeros([eggs+1, floors+1])
print m_ij
build_egg_matrix(m_ij, eggs,floors)
print m_ij
print m_ij[2][100]
