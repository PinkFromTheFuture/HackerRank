# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

# The first line contains the number of items
n = int(input())

# An OrderedDict is a dictionary that remembers the order
# of the keys that were inserted first
items = OrderedDict()

# The next n lines contains the item's name and price, separated by a space
for _ in range(n):
    item_name, separator, net_price = input().rpartition(' ')
    if item_name not in items:
        # add item to dictionary if it does not already exists
        items[item_name] = int(net_price)
    else:
        # increase the item value if it already is in the dictionary
        items[item_name] += int(net_price)

# print each item_name and net_price in order of its first occurrence. 
for item in items:
    print('{} {}'.format(item, items[item]))
