import sys
sys.stdin = open('벽돌꺠기.txt')

DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]
def search_depth(y, x, cnt):
    Y = y - 1
    if Y >= 0 and mat[Y][x] != 0:
        return search_depth(Y, x, cnt+1)
    else:
        return cnt


def find_block(y, x, k, dip):
    for c in DIR:
        Y = y
        X = x
        visited[Y][X] = 1
        for i in range(k-1):
            Y = Y+c[0]
            X = X+c[1]
            if 0 <= X < W and 0 <= Y < H and mat[Y][X] != 0:
                if mat[Y][X] > 1 and visited[Y][X] == 0:
                    find_block(Y, X, mat[Y][X], dip+1)
                visited[Y][X] = 1

def count_bombs(y, x, dep):
    global result, dicide
    print(find_block(y, x, mat[y][x], 0))
    bomb_sum = 0
    for i in range(H):
        bomb_sum += visited[i].count(1)
    if bomb_sum//dep > result:
        result = bomb_sum
        dicide = [y, x, dep]


def cascade():
    for x in range(W):
        for y in range(H-1, -1, -1):
            if mat[y][x] == 0:
                for Y in range(y-1, -1, -1):
                    if mat[Y][x] != 0:
                        mat[y][x], mat[Y][x] = mat[Y][x], mat[y][x]
                        break
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(H)]
    total = 0
    while N > 0:
        # [print(mat[i]) for i in range(H)]
        bomb = []
        for y in range(H):
            for x in range(W):
                if mat[y][x] > 1:
                    count = search_depth(y, x, 1)
                    if count <= N:
                        bomb.append([y, x, count])
        result = 0
        dicide = []
        if bomb:
            for start in bomb:
                visited = [[0]*W for _ in range(H)]
                count_bombs(start[0], start[1], start[2])
        else:
            total -= N
            if total < 0 :
                total = 0
            N = 0
            break
        # print(dicide)
        visited = [[0]*W for _ in range(H)]
        count_bombs(dicide[0], dicide[1], dicide[2])
        for y in range(H):
            for x in range(W):
                if visited[y][x] == 1:
                    mat[y][x] = 0
        # [print(mat[i]) for i in range(H)]
        cascade()
        # [print(mat[i]) for i in range(H)]
        N -= dicide[2]
        # print(N)
    for y in range(H):
        for x in range(W):
            if mat[y][x] != 0:
                total += 1
    print('#{} {}'.format(tc, total))