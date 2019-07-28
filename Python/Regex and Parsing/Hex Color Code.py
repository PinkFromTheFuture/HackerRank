# https://www.hackerrank.com/challenges/hex-color-code/problem

import re

n = int(input())

matches = []
for _ in range(n):
    found = re.findall(r'(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})',input())
    for match in found:
        if match != '':
            print(match)
            matches.append(match)
