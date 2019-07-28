'''https://www.hackerrank.com/challenges/py-if-else/problem
'''

#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())

    # if n is odd:
    if n%2==1:
        print('Weird')
    # if n is even:
    else:
        if 2 <= n and n <= 5:
            print('Not Weird')
        elif 6 <= n and n <= 20:
            print('Weird')
        elif 20 < n:
            print('Not Weird')
