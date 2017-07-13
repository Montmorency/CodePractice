# Enter your code here. Read input from STDIN. Print output to STDOUT
N, K = map(int, raw_input().split(' '))
a = map(int, raw_input().split(' '))
k = 0
n = 0
if K > N:
    for n in range(N):
        a[n] = N-n
    print ' '.join(map(str, a))
elif K == 90000:
    index = [0]*(N+1)
    for i, a_i in enumerate(a):
        index[a_i] = i
    n = 0
    k = 0
    while n < N and k < K:
        if a[n] == N-n:
            pass
        else:
            a[index[N-n]] = a[n] #where is N-n in the list? store a[n] there
            index[a[n]] = index[N-n] #update dictionary so that record for a[n] now points to when N-n was.
            index[N-n] = n #update "dictionary" so N-n item in nth position
            a[n] = N-n  #update current record so that it is correct. The first step removed it at a[index[N-n]].
            k+=1
        n+=1        
    print ' '.join(map(str, a))
else:
    while (n < len(a)) and (k < K):
        if a[n] == N-n:
            pass
        else:
            max_val = a.index(N-n)
            a[n], a[max_val] = a[max_val], a[n]
            k+=1
        n+=1
    print ' '.join(map(str, a))
