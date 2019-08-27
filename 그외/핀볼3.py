import sys
sys.stdin = open("핀볼.txt")
DIR = [[0,1], [1, 0], [0, -1], [-1, 0]]
DIRS = [[2, 0, 3,1],[2, 3, 1, 0],[1, 3, 0, 2],[3, 2, 0, 1], [2, 3, 0, 1]]

def change(y, x, c, k):
    global score
    if 1 <= k <= 5:
        c = DIRS[k-1][c]
        score += 1
        return y, x, c
    if 6 <= k <= 10:
        # print(worm[k-6])
        for i in worm[k-6]:
            if [y, x] != i:
                y, x = i[0], i[1]
                break
        return y, x, c


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    mat = [[5]+list(map(int, input().split()))+[5] for i in range(N)]
    mat.insert(0, [5]*(N+2))
    mat.append([5]*(N+2))
    worm = [[] for _ in range(5)]
    for y in range(N+2):
        for x in range(N+2):
            if mat[y][x] > 5:
                worm[mat[y][x]-6].append([y, x])
    result = 0
    for y in range(1, N+1):
        for x in range(1, N+1):
            for c in range(4):
                score = 0
                gone = 0
                ori_y, ori_x = y, x
                if mat[y][x] == 0:
                    Y = y
                    X = x
                    while True:
                        Y += DIR[c][0]
                        X += DIR[c][1]
                        if mat[Y][X] > 0:
                            # print(Y, X, c, score)
                            Y, X, c = change(Y, X, c, mat[Y][X])
                        if mat[Y][X] == -1:
                            break
                        if score == 0 and mat[Y][X] == 0:
                            break
                        if ori_y == Y and ori_x == X:
                            break
                    if result < score:
                        result = score
    print('#{} {}'.format(test_case,result))