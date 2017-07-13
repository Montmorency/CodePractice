def lonely_integer(a):
  while a:
    test = a.pop()
    try:
        a.remove(test)
    except ValueError:
        return test

def lonely_integer(a):
  """
  XOR will evaluate to 0 if two identical numbers are present bit wise 
  in the list, other wise 0000000^number = number.
  """
  lonely_integer = reduce(lambda x, y: x ^ y, a)
  return lonely_integer
