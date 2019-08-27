import sys
sys.stdin = open("정사각형방.txt")
DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def climb(y, x, n):
    global total, num, ori_y, ori_x
    while True:
        flag = 0
        for i in range(4):
            Y = y+DIR[i][0]
            X = x+DIR[i][1]
            if 0 <= Y < N and 0 <= X < N:
                if square[Y][X] == square[y][x]+1:
                    y, x, n = Y, X, n+1
                    flag = 1
                    break
        if i == 3 and flag == 0:
            if total < n:
                total = n
                num = square[ori_y][ori_x]
                return
            elif total == n:
                num = min(num, square[ori_y][ori_x])
                return
            else :
                return
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    total = 1
    num = 0
    for a in range(N):
        for b in range(N):
            ori_y, ori_x = a, b
            climb(a, b, 1)
    print('#{} {} {}'.format(tc,num, total))