'''https://www.hackerrank.com/challenges/30-conditional-statements/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #Given an integer, N, perform the following conditional actions:
    N = int(input())

    #If  is odd, print Weird
    if (N % 2 == 1):
        print("Weird")

    else:
        #If  is even and in the inclusive range of 2 to 5, print Not Weird
        if(N % 2 == 0 and N >= 2 and N <= 5):
            print("Not Weird")

        #If  is even and in the inclusive range of 6 to 20, print Weird
        elif(N % 2 == 0 and N >= 6 and N <= 20):
            print("Weird")

        #If  is even and greater than 20, print Not Weird
        else:
            print("Not Weird")

