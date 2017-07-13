#!/bin/python

import sys
from itertools import combinations

def max_min_sum(arr):
    min_num = float('Inf')
    max_num = 0
    for c in combinations(arr,4):
        total = sum(c)
        if total < min_num:
            min_num = total
        if total > max_num:
            max_num = total
    return min_num, max_num
    

arr = map(int, raw_input().strip().split(' '))
a,b = max_min_sum(arr)
print a, b
