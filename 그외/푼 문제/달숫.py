DIR = [[0,1], [1, 0], [0,-1], [-1, 0]]
def snail(y, x, c):
    global num
    Y = y + DIR[c][0]
    X = x + DIR[c][1]
    if num > len(mat)**2:
        return
    if 0 <= X < N and 0 <= Y < N:
        if mat[Y][X] == 0:
            mat[Y][X] = num
            num += 1
            return snail(Y, X, c)
        if mat[Y][X] != 0:
            return snail(Y-DIR[c][0], X-DIR[c][1], (c+1)%4)
    else:
        snail(Y-DIR[c][0], X-DIR[c][1], (c+1)%4)
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    num = 1
    mat = [[0]*N for _ in range(N)]
    snail(0, -1, 0)
    print('#{}'.format(test_case))
    for i in range(N):
        print(' '.join(list(map( str, mat[i]))))
