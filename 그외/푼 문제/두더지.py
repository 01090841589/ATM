import sys
sys.stdin = open("두더지.txt")
DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def finding(y, x):
    global total, num, NUM
    for i in range(4):
        Y = y+DIR[i][0]
        X = x+DIR[i][1]
        if 0 <= Y < N and 0 <= X < N:
            if MAP[Y][X] == 1:
                MAP[Y][X] = 0
                num += 1
                finding(Y, X)
    if i == 3:
        total = max(total, num)
# T = int(input())
for test_case in range(1, 2):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    total = 1
    NUM = []
    for a in range(N):
        for b in range(N):
            if MAP[a][b] ==1:
                num = 0
                finding(a, b)
                NUM.append(total)
    NUM.sort(reverse=True)
    print(len(NUM))
    [print(NUM[i]) for i in range(len(NUM))]