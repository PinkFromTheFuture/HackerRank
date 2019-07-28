'''https://www.hackerrank.com/challenges/reduced-string/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):

    # convert the string to a list
    string_list = list(s)

    # initiate loop variables
    i = 0
    tail = len(string_list)-1

    # loop through the whole list of characters of the string
    while (i < tail):
        if(i > 0 and string_list[i] == string_list[i-1]):
                del string_list[i-1]
                del string_list[i]
                tail = tail - 2
                i = i - 1

        if(string_list[i] == string_list[i+1]):
            del string_list[i+1]
            del string_list[i]
            tail = tail - 2
            if ( 0 < i ):
                i = i - 1
        else:
            i = i + 1

    to_return = "".join(string_list)

    # convert the reduced list into a string and return it
    # or return 'Empty String' if it is the case
    if( 0 < len(string_list) ):
        return "".join(string_list)
    else:
        return "Empty String"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
