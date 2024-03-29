'''https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings'''

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
            # but I leave the line below because it could be used to
            # optimize the solution if the requirements were harder
            # s = s[0:i:] + s[i+1::]
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
