# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    set_of_array = set(array)
    return sum(set_of_array)/len(set_of_array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
