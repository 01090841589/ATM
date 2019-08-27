import sys
sys.stdin = open("ladder.txt")
DIR = [[0, -1], [0, 1], [1, 0]]
DIR2 = [[0, -1], [1, 0]]
DIR3 = [[0, 1], [1, 0]]
def find_ladder(y, x):
    global go, cnt, ori_x
    if go == 0:
        for c in range(2):
            X, Y = x + DIR2[c][1], y + DIR2[c][0]
            if 0 <= X < 100 and 0 <= Y < 100:
                if ladder[Y][X] == 1:
                    cnt += 1
                    go = c*2
                    return find_ladder(Y, X)
    elif go == 1:
        for c in range(2):
            X, Y = x + DIR3[c][1], y + DIR3[c][0]
            if 0 <= X < 100 and 0 <= Y < 100:
                if ladder[Y][X] == 1:
                    cnt += 1
                    go = c+1
                    return find_ladder(Y, X)
    else:
        for c in range(3):
            X, Y = x+DIR[c][1], y+DIR[c][0]
            if 0 <= X < 100 and 0 <= Y < 100:
                if ladder[Y][X] == 1:
                    cnt += 1
                    go = c
                    return find_ladder(Y, X)
for test_case in range(10):
    t = int(input())
    ladder = [list(map(int,input().split())) for i in range(100)]
    x = [i for i in range(100) if ladder[0][i] == 1]
    y = 0
    go, total, ori_x = 2, 1000, 0
    for a in x:
        cnt = 0
        find_ladder(y, a)
        if total > cnt:
            total = cnt
            result = a
    print('#{0} {1}'.format(t, result))