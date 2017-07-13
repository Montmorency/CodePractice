#!/bin/python

import sys

def timeConversion(s):
    # Complete this function
    split_time = s.split(':')
    am_pm = split_time[2][-2:]
    if am_pm =='PM':
        if 12 != int(split_time[0]):
            hour = int(split_time[0])+12
        else:
            hour = 12
    elif int(split_time[0]) == 12 and am_pm=='AM':
        hour = '00'
    else:
        hour = split_time[0]
    return '{}:{}:{}'.format(hour, split_time[1], split_time[2][:2])

s = raw_input().strip()
result = timeConversion(s)
print(result)
