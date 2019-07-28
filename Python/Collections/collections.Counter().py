# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

# initialize the acumulator for the answer
amount_of_money_earned  = 0

# The first line contains the number of shoes
x = int(input())

# The second line contains the space separated list
# of all the shoe sizes in the shop
shoe_sizes = Counter(list(input().split(' ')))

# The third line contains the number of customers
n = int(input())

# The next lines contain the space separated values of the shoe
# size desired by the customer and xi, the price of the shoe
for _ in range(n):
    size, price = input().split(' ')
    # Customers who are willing to pay amount of money only if
    # they get the shoe of their desired size:
    if shoe_sizes[size]:
        amount_of_money_earned += int(price)
        # reduce the counter of available sizes
        shoe_sizes[size] -= 1

print(amount_of_money_earned)
