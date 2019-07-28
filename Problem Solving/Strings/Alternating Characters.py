'''https://www.hackerrank.com/challenges/alternating-characters/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    previous_char = -1
    deletions_counter = 0
    for i, char in enumerate(s):
        if char == previous_char:
            # no need to delete anything, just increase the counter
            deletions_counter += 1
        else:
            # since they are different, change the previous character
            previous_char = char
    return deletions_counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
