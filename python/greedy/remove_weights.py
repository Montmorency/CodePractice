# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
weights = map(int, raw_input().split(' '))
#take as many toys as possible at each step:
min_weight = min(weights)
max_weight = max(weights)
index = [0]*10001
for w in weights:
    index[w] += 1
units = 0
i = 0
while i <= max_weight:
    if index[i] > 0:
        i += 4
        units += 1
    i += 1
print units
