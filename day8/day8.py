import math
import os
import random
import re
import sys

def reverse(array):
    i = len(array) - 1 
    while i >= 0:
        print(array[i], end = " ")
        i = i -1 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    reverse(arr)
