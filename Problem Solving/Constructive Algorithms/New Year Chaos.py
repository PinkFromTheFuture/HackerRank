'''https://www.hackerrank.com/challenges/new-year-chaos/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q, n):
    bribes = 0

    # the list index start from 0 while the elements start counting from 1
    # so we subtract 1 from each element to make them match
    Q = [P-1 for P in q]
    for i, element in enumerate(Q):
        if element - i > 2:
            print('Too chaotic')
            return

        # if an element is smaller than it's position, it means it has been bribed
        # by those elements that are greater than him. So we count those elements
        # that are greater and come before the bribed element. We subtract 1 from
        # the element because bribers can't go past more than 1 element. We also
        # get the max between that and 0 so we don't compare with negative values
        else:
            for j in range(max(element-1,0), i):
                if (element < Q[j]):
                    bribes += 1
        
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q, n)
