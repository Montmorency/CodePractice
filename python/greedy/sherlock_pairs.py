# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for _ in range(t):
    m_ij = 0
    N = int(raw_input())
    good_pairs = []
    for i in range(1, N+1):
        if i%3 == 0 and (N-i)%5==0:
            good_pairs.append((i,N-i))
    if len(good_pairs)>0:
        good_pairs.sort(key=lambda x:x[0])
        print int(good_pairs[-1][0]*'5'+good_pairs[-1][1]*'3')
    elif len(good_pairs)==0 and N%3==0:
        print '5'*N
    elif len(good_pairs)==0 and N%5==0:
        print '3'*N
    else:
        print '-1'
