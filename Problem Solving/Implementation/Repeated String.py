'''https://www.hackerrank.com/challenges/repeated-string/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # count the ocurrencies in the base string
    count_in_base_string = s.count('a')
    # print('count_in_base_string: {}'.format(count_in_base_string))

    # expand the base string and get the count from the ocurrencies of the whole string
    len_of_s = len(s)
    count = (n // len_of_s) * count_in_base_string
    # print('count: {}'.format(count))
    
    # add in the remaining ones from the non whole expansion
    # print('n % len_of_s: {}'.format(n % len_of_s))
    i = 0
    while (i < n % len_of_s):
        if s[i] == 'a':
            count += 1
        i += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
