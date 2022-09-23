#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(array):
    N = [ ]
    M = [ ]
    
    r = 0
    while r < 5:
        c = 2
        while c <= 5:
            f = 0
            while f < 3:
                for _ in range(f, c):
                    N.append(array[f][_])
                f += 1
            M.append(N)
            c += 1    
        r += 1
    f += 1

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
