# Enter your code here. Read input from STDIN. Print output to STDOUT
N,K = map(int, raw_input().split(' '))
prices = map(int, raw_input().split(' '))
prices.sort()
total_purchase = K*[0]
n = 0
total_spent = 0
while n < N:
    for k in range(K):
        if len(prices) >= 1 and n < N:
            total_spent += (total_purchase[k]+1)*prices.pop()
            total_purchase[k] += 1
            n += 1
print total_spent
