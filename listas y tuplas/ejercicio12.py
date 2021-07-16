matA = [
    [1, 2, 3],
    [4, 5, 6]
]

matB = [
    [-1, 0],
    [ 0, 1],
    [ 1, 1]
]

res = [
    [0, 0], 
    [0, 0]
]

for i in range(len(matA)):
    for j in range(len(matB[0])):
        for k in range(len(matB)):
            res[i][j] += matA[i][k] * matB[k][j]

print(res)
