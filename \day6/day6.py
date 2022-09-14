#!/bin/python3

import math
import os
import random
import re
import sys

def multiples(n):
    for i in range(1, 11):
        x = n*i
        print(f"{n} x {i} = {x}")
        
if __name__ == '__main__':
    n = int(input().strip())
    multiples(n)
