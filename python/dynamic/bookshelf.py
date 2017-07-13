import numpy as np


def partition(seq, K, N):
  """
  From Skiena's ADM chapter on dynamic programming for 
  partitioning an ordered array.
  Starting indices in numpy arrays from 1 for simplicity.
  """
  m_ij = np.zeros([N+1, K+1])
  d_ij = np.zeros([N+1, K+1])
#initialize for a sequen of length 1 it does not matter how many
#partitions we have we always have the min cost of s_1:
#prefix sums:
  prefix_sum = np.zeros([N+1])
  prefix_sum[0] = 0
  for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + seq[i-1]

  for n in range(1,N+1): m_ij[n][1] = prefix_sum[n]
  for j in range(1,K+1): m_ij[1][j] = seq[0]

  for i in range(2, N+1):
    for j in range(2, K+1):
      m_ij[i][j] = float('Inf')
      for x in range(1, (i-1+1)):
        s = max(m_ij[x][j-1], prefix_sum[i]-prefix_sum[x])
        if m_ij[i][j] > s:
          m_ij[i][j] = s
          d_ij[i][j] = x
  return m_ij, d_ij

def get_partitions(seq, d_ij, N,K):
  if K == 1:
    print seq[:int(N)]
  else:
    print 'labels', d_ij[N][K]
    get_partitions(seq, d_ij, d_ij[N][K], K-1)
    print seq[int(d_ij[N][K]):int(N)]

if __name__=='__main__':
  books = [100,200,300,400,500,600,700,800,900]
  K = 3
  key_dict = {}
  m_ij, d_ij = partition(books, K, len(books))
  print m_ij
  print d_ij
  get_partitions(books, d_ij, len(books), K)
  books = [1,1,1,1,1,1,1,1,1]
  m_ij, d_ij = partition(books, K, len(books))
  print m_ij
  print d_ij
  get_partitions(books, d_ij, len(books), K)
