# Enter your code here. Read input from STDIN. Print output to STDOUT
# effectively have N/2 bins want to maximize each bin |[A_i-A_i-1]| 1 <= A_i <= B_i
"""
HackerRank answer to maximize sum(A_i - A_i-1) where a list B determines 1 <= A <= B_i.
"""
t = int(raw_input())
for _ in range(t):
    N = int(raw_input())
    B = map(int, raw_input().split(' '))
    lo = 0
    hi = 0
#Dynamic and Greedy algorithm?
    for i in range(1, N):
        lo, hi = (max(lo + 1-1, hi + abs(B[i-1]-1)), max(lo + abs(B[i]-1), hi + abs(B[i]-B[i-1])))        
    print max([lo,hi])
