'''https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup'''
#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    min_jumps = 0

    len_of_c = len(c)

    # for val in c:
    #     print (val)

    i = 0
    while (i < len_of_c-2):
        # print('i+2 is {} int(c[i+2]) is {} jumping from {} to'.format(i+2, c[i+2], i), end=' ')
        if (int(c[i+2]) == 0):
            i += 2
            # print('{} by step of 2'.format(i))
        else:
            i += 1
            # print('{} by step of 1'.format(i))
        min_jumps += 1

    if len_of_c % 2 == 0 and i % 2 == 0:
        min_jumps += 1
    
    return min_jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
