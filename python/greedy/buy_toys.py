# Enter your code here. Read input from STDIN. Print output to STDOUT
N, K = map(int, raw_input().split(' '))
prices = map(int, raw_input().split(' '))
prices.sort()
toys = 0
spent = 0
#print prices
for p in prices:
    spent += p
    if spent > K:
        break
    else:
        toys +=1
print toys
