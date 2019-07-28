'''https://www.hackerrank.com/challenges/validating-uid/problem
'''

#!/bin/python3

import re

# The first line contains an integer t, the number of test cases
t = int(input())

# The next t lines contains an employee's UID
uids = []
for _ in range(t):
    uids.append(input())

# It must contain at least 2 uppercase English alphabet characters
check_upper_characters = r'.*([A-Z].*){2}'
# it must contain at least 3 digits (0-9).
check_digit_characters = r'.*([0-9].*){3}'
# It should only contain alphanumeric characters (0-9, a-z & A-Z). 
# and there must be exactly 10 characters
check_valid_characters_and_length = r'([A-Za-z0-9]){10}$'
# No character should repeat. The regex bel
# ow matches if there are repeats
has_repeating_characters = r'.*(.).*\1'

for uid in uids:
    if (
        bool(re.match(check_upper_characters, uid))
        and bool(re.match(check_digit_characters, uid))
        and bool(re.match(check_valid_characters_and_length, uid))
        and not bool(re.match(has_repeating_characters, uid))
    ):
        print('Valid')
    else:
        print('Invalid')
