# Enter your code here. Read input from STDIN. Print output to STDOUT
def min_change(coins, diff):
    m = [[0 for _ in range(diff+1)] for _ in range(len(coins) +1)]
    for i in range(diff+1):
        m[0][i] = i
    for c in range(1, len(coins)+1):
        for r in range(1, diff+1):
            if coins[c-1] == r:
                m[c][r] = 1
            elif coins[c-1] > r:
                m[c][r] = m[c-1][r]
            else:
                m[c][r] = min(m[c-1][r],1+m[c][r-coins[c-1]])
    return m[-1][-1]

def distribute_chocolate(distribution):
    operations = 0
    coins = [1,2,5]
    distribution.sort()
    while len(distribution) > 1:
        max_val = distribution[-1]
        max_val_2 = distribution[-2]
        diff = max_val-max_val_2
        if diff != 0:
            min_changes = min_change(coins, diff)
            distribution[-1] -= diff
            operations += min_changes
        else:
          distribution.pop()
    return operations

#t = int(raw_input())
t = 1
for tc in range(t):
    arr = [2,2,7,8]
    N = len(arr)
    #N = int(raw_input())
    #arr = map(int, raw_input().split(' '))
    print distribute_chocolate(arr)
