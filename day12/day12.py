#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(array):
    new = [ ]
    A = [ ]
    for R in range(4):
        for C in range(4):
            ##new.append(array[R][C])
    #print(new) 
            sum = 0
            for r in range(R, R + 3):
                for c in range(C, C + 3):
                    sum += array[r][c]
                    #A.append(array[r][c])
            new.append(sum)
    print(max(new))        
  
if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    hourglass(arr)
