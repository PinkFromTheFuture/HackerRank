'''https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps'''
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # create hash tables with the characters of the strings
    c1 = Counter(s1)
    c2 = Counter(s2)

    # check for the intersection of hash tables
    if(c1 & c2 == {}):
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
