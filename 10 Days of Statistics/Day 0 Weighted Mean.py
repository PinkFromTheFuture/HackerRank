# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

#The first line contains an integer, N, denoting the number of elements in arrays X and W. 
N = int(input())

#The second line contains N space-separated integers describing the respective elements of array X. 
X = list(map(int, input().split(' ')))

#The third line contains N space-separated integers describing the respective elements of array W.
W = list(map(int, input().split(' ')))

dividend=0
for i in range (0, N):
    dividend += X[i]*W[i]

divisor = sum(W)

weighted_mean = dividend / divisor

print("{:.1f}".format(weighted_mean))
