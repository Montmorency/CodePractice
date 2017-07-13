#Need to find the roots of the characteristic equation?
def recurrence(coeffs, f_ks,K)
  for c, f_k in zip(coeffs, f_ks):
    f_k[K] += c*f_k
  f_k = f_k%(10e9+7)
  return f_k
