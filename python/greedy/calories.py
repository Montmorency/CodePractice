#!/bin/python
import sys
#The list calories contains integral numbers of calories:
#the quantity to minimize is sum(2^i*c for i in range(len(calories))
#where i number already eaten and c
n = int(raw_input().strip())
calories = map(int, raw_input().strip().split(' '))
calories.sort(reverse=True)
print sum([2**i*calories[i] for i in range(len(calories))])
