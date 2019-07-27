'''https://www.hackerrank.com/challenges/flipping-bits/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=miscellaneous'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    # in python ~  is the Binary Ones Complement. It is unary
    # and has the effect of 'flipping' bits.
    # to return the result as an unsigned integer, it's
    # necessary to add the complement, 2**32 or (1 << 32)
    # return ~n + 2**32
    
    # another way to do it would be to get the AND of the bits
    # with the maximun unsigned integer. this might be actually faster
    return ~n & 0xffffffff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
