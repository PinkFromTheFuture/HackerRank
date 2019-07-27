'''https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_array = []
    for i in range(0, 6-2):
        for j in range(0, 6-2):
            # initialize the sum
            hourglass = 0
            # add first line
            hourglass += arr[i][j]     + arr[i][j+1]   + arr[i][j+2]
            # add second line
            hourglass += arr[i+1][j+1]
            # add third line
            hourglass += arr[i+2][j]   + arr[i+2][j+1] + arr[i+2][j+2]
            # append to the array containing all sums
            hourglass_array.append(hourglass)
    # return the answer from the sums
    return max(hourglass_array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
