# https://www.hackerrank.com/challenges/py-set-add/problem

# The first line contains an integer n, the total number of country stamps
n = int(input())

# The next n lines contains the name of the country where the stamp is from
countries = set()
for _ in range(n):
    countries.add(input())

# Find the total number of distinct country stamps
# put them in a set to get the unique elements
# print the length of the unique elements set
print(len(countries))
