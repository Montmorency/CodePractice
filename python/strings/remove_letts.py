def number_needed(a, b):
  a_list=sorted(a)
  b_list=sorted(b)
  a_n = 0
  b_n = 0
  for lett in a:
    if lett in b_list:
      b_list.remove(lett)
    else:
      a_list.remove(lett)
      a_n += 1
  b_list=sorted(b)
  for lett in b:
    if lett in a_list:
      a_list.remove(lett)
    else:
      b_list.remove(lett)
      b_n += 1
  return a_n + b_n


a='cde'
b='abc'
a = raw_input().strip()
b = raw_input().strip()
print number_needed(a,b)

