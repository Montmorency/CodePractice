t = int(raw_input())
for _ in range(t):
    N = int(raw_input())
    grid = []
    for n in range(N):
        grid.append(sorted(list(raw_input())))
    possible = True
    j = 0                
    while possible == True and j < N:
        for i in range(N-1):
            if grid[i][j] <= grid[i+1][j]:
                pass
            else:
                possible = False
                break
        j+= 1
    if not possible: print 'NO'
    if possible: print 'YES'
