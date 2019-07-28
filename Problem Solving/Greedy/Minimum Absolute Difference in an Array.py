'''https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    # get the size of the array in a variable to call len only once
    size_of_arr = len(arr)
    # since we are talking about the minimum difference, we can
    # sort the array and then only compare adjacent elements
    arr.sort()

    # initialize the minimum difference with a high value
    minimum = arr[-1] - arr[0]

    # loop through the sorted array and compared ajacent elements
    for i in range(0, size_of_arr-1):
        difference = abs(arr[i] - arr[i+1])
        # if the difference is smaller than the minimum, update it
        if difference < minimum:
            minimum = difference

    return minimum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
