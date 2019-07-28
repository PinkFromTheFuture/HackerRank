'''https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings'''

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # create hash tables with the characters of the strings
    ca = Counter(a)
    cb = Counter(b)

    # put all the characters in a hash table and then subtract
    # the intersection two times (one for each of the strings)
    extras = (ca+cb) - (ca & cb) - (ca & cb)

    # return the sum of all values of the remaining hash table
    return sum(extras.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
