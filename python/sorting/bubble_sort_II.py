def bubble_sort(a):
    not_sorted = False
    i = 0
    num_swaps = 0
    while i<(len(a)-1):
        bubble = a[i]
        if bubble > a[i+1]:
            tmp = a[i+1]
            a[i+1] = bubble
            a[i] = tmp
            num_swaps += 1
            i=0
        else:
            i+= 1
    print 'Array is sorted in {} swap'.format(num_swaps)
    print 'First Element: {}'.format(a[0])
    print 'Last Element: {}'.format(a[-1])


a = [2,9,3,48,6,11,9]
print a
bubble_sort(a)
print a
