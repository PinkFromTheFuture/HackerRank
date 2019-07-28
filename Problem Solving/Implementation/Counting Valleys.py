'''https://www.hackerrank.com/challenges/counting-valleys/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.

def countingValleys(n, s):
    level = 0
    is_in_valley = False
    valleys_visited = 0

    for char in s:
        if char.upper() == 'D':
            level -= 1
            if not is_in_valley and level == -1:
                is_in_valley = True
                valleys_visited += 1
        else:
            level += 1
            if is_in_valley and level == 0:
                is_in_valley = False
    
    return valleys_visited
        
        
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
