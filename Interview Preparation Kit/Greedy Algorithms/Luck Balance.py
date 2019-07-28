'''https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    # sort the contests by the luck value in descending order
    contests.sort(key=lambda contest:contest[0], reverse=True)
    # loop through all of them
    for contest in contests:
        # non important contests, can lose them all
        if(contest[1] == 0):
            luck = luck + contest[0]
        # important contests, can be lost or not, depending on k
        else:
            # can still lose a contest
            if k > 0:
                luck = luck + contest[0]
                k = k - 1
            # can no longer lose a contest
            else:
                luck = luck - contest[0]
    return luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
