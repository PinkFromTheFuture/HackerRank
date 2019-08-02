'''https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays&isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    # initialize the swap counter
    swaps = 0

    # create an auxiliary hash table with the position of each element.
    # this way they will be indexed and I won't need to use list.index()
    # many times. This optimization reduces the complexity of the algorithm
    # from n^2 to 2n, making it pass the tests without a timeout
    aux_dict = {}
    for position, element in enumerate(arr):
        aux_dict[element] = position

    # loop through the array
    for i, element in enumerate(arr):  
        # see if the element in the current position is where it should be
        if (element == i+1):      
            # do nothing if the item is where it was supposed to be
            pass
        else:
            # deprecated because a new and more performant solution is below
            # find in the array the element that should be in the current position
            # right_element_position = arr[i:].index(i+1) + i
            # swap the current position for the number that should be in it
            # swap = arr[right_element_position]
            # arr[i] = arr[i]
            # arr[element] = swap
            # increase the counter of number of swaps
            # swaps += 1

            # save the value that is going to be swaped
            swap = arr[i]
            dict_swap = aux_dict[i+1]

            # swap the current position for the number that should be in it
            arr[i] = i+1
            arr[aux_dict[i+1]] = swap

            # replaced the swaped indexed value onto a new position
            aux_dict[swap] = dict_swap
            aux_dict[i+1] = i

            # increase the counter of number of swaps
            swaps += 1

    # return the answer
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
