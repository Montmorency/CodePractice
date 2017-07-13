# Enter your code here. Read input from STDIN. Print output to STDOUT
def min_ops(target, number):
    a = (number-target)/5
    b = ((number-target) - a*5)/2
    c = ((number-target)-a*5-b*2)/1
    return a+b+c

t = int(raw_input())
for _ in range(t):
    N = int(raw_input())
    cupcakes = map(int, raw_input().split(' '))
    cupcakes.sort()
    target = cupcakes[0]
    ops = []
    for i in range(5):
        ops.append(sum([min_ops(target-i, c) for c in cupcakes]))
    print min(ops)
