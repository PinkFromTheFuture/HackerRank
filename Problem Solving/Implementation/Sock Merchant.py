'''https://www.hackerrank.com/challenges/sock-merchant/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    swap_array = []
    pairs_counter = 0

    for element in ar:
        if element in swap_array:
            swap_array.remove(element)
            pairs_counter += 1
        else:
            swap_array.append(element)
    
    return pairs_counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
