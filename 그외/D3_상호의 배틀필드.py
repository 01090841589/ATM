import sys
sys.stdin = open("상호의배틀필드2.txt")
def shoot(y, x):
    Y = y
    X = x
    c = direc(Y, X)
    while True:
        Y = Y + DIR[c][0]
        X = X + DIR[c][1]
        if 0 <= Y < H and 0 <= X < W:
            if MAP[Y][X] == '*':
                MAP[Y][X] = '.'
                return
            elif MAP[Y][X] == '#':
                return
        else:
            return
def direc(i, j):
    if MAP[i][j] == '<':
        return 2
    elif MAP[i][j] == '>':
        return 3
    elif MAP[i][j] == '^':
        return 0
    elif MAP[i][j] == 'v':
        return 1
DIR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for test_case in range(1, T+1):
    H, W = map(int, input().split())
    MAP = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if MAP[i][j] == '<' or MAP[i][j] == '>' or MAP[i][j] == '^' or MAP[i][j] == 'v':
                NOW = [i, j]
    N = int(input())
    mov = list(input())
    for go in range(N):
        if mov[go] == 'S':
            shoot(NOW[0], NOW[1])
        elif mov[go] == 'U':
            if NOW[0] == 0:
                MAP[NOW[0]][NOW[1]] = '^'
            elif MAP[NOW[0]-1][NOW[1]] == '*' or MAP[NOW[0]-1][NOW[1]] == '#' or MAP[NOW[0]-1][NOW[1]] == '-':
                MAP[NOW[0]][NOW[1]] = '^'
            elif MAP[NOW[0]-1][NOW[1]] == '.':
                MAP[NOW[0]][NOW[1]] = '.'
                MAP[NOW[0]-1][NOW[1]] = '^'
                NOW[0] -= 1
        elif mov[go] == 'D':
            if NOW[0] == H-1:
                MAP[NOW[0]][NOW[1]] = 'v'
            elif MAP[NOW[0]+1][NOW[1]] == '*' or MAP[NOW[0]+1][NOW[1]] == '#' or MAP[NOW[0]+1][NOW[1]] == '-':
                MAP[NOW[0]][NOW[1]] = 'v'
            elif MAP[NOW[0]+1][NOW[1]] == '.':
                MAP[NOW[0]][NOW[1]] = '.'
                MAP[NOW[0]+1][NOW[1]] = 'v'
                NOW[0] += 1
        elif mov[go] == 'L':
            if NOW[1] == 0:
                MAP[NOW[0]][NOW[1]] = '<'
            elif MAP[NOW[0]][NOW[1]-1] == '*' or MAP[NOW[0]][NOW[1]-1] == '#' or MAP[NOW[0]][NOW[1]-1] == '-':
                MAP[NOW[0]][NOW[1]] = '<'
            elif MAP[NOW[0]][NOW[1]-1] == '.':
                MAP[NOW[0]][NOW[1]] = '.'
                MAP[NOW[0]][NOW[1]-1] = '<'
                NOW[1] -= 1
        elif mov[go] == 'R':
            if NOW[1] == W-1:
                MAP[NOW[0]][NOW[1]] = '>'
            elif MAP[NOW[0]][NOW[1]+1] == '*' or MAP[NOW[0]][NOW[1]+1] == '#' or MAP[NOW[0]][NOW[1]+1] == '-':
                MAP[NOW[0]][NOW[1]] = '>'
            elif MAP[NOW[0]][NOW[1]+1] == '.':
                MAP[NOW[0]][NOW[1]] = '.'
                MAP[NOW[0]][NOW[1]+1] = '>'
                NOW[1] += 1
    print('#{}'.format(test_case),end=' ')
    [print(''.join(MAP[a])) for a in range(H)]