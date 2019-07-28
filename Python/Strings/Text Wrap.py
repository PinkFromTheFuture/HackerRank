# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    # # manual implementation:
    # wrapped = ''
    # i = 0
    # while i < len(string):
    #     wrapped += string[i:i+max_width:]+'\n'
    #     i += max_width
    # return wrapped
    
    # implementation using the given lib:
    # textwrap.fill(text, width=70, **kwargs) Wraps the single
    # paragraph in text, and returns a single string containing
    # the wrapped paragraph.
    return textwrap.fill(string, width=max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
