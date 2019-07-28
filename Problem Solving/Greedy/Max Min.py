'''https://www.hackerrank.com/challenges/angry-children/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    # start the result with a high value, max int value
    minimum_unfairness = 0xFFFFFFFF

    arr.sort(reverse=True)
    # k is the number of elements. we adjust it to the distance
    # from the first to the last, to avoid during math more than once
    distance = k-1

    for i in range(len(arr)-distance):
        unfairness = arr[i] - arr[i+distance]
        if unfairness < minimum_unfairness:
            minimum_unfairness = unfairness

    return minimum_unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
