'''https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting'''

#!/bin/python3

import os

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    quantity_of_toys_to_purchase = 0
    for price in prices:
        difference = k - price
        if difference > 0:
            quantity_of_toys_to_purchase += 1
            k = difference
        else:
            # break
            return quantity_of_toys_to_purchase
    return quantity_of_toys_to_purchase

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
