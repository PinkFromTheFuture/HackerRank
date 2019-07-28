# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # # implementation using regualr syntax
    # answer_list = []
    # for ix in range(x+1):
    #     for iy in range(y+1):
    #         for iz in range(z+1):
    #             # where the sum is not equal to n
    #             if(ix+iy+iz != n):
    #                 answer_list.append([ix,iy,iz])
    # # print a list of all possible coordinates 
    # print(answer_list)

    # implementation using fancy syntax:
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])
