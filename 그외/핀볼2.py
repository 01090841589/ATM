import sys, time
start=time.time()
sys.stdin = open("핀볼.txt")
DIR = [[0,1], [1, 0], [0, -1], [-1, 0]]
DIRS = [[2, 0, 3,1],[2, 3, 1, 0],[1, 3, 0, 2],[3, 2, 0, 1], [2, 3, 0, 1]]

def walls(num, c, Y, X):
    global score, gone, first_blood
    score += 1
    if DIRS[num][c] == 0 and X == N-1:
        score+=2
        return (c + 2) % 4
    elif DIRS[num][c] == 1 and Y == N-1:
        score+=2
        return (c + 2) % 4
    elif DIRS[num][c] == 2 and X == 0:
        score+=2
        return (c + 2) % 4
    elif DIRS[num][c] == 3 and Y == 0:
        score+=2
        return (c + 2) % 4
    else:
        return DIRS[num][c]
def hole(Y, X, c):
    global score, gone
    gone += 1
    for i in range(N):
        for j in range(N):
            if mat[i][j] == mat[Y][X]:
                if i != Y or j != X:
                    if c == 0 and j == N - 1:
                        score += 1
                        return Y, X, (c + 2) % 4
                    elif c == 1 and i == N - 1:
                        score += 1
                        return Y, X, (c + 2) % 4
                    elif c == 2 and j == 0:
                        score += 1
                        return Y, X, (c + 2) % 4
                    elif c == 3 and i == 0:
                        score += 1
                        return Y, X, (c + 2) % 4
                    else:
                        return i, j, c
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for i in range(N)]
    result = 0
    for y in range(N):
        first_blood = []
        for x in range(N):
            for c in range(4):
                score = 0
                gone = 0
                ori_y, ori_x = y, x
                if mat[y][x] == 0:
                    Y = y
                    X = x
                    while True:
                        if Y == ori_y and Y == ori_x and gone > 0:
                            break
                        if Y == ori_y and X == ori_x and score > 0:
                            if score > result:
                                result = score
                            break
                        Y = Y + DIR[c][0]
                        X = X + DIR[c][1]
                        if 0 <= X < N and 0 <= Y < N:
                            if mat[Y][X] == 0:
                                continue
                            elif 0 < mat[Y][X] <= 5:
                                if len(first_blood) == 0:
                                    first_blood = [Y, X, c]
                                if [Y, X, c] == first_blood and score == 0:
                                    break
                                c = walls(mat[Y][X] - 1, c, Y, X)
                                continue
                            elif 6 <= mat[Y][X] < 10:
                                Y, X, c = hole(Y, X, c)
                                continue
                            elif mat[Y][X] == -1:
                                break
                        else:
                            c = (c + 2) % 4
                            score += 1
                            continue

    print('#{} {}'.format(test_case, result))
    print(time.time()-start)