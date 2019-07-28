# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
english_rolls = set(map(int, input().split()))
b = int(input())
french_rolls  = set(map(int, input().split()))

# print the intersection of both sets
print(len(english_rolls^french_rolls))
