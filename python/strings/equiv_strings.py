def el_by_el(a,b):
  for i,j in zip(a,b):
    if i != j:
      return False
    else:
      continue
  return True
