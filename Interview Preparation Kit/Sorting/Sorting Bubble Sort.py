'''https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting'''

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# store the number of swaps on the counter variable
numSwaps = 0
for i in range (0, n):
    for j in range (0, n-1):
        if (a[j] > a[j+1]):
            # swap the numbers
            swap = a[j+1]
            a[j+1] = a[j]
            a[j] = swap
            # increment the swap counter
            numSwaps+=1

# print output according to the definition
print("Array is sorted in {} swaps.".format(numSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[n-1]))