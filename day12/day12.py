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

        

# Edit 2:
# #!/bin/python3

# def hourglass(array):
#     r = 3
#     c = 2
#     A = [ ]
#     hg = [ ]
    
#     for p in range(r):
#         for i in range(3):
#             for j in range(i, c+i):
#                 f = 0
#                 while f < 3:
#                     for _ in range(2):
#                         hg.append(array[f][_])
#                     f += 1
#                 Sum = 0
#                 for i in range(len(arr)):
#                 Sum = Sum + arr[i]
#                 #print (Sum)
#                 A.append(sum)
#     # N = [ ]
#     # M = [ ]
    
#     # r = 0
#     # while r < 5:
#     #     c = 2
#     #     while c <= 5:
#     #         f = 0
#     #         while f < 3:
#     #             for _ in range(f, c):
#     #                 N.append(array[f][_])
#     #             f += 1
#     #         M.append(N)
#     #         c += 1    
#     #     r += 1
#     # f += 1

