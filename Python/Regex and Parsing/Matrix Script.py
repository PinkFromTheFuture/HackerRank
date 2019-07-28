'''https://www.hackerrank.com/challenges/matrix-script/problem
'''

#!/bin/python3

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# txt = ''
# for j in range(m):
#     for i in range(n):
#         txt += matrix[i][j]
txt = ''.join(matrix[i][j] for j in range(m) for i in range(n))

# txt = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])',' ',txt)
txt = re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', txt)
print(txt)
