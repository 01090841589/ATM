import sys
sys.stdin = open('p4.txt')

DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def climb(y, x, cnt, can, visited):
    global total, K
    for c in DIR:
        Y = y + c[0]
        X = x + c[1]
        if 0 <= X < N and 0 <= Y < N and [Y,X] not in visited:
            if mat[Y][X] < mat[y][x]:
                visited.append([Y, X])
                climb(Y, X, cnt + 1, can, visited)
                visited.pop()
            elif can == 1:
                for c in DIR:
                    yy = Y + c[0]
                    xx = X + c[1]
                    if yy != y or xx != x:
                        if 0 <= xx < N and 0 <= yy < N:
                            for i in range(1, 1 + K):
                                if mat[Y][X]-i >0:
                                    if mat[yy][xx] < mat[Y][X] - i and mat[Y][X] -i < mat[y][x]:
                                        visited.append([Y, X])
                                        visited.append([yy, xx])
                                        climb(yy, xx, cnt + 2, can - 1, visited)
                                        visited.pop()
                                        visited.pop()
    if can == 1:
        for c in DIR:
            Y = y + c[0]
            X = x + c[1]
            if 0 <= X < N and 0 <= Y < N:
                for i in range(1, 1 + K):
                    if [Y, X] not in visited:
                        if mat[Y][X]-i < mat[y][x]:
                            cnt += 1
                            if total < cnt:
                                total = cnt
                            return

    if total < cnt:
        total = cnt

T = int(input())
for tc in range(1, 1+T):

    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for i in range(N)]
    total = 0
    top = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] > top:
                top = mat[i][j]
    for i in range(N):
        for j in range(N):
            if mat[i][j] == top:
                climb(i, j, 1, 1, [[i, j]])
    print('#{} {}'.format(tc, total))
