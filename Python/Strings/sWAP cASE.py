# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    # there is a built-in method from the string primitive that does this:
    # https://docs.python.org/3/library/stdtypes.html?highlight=swapcase#str.swapcase
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
