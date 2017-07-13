def string_diff(pattern, target):
  """
  Following Skiena's description in ADM chapter on dynamic programming.
  """
  for i = 0 in range(len(pattern)): d_ij[i][0] =  1
  for i = 0 in range(len(target)): d_ij[0][i] =  1
  for i = 1 in range(len(pattern)):
    for j = 1 in range(len(target)):
      d_ij[i,j] = min(d_ij[i-1][j-1]+sub_cost(pattern[i], target[j]), d[i-1][j]+1, d[i][j-1]+1)
  
