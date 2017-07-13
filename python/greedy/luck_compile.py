# Enter your code here. Read input from STDIN. Print output to STDOUT
N, K = map(int, raw_input().split(' '))
important = []
unimportant = []
for _ in range(N):
    l, t = map(int, raw_input().split(' '))
    if t == 1:
        important.append(int(l))
    else:
        unimportant.append(int(l))        
important.sort()
start = len(important)-K
end = len(important)-K
if K <= len(important):
    print sum(important[start:]) + sum(unimportant) - sum(important[:end])
else:
    print sum(unimportant) + sum(important)
