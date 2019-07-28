'''https://www.hackerrank.com/challenges/greedy-florist/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, prices):
    prices.sort(reverse=True)

    minimum_cost = 0
    i = 0
    for i in range(len(prices)):
        minimum_cost += prices[i]*(i//k+1)

    # # alternative implementation 1, my first implementation, with a wierd structure:
    # previously_purchased_flowers = 0
    # while (i < len(prices)):
    #     for _ in range(k):
    #         if i < len(prices):
    #             minimum_cost += prices[i] * (previously_purchased_flowers+1)
    #             i+=1
    #         else:
    #             break
    #     previously_purchased_flowers+=1

    # # alternative implementation 2:
    # minimum_cost = 0
    # for i in range(len(prices) // k+1):
    #     minimum_cost += sum(prices[i*k:i*k+k]) * (i+1)

    return minimum_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
