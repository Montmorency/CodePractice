#!/bin/python

import sys

def final_energy(n, k, c):
    energy = 100
    cloud = 0
    while True:
        energy -= 1
        cloud = (cloud + k)%n
        if c[cloud] == 1:
            energy -= 2
        if cloud == 0:
            return energy
    
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
print final_energy(n,k,c)
