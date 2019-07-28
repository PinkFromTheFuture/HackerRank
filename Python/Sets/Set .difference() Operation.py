# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
english_rolls = set(map(int, input().split()))
b = int(input())
french_rolls  = set(map(int, input().split()))

print(len(english_rolls-french_rolls))
