'''https://www.hackerrank.com/challenges/compare-the-triplets/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):

    result_array = [0,0]

    for i in range(0,3):
        #print('comparing {} with {} from position {}'.format(a[i],b[i],i))
        if (a[i] < b[i]):
            #print('increasing 1')
            result_array[1] += 1
        if (a[i] > b[i]):
            #print('increasing 0')
            result_array[0] += 1

    return result_array
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
