def greedy_match(pattern, string):
  """
  Returns match in string. 
  """
  for k in range(len(string)):
    shift_string = string[k:]+string[:k]
    substring = shift_string[:len(pattern)]
    for p, s in zip(pattern, substring):
      if p == s:
        matched = True
      else:
        matched = False
        break
    if matched: return matched, k
  return False, -1


if __name__=='__main__':
  p, s = raw_input().split(' ')
  print greedy_match(p, s)  
