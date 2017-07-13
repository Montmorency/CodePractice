def anagram_swaps(string):
    if len(string)%2 != 0:
        return -1    
    N = len(string)
    a = string[:N/2]
    b = string[N/2:]
    list_a = list(a)
    list_b = list(b)
    list_a.sort()
    list_b.sort()
    swaps = 0
    for y in list_b:
        print y
        try:
            list_a.remove(x)
        except ValueError:
            pass
    return len(list_a)


t = 1
#t = int(raw_input())
for i in range(t):
    #string = raw_input()
    string = 'xyzx'
    print anagram_swaps(string)
