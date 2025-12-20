def diagonal_difference(arr):
    n=len(arr)
    d1=0
    d2=0
    for i in range(n):
        d1=d1+arr[i][i]
        d2=d2+arr[i][n-i-1]
    return abs(d1-d2)
matrix=[[1,5,6],
        [5,7,8],
        [8,7,4]
]
diagonal_difference(matrix)
print(diagonal_difference(matrix))



