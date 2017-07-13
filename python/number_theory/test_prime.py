def test_prime(p):
    if p == 1:
        print 'Not prime'
        return
    if p == 2:
        print 'Prime'
        return 
    if p % 2 == 0:
        print 'Not prime'
        return
    n = int(p**0.5)+1
    for x in range(3,n+1):
        if p % x == 0:
            print 'Not prime'
            return
    print 'Prime'
    
p = int(raw_input().strip())

for _ in xrange(p):
    n = int(raw_input().strip())
    test_prime(n)
