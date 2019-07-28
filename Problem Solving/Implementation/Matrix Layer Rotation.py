'''https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
'''

#!/bin/python3

def reverse(arr, i, j):
    for idx in range(int((j - i + 1) / 2)):
        arr[i + idx], arr[j - idx] = arr[j - idx], arr[i + idx]
 
 
def rotateList(A, K):
    '''performs a right rotation
    '''

    # K needs to be adjusted to len(A) - K for left rotation
    l = len(A)
    K %= len(A)
 
    reverse(A, l - K, l - 1)
    reverse(A, 0, l - K - 1)
    reverse(A, 0, l - 1)
 
    return A
 
 
def rotateLayers(N, M, R, layers):
    for layer in layers:
        rotateList(layer, len(layer) - R)
 
 
def matrixRotation(M, N, R, mat):
    # generate a list of layers
    l = int(min(N, M) // 2)
    layers = [[] for _ in range(l)]
    for level in range(l):
        top = (N - 1) - 2 * level
        side = (M - 1) - 2 * level

        # right
        for i in range(top):
            layers[level].append(mat[level][level + i])
        
        # down
        for j in range(side):
            layers[level].append(mat[level + j][level + top])
        
        # left
        for i in range(top):
            layers[level].append(mat[level + side][level + top - i])
        
        # up
        for j in range(side):
            layers[level].append(mat[level + side - j][level])
 
    # rotate each layer
    rotateLayers(N, M, R, layers)
 
    # fill the layers back in
    for level in range(l):
        top = (N - 1) - 2 * level
        side = (M - 1) - 2 * level
        
        # right
        for i in range(top):
            mat[level][level + i] = layers[level].pop(0)
        
        # down
        for j in range(side):
            mat[level + j][level + top] = layers[level].pop(0)
        
        # left
        for i in range(top):
            mat[level + side][level + top - i] = layers[level].pop(0)
        
        # up
        for j in range(side):
            mat[level + side - j][level] = layers[level].pop(0)
 

if __name__ == '__main__':
    M, N, R = map(int, input().split())
    mat = []
    for i in range(M):
        mat.append(list(map(int, input().split())))
 
    matrixRotation(M, N, R, mat)
 
    # print the answer
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in mat]))
