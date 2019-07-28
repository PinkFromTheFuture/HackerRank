# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

from math import sqrt

#The first line contains an integer, N, denoting the number of elements in the array. 
N = int(input())

#The second line contains N space-separated integers describing the respective elements of the array.
elements = list(map(int, input().split(' ')))

#Print the standard deviation on a new line, rounded to a scale of 1 decimal place (i.e., 12.3 format).

#First, we find the mean:
sum_of_elements = 0
for i in range (0, N):
    sum_of_elements += elements[i]

mean = sum_of_elements / N


#Next, we calculate the squared distance from the mean (xi - mean)^2 for each xi
sum_of_squared_distance = 0
for i in range (0, N):
    sum_of_squared_distance += (elements[i] - mean) ** 2


standard_deviation = sqrt(sum_of_squared_distance / N)

print("{:.1f}".format(standard_deviation))
