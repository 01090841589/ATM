import sys
sys.stdin = open("디저트카페.txt")
DIR = [[1, -1], [1, 1], [-1, 1], [-1, -1]]
def rectan_search(y, x, x_ran, y_ran, visited):
    global result
    Y = y
    X = x
    if x == 0 and y == 0:
        return
    if x == 0 and y == N-1:
        return
    if x == N-1 and y == 0:
        return
    if x == N-1 and y == N-1:
        return
    if x_ran + y_ran > N-1:
        return
    for c in DIR:
        if (x_ran+y_ran)*2 < result:
            break
        if sum(c) // 2 :
            for i in range(y_ran):
                y += c[0]
                x += c[1]
                if 0 <= x < N and 0 <= y < N:
                    if mat[y][x] not in visited:
                        visited.append(mat[y][x])
                    elif c == [1, 1]:
                        return
                    else:
                        visited = []
                        break
                else:
                    return
        else:
            for i in range(x_ran):
                y += c[0]
                x += c[1]
                if 0 <= x < N and 0 <= y < N:
                    if mat[y][x] not in visited:
                        visited.append(mat[y][x])
                    elif c == [1, -1]:
                        return
                    else:
                        visited = []
                        break
                else:
                    return
        if visited == []:
            break
    if result <= len(visited):
            result = len(visited)
    rectan_search(Y, X, x_ran+1, y_ran, [])
    rectan_search(Y, X, x_ran, y_ran+1, [])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for y in range(N-2):
        for x in range(N-1):
            rectan_search(y, x, 1, 1, [])
    if result <= 2:
        result = -1
    print('#{} {}'.format(tc, result))