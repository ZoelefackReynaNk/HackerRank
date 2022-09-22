#!/bin/python3

import math
import os
import random
import re
import sys

def b10_to_b2(n):
    list_a = [ ]  #creat an emty list a
    i = 0 
    #n is divided by 2 and remainder is in the list
    while(abs(n) > 0):
       t = abs(n) % 2
       list_a.append(t)
       n = abs(n)//2   
       i += 1
    b = [ ] #another list b is created
    j = i - 1#this loop adds collects elements in reverse order
    while(j >= 0):
        b.append(list_a[j])
        # if list_a[i] == 1 and list_a[j-1] == 1:
        #     v += 1
        j = j-1
    v = 1
    # ones = [ ]
    # zeros = [ ]
    for i in range(j):
        if b[i] == 1 and b[i + 1] == 1:
            v += 1
            #ones.append(i)
        else:
            continue
            #zeros.append(i)
    print(v)
    # for x in range(len(ones) - 1):
    #     if ones[x +1] - ones[x] == 1:         
    #         v += 1
    #     else:
    #        continue
if __name__ == '__main__':
    n = int(input().strip())
    b10_to_b2(n)
