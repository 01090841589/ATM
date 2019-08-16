DIR = [[0,1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
def queen(y, x, arr):
    global result
    Y = y+arr[0]
    X = x+arr[1]
    if 0 <= X < N and 0 <= Y < N:
        if mat[Y][X] == 0:
            queen(Y, X, arr)
            print(Y, X)
        else :
            result = 1
N = 4
mat = []
for i in range(N):
    mat.append([0]*4)
for i in range(N):
    print(mat[i])
print(mat)
for x in range(N):
    for y in range(N):
        result = 0
        for arr in DIR:
            queen(y, x, arr)
        print(result)
        if result == 0:
            mat[x][y] = 1

for i in range(N):
    print(mat[i])