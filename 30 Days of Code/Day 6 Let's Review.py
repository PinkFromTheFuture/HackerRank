'''https://www.hackerrank.com/challenges/30-review-loop/problem
'''

'''Given a string, S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as 2
space-separated strings on a single line (see the Sample below
for more detail).
Note: 0 is considered to be an even index.
'''

#Input Format
#The first line contains an integer, T (the number of test cases). 
test_cases = int(input())

#Each line i of the T subsequent lines contain a String, S.
strings = []
for i in range(0, test_cases):
    string = input()
    even_chars = []
    odd_chars = []
    for j in range(0, len(string)):
        if(j%2 == 0):
            even_chars.append(string[j])
        else:
            odd_chars.append(string[j])
    two_separated_string = "{} {}".format(''.join(even_chars), ''.join(odd_chars))
    strings.append(two_separated_string)

for i in range(0, test_cases):
    print(strings[i])
