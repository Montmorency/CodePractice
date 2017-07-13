#!/bin/python
import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Enter your code here. Read input from STDIN. Print output to STDOUT
a.sort()
result = [abs(a[i]-a[i+1]) for i in range(len(a)-1)]
print min(result)
