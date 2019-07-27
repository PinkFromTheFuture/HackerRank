'''https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d, n):
    # no need to rotate too many times, only the remainder of the ring division
    d_ring = (d % n)
    
    return a[d_ring:] + a[:d_ring]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d, n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
