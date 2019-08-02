'''https://www.hackerrank.com/challenges/camelcase/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    # initialize the word counter with 1 because the first word starts with lowercase
    words = 1
    # loop through the string by each character
    for character in s:
        # count the number of upper case letters which mark the start of a word
        if character in ('ABCDEFGHIJKLMNOPQRSTUVXWYZ'):
            words += 1

    return words

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
