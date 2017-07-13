from collections import deque
def merge(a, b):
    result = []
    swaps = 0
    a = deque(a)
    b = deque(b)
    while a and b:
        if a[0] > b[0]:
            swaps += len(a)
            result.append(b.popleft())
        else:
            result.append(a.popleft())
    while a:
        result.append(a.popleft())
    while b:
        result.append(b.popleft())
    return result, swaps

def merge_sort(a):
    if len(a) > 1:
        left = a[:len(a)/2]
        right = a[(len(a)/2):]
        left_sort, swaps_l  = merge_sort(left)
        right_sort, swaps_r  = merge_sort(right)
        result, swaps = merge(left_sort, right_sort)
        return result, swaps + swaps_l + swaps_r
    else:
        return a, 0

def count_inversions(a):
    a, swaps = merge_sort(a)
    return swaps
