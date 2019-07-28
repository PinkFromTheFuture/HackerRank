# https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
english_rolls = set(map(int, input().split()))
b = int(input())
french_rolls  = set(map(int, input().split()))

# print the union of both sets
print(len(english_rolls|french_rolls))
