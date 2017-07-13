# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
a = map(int, raw_input().split(' '))
a.sort()

i = N-3
while i > 0 and ((a[i] + a[i+1]) <= a[i+2]):
    i -= 1
if i > 0:
    print ' '.join(map(str, sorted([a[i], a[i+1], a[i+2]])))
elif i == 0 and (a[i]+a[i+1] > a[i+2]):
    print ' '.join(map(str, sorted([a[i], a[i+1], a[i+2]])))
else:
    print '-1'
