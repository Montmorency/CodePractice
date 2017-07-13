#!/bin/python
import sys

def super_reduced_string(s):
    s= list(s)
    n = 0
    while n < len(s)-1:
        if s[n] == s[n+1]:
            del s[n]
            del s[n]
            n = 0
        else:
            n += 1
    if len(s) > 0:
        return ''.join(s)
    else:
        return 'Empty String'

s = raw_input().strip()
result = super_reduced_string(s)
print(result)
