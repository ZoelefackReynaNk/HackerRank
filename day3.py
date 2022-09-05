#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    tip = (tip_percent/100)*meal_cost
    taxes = (tax_percent/100)*meal_cost
    total_cost = meal_cost + tip + taxes
    if (total_cost - int(total_cost)) >= 0.5:
        print(int(total_cost)+1)
    elif (total_cost - int(total_cost)) == 0:
        print(total_cost)
    else:
        print(int(total_cost))
    # Write your code here

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
