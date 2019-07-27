'''https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps'''
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # make a counter for the notes and the magazines, which is
    # basically a hash table or a dictionary with each word and
    # the amount of times it occurs.
    note_hash_table = Counter(note)
    magazine_hash_table = Counter(magazine)

    # We subtract the magazine words from the note words and
    # if it is an empity object it means that all words were
    # found, so this case evaluates to True
    if(note_hash_table - magazine_hash_table == {}):
        print ('Yes')
        return True
    else:
        print ('No')
        return False


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
